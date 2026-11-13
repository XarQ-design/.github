# Draws the XarQ-design organization profile art: banner.png and avatar.png.
# Usage: python3 gen.py <out-dir>   (needs Inkscape and the Montserrat font)
import os, subprocess, sys

OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
SRC = os.path.join(OUT, "src"); os.makedirs(SRC, exist_ok=True)

# The XarQ logomark (src/assets/logo/xarq-mark.svg), 100x100 frame.
MARK = ('<path d="M72 28 L28 72" stroke="#8B6BFF" stroke-width="15" stroke-linecap="round"/>'
        '<path d="M28 28 L84 84" stroke="#4C86FF" stroke-width="15" stroke-linecap="round"/>'
        '<rect x="66.7" y="22.7" width="10.6" height="10.6" rx="2.2" fill="#0C0D10" stroke="#8B6BFF" stroke-width="3.4"/>')
FONT = "font-family:Montserrat;"

def render(name, svg, width):
    p = os.path.join(SRC, name + ".svg"); open(p, "w").write(svg)
    subprocess.run(["inkscape", p, "--export-type=png",
                    f"--export-filename={os.path.join(OUT, name + '.png')}",
                    f"--export-width={width}"], check=True, capture_output=True)

def node(x, y, hx1, hy1, hx2, hy2):
    # An anchor point with its two Bézier handles, as the Node tool draws them.
    return (f'<line x1="{hx1}" y1="{hy1}" x2="{hx2}" y2="{hy2}" stroke="#4C86FF" stroke-width="1.2" opacity="0.55"/>'
            f'<circle cx="{hx1}" cy="{hy1}" r="3.2" fill="#0f151b" stroke="#4C86FF" stroke-width="1.2" opacity="0.7"/>'
            f'<circle cx="{hx2}" cy="{hy2}" r="3.2" fill="#0f151b" stroke="#4C86FF" stroke-width="1.2" opacity="0.7"/>'
            f'<rect x="{x-4}" y="{y-4}" width="8" height="8" fill="#4C86FF" opacity="0.9"/>')

# 1. banner ---------------------------------------------------------------
W, H = 880, 300
curve = "M 600 300 C 640 260, 680 250, 720 262 C 760 274, 770 240, 800 200 S 860 80, 900 50"
banner = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<radialGradient id="bg" cx="{0.22*W}" cy="{0.45*H}" r="{0.8*W}" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#2a3846"/><stop offset="0.55" stop-color="#151d25"/><stop offset="1" stop-color="#07090b"/></radialGradient>
<radialGradient id="glow" cx="160" cy="150" r="150" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#2D6FF7" stop-opacity="0.35"/><stop offset="1" stop-color="#2D6FF7" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="22" height="22" patternUnits="userSpaceOnUse">
<path d="M 22 0 L 0 0 0 22" fill="none" stroke="#a9bfd2" stroke-width="0.6" opacity="0.07"/></pattern>
<linearGradient id="fr" x1="0" x2="1"><stop offset="0.6" stop-color="#fff" stop-opacity="0"/><stop offset="0.85" stop-color="#fff"/></linearGradient>
<mask id="fadeR"><rect width="{W}" height="{H}" fill="url(#fr)"/></mask>
<clipPath id="card"><rect width="{W}" height="{H}" rx="22"/></clipPath>
</defs>
<g clip-path="url(#card)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<g mask="url(#fadeR)">
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<path d="{curve}" fill="none" stroke="#cfe3ff" stroke-width="2.2" opacity="0.55"/>
{node(720, 262, 680, 250, 760, 274)}
{node(800, 200, 770, 240, 830, 160)}
<rect x="730" y="28" width="120" height="86" fill="none" stroke="#4C86FF" stroke-width="1" stroke-dasharray="4 3" opacity="0.5"/>
<circle cx="790" cy="71" r="28" fill="#8B6BFF" opacity="0.18"/>
</g>
<rect width="{W}" height="{H}" fill="url(#glow)"/>
<g transform="translate(95 85) scale(1.3)">{MARK}</g>
<text x="270" y="130" fill="#e6eef5" style="{FONT}font-weight:300;font-size:58px;letter-spacing:18px">XARQ</text>
<text x="272" y="170" fill="#a9bfd2" style="{FONT}font-weight:400;font-size:17px">Draw, retouch, lay out and publish, in one studio.</text>
<text x="272" y="200" fill="#6a7483" style="{FONT}font-weight:500;font-size:12px;letter-spacing:3px">LINUX · WINDOWS · MACOS · HAIKU</text>
</g></svg>'''
render("banner", banner, W * 2)

# 2. avatar (the org picture; GitHub crops it to a circle in some places) --
avatar = f'''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="500" viewBox="0 0 500 500">
<defs><radialGradient id="g" cx="250" cy="220" r="300" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#2a3846"/><stop offset="1" stop-color="#0C0D10"/></radialGradient></defs>
<rect width="500" height="500" fill="url(#g)"/>
<g transform="translate(110 110) scale(2.8)">{MARK}</g>
</svg>'''
render("avatar", avatar, 500)
