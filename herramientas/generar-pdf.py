# Genera entregable/copiloto-salud360.pdf desde entregable/copiloto-salud360.md
#
# Pasos:
#   1. Extrae el bloque Mermaid y lo renderiza a SVG con un navegador headless
#      (Edge o Chrome) cargando mermaid.js desde jsDelivr. El SVG se guarda en
#      entregable/build/ y se reutiliza mientras el diagrama no cambie.
#   2. Convierte el Markdown a HTML (paquete markdown de Python) e incrusta el SVG.
#   3. Imprime el HTML a PDF con el mismo navegador.
#   4. Verifica el PDF: paginas, pagina donde termina D7, fuentes, texto.
#
# Uso:  python herramientas/generar-pdf.py [--forzar-diagrama] [--solo-verificar]
# Requisitos: Python 3 con el paquete markdown, Edge o Chrome, red para el
# primer render del diagrama. pdftotext es opcional (mejora la verificacion).

import hashlib
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parent.parent
MD = RAIZ / "entregable" / "copiloto-salud360.md"
BUILD = RAIZ / "entregable" / "build"
PDF = RAIZ / "entregable" / "copiloto-salud360.pdf"
HTML_FINAL = BUILD / "copiloto-salud360.html"
SVG = BUILD / "diagrama-d2.svg"
SVG_HASH = BUILD / "diagrama-d2.sha256"
MERMAID_CDN = "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js"
FUENTE = "'Segoe UI', Arial, sans-serif"

# Ajustes de render del diagrama (no cambian nodos, flechas ni textos).
# DIAGRAMA_DIRECCION fuerza una direccion distinta a la del .md; None usa la del .md.
DIAGRAMA_DIRECCION = None
DIAGRAMA_FLOWCHART = "{htmlLabels:false, useMaxWidth:true, curve:'basis', nodeSpacing:8, rankSpacing:18, padding:6, subGraphTitleMargin:{top:30, bottom:50}}"
DIAGRAMA_LETRA = "28px"
DIAGRAMA_ALTO_MAX_CM = 17
ANCHO_UTIL_CM = 21.0 - 2 * 2.0  # A4 menos margenes de 2 cm

NAVEGADORES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

CSS = """
@page { size: A4; margin: 2cm; }
html { font-family: %(fuente)s; font-size: 10pt; color: #111; background: #fff; }
body { margin: 0; line-height: 1.35; }
* {
  font-variant-ligatures: none;
  font-feature-settings: "liga" 0, "clig" 0, "dlig" 0, "hlig" 0;
  hyphens: none; -webkit-hyphens: none;
}
h1 { font-size: 16pt; margin: 0 0 4pt 0; }
h2 { font-size: 12.5pt; margin: 12pt 0 4pt 0; border-bottom: 0.75pt solid #999; padding-bottom: 2pt; break-after: avoid; }
h1 + p, h1 + p + p { margin: 2pt 0; }
p { margin: 4pt 0; }
ul, ol { margin: 3pt 0; padding-left: 16pt; }
li { margin: 1pt 0; }
table { width: 100%%; border-collapse: collapse; margin: 5pt 0; table-layout: auto; break-inside: auto; }
th, td { border: 0.5pt solid #888; padding: 2pt 4pt; vertical-align: top; text-align: left; overflow-wrap: break-word; }
th { background: #eee; }
tr { break-inside: avoid; }
.diagrama { margin: 6pt 0; break-inside: avoid; text-align: center; }
.diagrama svg { width: 100%%; height: auto; max-height: %(alto)scm; }
.nueva-pagina { break-before: page; }
.nw { white-space: nowrap; }
""" % {"fuente": FUENTE, "alto": DIAGRAMA_ALTO_MAX_CM}


def buscar_navegador():
    for ruta in NAVEGADORES:
        if os.path.isfile(ruta):
            return ruta
    sys.exit("No se encontro Edge ni Chrome en las rutas habituales.")


def ejecutar_navegador(navegador, args, timeout=120):
    perfil = tempfile.mkdtemp(prefix="perfil-pdf-")
    try:
        cmd = [navegador, "--headless=new", "--disable-gpu", "--no-first-run",
               "--disable-extensions", "--user-data-dir=" + perfil] + args
        r = subprocess.run(cmd, capture_output=True, timeout=timeout)
        return r.stdout.decode("utf-8", errors="replace")
    finally:
        shutil.rmtree(perfil, ignore_errors=True)


