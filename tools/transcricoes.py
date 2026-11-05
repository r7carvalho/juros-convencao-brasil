#!/usr/bin/env python3
"""Baixa metadados e transcrições de vídeos do YouTube para dados/brutos/transcricoes/.

Roda no GitHub Actions (.github/workflows/transcricoes.yml), porque a rede da sessão de nuvem
bloqueia o YouTube. Usa yt-dlp (metadados, busca e legendas automáticas) e, como alternativa para
o texto, youtube-transcript-api.

Uso:
  python3 tools/transcricoes.py --ids ID1 ID2 ...           # vídeos indicados
  python3 tools/transcricoes.py --busca "termo" --max 25    # lista resultados de busca
  python3 tools/transcricoes.py --busca "termo" --baixar 10 # baixa os N primeiros da busca

Saída: um JSON por vídeo (<id>.json: metadados, segmentos com tempo e texto corrido) e, na
busca, _busca-<slug>.json com a lista de resultados.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request

SAIDA = os.path.join("dados", "brutos", "transcricoes")
LINGUAS = ["pt", "pt-BR", "pt-PT", "en"]


def log(*a):
    print(*a, flush=True)


def metadados(vid):
    import yt_dlp
    opts = {"quiet": True, "skip_download": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
    return info


def texto_de_vtt(vtt):
    """Converte WebVTT de legenda automática em segmentos sem repetição."""
    segs, vistos = [], set()
    bloco_t = None
    for linha in vtt.splitlines():
        m = re.match(r"(\d+):(\d+):(\d+)\.(\d+) -->", linha)
        if m:
            h, mi, s, _ = map(int, m.groups())
            bloco_t = h * 3600 + mi * 60 + s
            continue
        if not linha.strip() or linha.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        limpa = re.sub(r"<[^>]+>", "", linha).strip()
        if limpa and limpa not in vistos and bloco_t is not None:
            vistos.add(limpa)
            segs.append({"inicio": bloco_t, "texto": limpa})
    return segs


def legenda_ytdlp(info):
    for campo in ("subtitles", "automatic_captions"):
        faixas = info.get(campo) or {}
        for lingua in LINGUAS:
            for f in faixas.get(lingua, []) or []:
                if f.get("ext") == "vtt" and f.get("url"):
                    with urllib.request.urlopen(f["url"], timeout=60) as r:
                        vtt = r.read().decode("utf-8", "replace")
                    segs = texto_de_vtt(vtt)
                    if segs:
                        return {"metodo": f"yt-dlp {campo}", "lingua": lingua, "segmentos": segs}
    return None


def legenda_api(vid):
    from youtube_transcript_api import YouTubeTranscriptApi
    api = YouTubeTranscriptApi()
    t = api.fetch(vid, languages=LINGUAS)
    segs = [{"inicio": int(s.start), "texto": s.text.strip()} for s in t if s.text.strip()]
    return {"metodo": "youtube-transcript-api", "lingua": t.language_code, "segmentos": segs}


def baixar(vid):
    destino = os.path.join(SAIDA, f"{vid}.json")
    reg = {"id": vid, "url": f"https://www.youtube.com/watch?v={vid}",
           "coleta": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())}
    info = None
    try:
        info = metadados(vid)
        for k in ("title", "channel", "uploader", "upload_date", "duration", "description",
                  "view_count", "chapters"):
            reg[k] = info.get(k)
    except Exception as e:  # noqa: BLE001
        reg["erro_metadados"] = repr(e)[:500]
    leg = None
    erros = []
    if info:
        try:
            leg = legenda_ytdlp(info)
        except Exception as e:  # noqa: BLE001
            erros.append("yt-dlp: " + repr(e)[:300])
    if not leg:
        try:
            leg = legenda_api(vid)
        except Exception as e:  # noqa: BLE001
            erros.append("api: " + repr(e)[:300])
    if leg:
        reg.update(leg)
        reg["texto"] = " ".join(s["texto"] for s in leg["segmentos"])
        reg["palavras"] = len(reg["texto"].split())
    if erros:
        reg["erros_transcricao"] = erros
    os.makedirs(SAIDA, exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, indent=1)
    log(vid, reg.get("title"), "|", reg.get("palavras", 0), "palavras |", "; ".join(erros) or "ok")
    return reg


def buscar(termo, n):
    import yt_dlp
    opts = {"quiet": True, "skip_download": True, "extract_flat": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        res = ydl.extract_info(f"ytsearch{n}:{termo}", download=False)
    itens = [{"id": e.get("id"), "titulo": e.get("title"), "canal": e.get("channel"),
              "duracao": e.get("duration"), "url": e.get("url")} for e in res.get("entries", [])]
    slug = re.sub(r"[^a-z0-9]+", "-", termo.lower()).strip("-")[:60]
    os.makedirs(SAIDA, exist_ok=True)
    with open(os.path.join(SAIDA, f"_busca-{slug}.json"), "w", encoding="utf-8") as f:
        json.dump({"termo": termo, "coleta": time.strftime("%Y-%m-%d"), "itens": itens},
                  f, ensure_ascii=False, indent=1)
    for i in itens:
        log("busca:", i["id"], i["titulo"], "|", i["canal"])
    return itens


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ids", nargs="*", default=[])
    p.add_argument("--busca", action="append", default=[])
    p.add_argument("--max", type=int, default=25)
    p.add_argument("--baixar", type=int, default=0)
    a = p.parse_args()
    ids = [re.sub(r".*(?:v=|youtu\.be/)([\w-]{11}).*", r"\1", x) for x in a.ids]
    for termo in a.busca:
        try:
            itens = buscar(termo, a.max)
            ids += [i["id"] for i in itens[: a.baixar] if i.get("id")]
        except Exception as e:  # noqa: BLE001
            log("falha na busca", termo, repr(e)[:300])
    vistos = []
    for vid in ids:
        if vid in vistos:
            continue
        vistos.append(vid)
        baixar(vid)
        time.sleep(2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
