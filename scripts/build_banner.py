"""Build self-contained banner SVGs. Requires fonttools==4.60.2."""
from pathlib import Path
from html import escape
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen

ROOT = Path(__file__).resolve().parents[1]
FONT = ROOT / 'assets/fonts/SpaceGrotesk[wght].ttf'


def lettering(text, x, y, size, color, weight=500, tracking=0):
    font = instantiateVariableFont(TTFont(FONT), {'wght': weight}, inplace=True)
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale = size / font['head'].unitsPerEm
    position, paths = 0, []
    for char in text:
        glyph = glyphs[cmap[ord(char)]]
        pen = SVGPathPen(glyphs)
        glyph.draw(pen)
        paths.append(f'<path transform="translate({position:.3f} 0)" d="{pen.getCommands()}"/>')
        position += glyph.width + tracking / scale
    return f'<g aria-label="{escape(text)}" fill="{color}" transform="translate({x} {y}) scale({scale} {-scale})">' + ''.join(paths) + '</g>'


def build(theme):
    dark = theme == 'dark'
    bg, fg = ('#111720', '#f1f5fc') if dark else ('#f2f5fa', '#152034')
    muted = '#a8b8cf' if dark else '#4c607b'
    accent = '#79aaff' if dark else '#235bd7'
    grid = '#253247' if dark else '#d9e2f0'
    panel = '#172333' if dark else '#e6edf8'
    content = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="400" viewBox="0 0 1280 400" role="img" aria-labelledby="title desc">
<title id="title">Matteo Mottinelli — @Mottyppo</title>
<desc id="desc">Software development. Original geometric MM monogram in blue, with Space Grotesk lettering.</desc>
<rect width="1280" height="400" rx="16" fill="{bg}"/>
<path d="M880 0H1280V400H748Z" fill="{panel}"/>
<g fill="none" stroke="{grid}" stroke-width="1">''']
    for x in range(856, 1240, 48):
        content.append(f'<path d="M{x} 48V352"/>')
    for y in range(64, 353, 48):
        content.append(f'<path d="M824 {y}H1232"/>')
    content.append('</g>')
    content.append(f'<path d="M64 55H92" stroke="{accent}" stroke-width="4"/>')
    content.append(lettering('SOFTWARE DEVELOPMENT', 109, 62, 20, muted, 500, 2))
    content.append(lettering('Matteo', 60, 174, 100, fg, 600, -2))
    content.append(lettering('Mottinelli', 60, 270, 100, fg, 600, -2))
    content.append(lettering('@Mottyppo', 66, 341, 27, accent, 500))
    # Two interlocking angular M shapes form an original architectural monogram.
    content.append(f'''<path d="M854 286V104H894L948 184L1002 104H1042V286H998V182L948 254L898 182V286Z" fill="{accent}"/>
<path d="M998 298V116H1038L1092 196L1146 116H1186V298H1142V194L1092 266L1042 194V298Z" fill="{bg}" stroke="{accent}" stroke-width="3"/>
<path d="M824 328H872M1184 72H1232" stroke="{accent}" stroke-width="2"/>
</svg>''')
    (ROOT / f'assets/banner-{theme}.svg').write_text('\n'.join(content))

for theme in ('light', 'dark'):
    build(theme)