def extraer_mermaid(texto):
    m = re.search(r"```mermaid\n(.*?)\n```", texto, re.S)
    if not m:
        sys.exit("No se encontro el bloque mermaid en el Markdown.")
    return m


def renderizar_diagrama(navegador, codigo, forzar):
    if DIAGRAMA_DIRECCION:
        codigo = re.sub(r"^flowchart \w+", "flowchart " + DIAGRAMA_DIRECCION,
                        codigo, count=1)
    huella = hashlib.sha256((codigo + DIAGRAMA_FLOWCHART + DIAGRAMA_LETRA
                             + MERMAID_CDN).encode("utf-8")).hexdigest()
    if (not forzar and SVG.exists() and SVG_HASH.exists()
            and SVG_HASH.read_text(encoding="utf-8").strip() == huella):
        print("Diagrama sin cambios: se reutiliza", SVG.name)
        return SVG.read_text(encoding="utf-8")

    pagina = """<!doctype html><html><head><meta charset="utf-8">
<style>body{font-family:%(fuente)s}</style>
<script src="%(cdn)s"></script></head><body>
<pre id="src" style="display:none">%(codigo)s</pre><div id="out"></div>
<script>
mermaid.initialize({startOnLoad:false, securityLevel:'strict', theme:'base',
  htmlLabels:false, fontFamily:"%(fuente)s",
  flowchart:%(flowchart)s,
  themeVariables:{fontFamily:"%(fuente)s", fontSize:'%(letra)s'}});
mermaid.render('d2svg', document.getElementById('src').textContent)
  .then(function(r){ document.getElementById('out').innerHTML = r.svg; })
  .catch(function(e){ document.getElementById('out').textContent = 'ERROR_MERMAID ' + e; });
</script></body></html>""" % {"fuente": FUENTE, "cdn": MERMAID_CDN, "flowchart": DIAGRAMA_FLOWCHART,
                              "letra": DIAGRAMA_LETRA,
                              "codigo": html.escape(codigo)}
    tmp = BUILD / "render-diagrama.html"
    tmp.write_text(pagina, encoding="utf-8")
    dom = ejecutar_navegador(navegador, ["--virtual-time-budget=20000",
                                         "--dump-dom", tmp.as_uri()])
    fallo = re.search(r'<div id="out">ERROR_MERMAID(.*?)</div>', dom, re.S)
    if fallo:
        sys.exit("Mermaid fallo: " + fallo.group(1)[:300])
    m = re.search(r'<svg[^>]*id="d2svg".*</svg>', dom, re.S)
    if not m:
        sys.exit("No se obtuvo el SVG (revisar acceso a %s)." % MERMAID_CDN)
    svg = m.group(0)
    SVG.write_text(svg, encoding="utf-8")
    SVG_HASH.write_text(huella, encoding="utf-8")
    print("Diagrama renderizado:", SVG.name)
    return svg


ES_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")


def separar_listas(texto):
    # Python-Markdown necesita una linea en blanco antes de una lista (GitHub
    # no). Se agrega solo en memoria; el archivo .md no se toca.
    salida, previa = [], ""
    for linea in texto.split("\n"):
        if ES_ITEM.match(linea) and previa.strip() and not ES_ITEM.match(previa):
            salida.append("")
        salida.append(linea)
        previa = linea
    return "\n".join(salida)


def sin_salto_en_guion(cuerpo):
    # Evita que el navegador parta una linea en el guion de una palabra
    # compuesta (por ejemplo "semanas-ingeniero"): el guion queda visible y
    # el texto extraido conserva la palabra completa.
    def en_texto(m):
        return re.sub(r"(?<![\w<])(\w+(?:-\w+)+)(?![\w>])",
                      r'<span class="nw">\1</span>', m.group(0))
    return re.sub(r">[^<]+<", en_texto, cuerpo)


def construir_html(texto, svg):
    m = extraer_mermaid(texto)
    marca = "MARCA_DIAGRAMA_D2"
    texto = texto[:m.start()] + marca + texto[m.end():]
    cuerpo = markdown.markdown(separar_listas(texto),
                               extensions=["tables", "sane_lists"],
                               output_format="html")
    cuerpo = sin_salto_en_guion(cuerpo)
    cuerpo = cuerpo.replace("<p>%s</p>" % marca,
                            '<div class="diagrama">%s</div>' % svg)
    cuerpo = re.sub(r"<h2>D8\.", '<h2 class="nueva-pagina">D8.', cuerpo, count=1)
    titulo = re.search(r"<h1>(.*?)</h1>", cuerpo).group(1)
    doc = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>%s</title>
<style>%s</style></head><body>
%s
</body></html>
""" % (re.sub("<[^>]+>", "", titulo), CSS, cuerpo)
    HTML_FINAL.write_text(doc, encoding="utf-8")
    return doc


def imprimir_pdf(navegador):
    if PDF.exists():
        PDF.unlink()
    ejecutar_navegador(navegador, ["--no-pdf-header-footer",
                                   "--print-to-pdf-no-header",
                                   "--print-to-pdf=" + str(PDF),
                                   HTML_FINAL.as_uri()])
    if not PDF.exists():
        sys.exit("El navegador no genero el PDF.")
    print("PDF generado:", PDF)


# ---------- Verificacion ----------

def objetos_pdf(datos):
    objs = {}
    for m in re.finditer(rb"(\d+) 0 obj(.*?)endobj", datos, re.S):
        objs[int(m.group(1))] = m.group(2)
    # Objetos dentro de object streams, si los hay
    for cuerpo in list(objs.values()):
        if b"/ObjStm" in cuerpo:
            s = re.search(rb"stream\r?\n(.*)endstream", cuerpo, re.S)
            try:
                plano = zlib.decompress(s.group(1))
            except Exception:
                continue
            n = int(re.search(rb"/N (\d+)", cuerpo).group(1))
            first = int(re.search(rb"/First (\d+)", cuerpo).group(1))
            nums = list(map(int, plano[:first].split()))
            for i in range(n):
                num, off = nums[2 * i], nums[2 * i + 1]
                fin = nums[2 * i + 3] if i + 1 < n else len(plano) - first
                objs[num] = plano[first + off:first + fin]
    return objs


def informe_fuentes(datos):
    objs = objetos_pdf(datos)
    descriptores = {}
    for cuerpo in objs.values():
        if b"/FontDescriptor" in cuerpo and b"/FontName" in cuerpo:
            nombre = re.search(rb"/FontName\s*/([^\s/>\]]+)", cuerpo).group(1)
            descriptores[nombre] = bool(re.search(rb"/FontFile[23]?\b", cuerpo))
    filas = []
    for cuerpo in objs.values():
        if re.search(rb"/Type\s*/Font\b", cuerpo) and b"/Subtype" in cuerpo:
            sub = re.search(rb"/Subtype\s*/(\w+)", cuerpo).group(1).decode()
            if sub.startswith("CIDFontType"):
                continue
            bf = re.search(rb"/BaseFont\s*/([^\s/>\]]+)", cuerpo)
            nombre = bf.group(1) if bf else b"(sin nombre)"
            emb = descriptores.get(nombre)
            if sub == "Type0":
                desc = re.search(rb"/DescendantFonts\s*\[\s*(\d+) 0 R", cuerpo)
                if desc:
                    d = objs.get(int(desc.group(1)), b"")
                    sub = "Type0/" + re.search(rb"/Subtype\s*/(\w+)", d).group(1).decode()
            filas.append((nombre.decode(), sub, emb, b"/ToUnicode" in cuerpo))
    return filas


def texto_pdf():
    if not shutil.which("pdftotext"):
        return None
    r = subprocess.run(["pdftotext", "-enc", "UTF-8", str(PDF), "-"],
                       capture_output=True)
    return r.stdout.decode("utf-8", errors="replace")


def plano(s):
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def letra_efectiva_diagrama():
    # Escala con que se dibuja el SVG: ocupa el ancho util salvo que el alto
    # maximo lo limite. 1 cm = 72 / 2,54 pt; 1 px de CSS = 0,75 pt.
    svg = SVG.read_text(encoding="utf-8")
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1).split()
    w, h = float(vb[2]), float(vb[3])
    pt_cm = 72 / 2.54
    escala = min(ANCHO_UTIL_CM * pt_cm / w, DIAGRAMA_ALTO_MAX_CM * pt_cm / h)
    letra_pt = float(DIAGRAMA_LETRA.replace("px", "")) * escala
    return w, h, escala, letra_pt


def verificar(doc_html):
    w, h, escala, letra = letra_efectiva_diagrama()
    print("\nDiagrama: viewBox %.0f x %.0f px; dibujado a %.1f x %.1f cm; "
          "letra efectiva %.1f pt" % (w, h, w * escala * 2.54 / 72,
                                     h * escala * 2.54 / 72, letra))
    datos = PDF.read_bytes()
    paginas = len(re.findall(rb"/Type\s*/Page\b", datos))
    caja = re.search(rb"/MediaBox\s*\[\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)", datos)
    print("\n== Verificacion ==")
    print("Paginas totales:", paginas)
    if caja:
        w, h = float(caja.group(3)), float(caja.group(4))
        print("Tamano de pagina: %.0f x %.0f pt (A4 = 595 x 842)" % (w, h))

    print("\nFuentes (nombre, tipo, embebida, ToUnicode):")
    filas = informe_fuentes(datos)
    for f in filas:
        print("  %s | %s | %s | %s" % (f[0], f[1],
              "si" if f[2] else ("no" if f[2] is False else "?"),
              "si" if f[3] else "no"))
    print("Fuentes Type 3:", sum(1 for f in filas if "Type3" in f[1]))

    texto = texto_pdf()
    if texto is None:
        print("pdftotext no disponible: se omite la verificacion de texto.")
        return
    hojas = texto.split("\f")
    d8 = next((i + 1 for i, h in enumerate(hojas) if "D8. Apéndice" in h), None)
    d7 = next((i + 1 for i, h in enumerate(hojas) if "D7. Lo que el brief" in h), None)
    print("\nD7 empieza en la pagina", d7, "; D8 empieza en la pagina", d8,
          "; D1 a D7 ocupan", (d8 - 1) if d8 else "?", "paginas")

    lig = [c for c in "\ufb00\ufb01\ufb02\ufb03\ufb04\ufb05\ufb06" if c in texto]
    invis = [hex(ord(c)) for c in "\u00ad\u200b\u200c\u200d\u2060\ufeff" if c in texto]
    print("Ligaduras en el texto extraido:", lig or "ninguna")
    print("Caracteres invisibles:", invis or "ninguno")
    cortes = [l for l in texto.splitlines() if re.search(r"[a-záéíóúñ]-$", l)]
    print("Lineas que terminan en letra seguida de guion:", len(cortes))
    for l in cortes[:10]:
        print("   ", l)

    pdf_plano = re.sub(r"\s+", " ", texto)
    bloques = [plano(b) for b in re.findall(r"<(?:p|li)>(.*?)</(?:p|li)>", doc_html, re.S)]
    bloques = [b for b in bloques if b and "MARCA_" not in b]
    faltan = [b for b in bloques if b not in pdf_plano]
    print("Parrafos y vinetas del Markdown encontrados literalmente en el PDF: %d de %d"
          % (len(bloques) - len(faltan), len(bloques)))
    for b in faltan[:10]:
        print("   NO:", b[:120])

    etiquetas = ["Orquestador", "máquina de estados", "Reglas de alarma",
                 "Validador:", "Menú con botones", "Agendamiento",
                 "Catálogo clínico", "Revisión", "Fuera de línea", "Flujo del"]
    pag_diag = next((i + 1 for i, h in enumerate(hojas) if "Orquestador" in h), None)
    print("Texto del diagrama extraible:",
          {e: (e in texto) for e in etiquetas}, "en la pagina", pag_diag)


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    texto = MD.read_text(encoding="utf-8").replace("\r\n", "\n")
    if "--solo-verificar" not in sys.argv:
        navegador = buscar_navegador()
        print("Navegador:", navegador)
        codigo = extraer_mermaid(texto).group(1)
        svg = renderizar_diagrama(navegador, codigo, "--forzar-diagrama" in sys.argv)
        doc = construir_html(texto, svg)
        imprimir_pdf(navegador)
    else:
        doc = HTML_FINAL.read_text(encoding="utf-8")
    verificar(doc)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
