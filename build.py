#!/usr/bin/env python3
"""Write index.html: the 1024x1024 poster for 19 November 2026.

Everything here is shapes and system fonts. No images, no webfonts, no network.
Icons are hand-written SVG on a 0..100 grid, one flat accent colour per card.
"""
import math

# ---------------------------------------------------------------- icons


def icon_drone(c):
    """A quadcopter seen from above, beside a radar sweep."""
    return f'''<svg viewBox="0 0 100 100" aria-hidden="true">
<g stroke="{c}" stroke-width="4.5" fill="none" stroke-linecap="round" opacity=".45">
<path d="M10 90 A19 19 0 0 1 29 71"/><path d="M10 90 A34 34 0 0 1 44 56"/></g>
<circle cx="10" cy="90" r="4.5" fill="{c}"/>
<g transform="translate(64,36) rotate(40)">
<g stroke="{c}" stroke-width="5" stroke-linecap="round">
<path d="M-21 -13 L21 13"/><path d="M-21 13 L21 -13"/></g>
<g fill="none" stroke="{c}" stroke-width="5.5">
<circle cx="-21" cy="-13" r="9.5"/><circle cx="21" cy="-13" r="9.5"/>
<circle cx="-21" cy="13" r="9.5"/><circle cx="21" cy="13" r="9.5"/></g>
<rect x="-10" y="-8.5" width="20" height="17" rx="8" fill="{c}"/></g></svg>'''


def icon_flags(c):
    """Three flags on three poles: the trilateral table."""
    return f'''<svg viewBox="0 0 100 100" aria-hidden="true">
<g fill="{c}">
<rect x="3" y="6" width="8" height="88" rx="4"/>
<rect x="34" y="6" width="8" height="88" rx="4"/>
<rect x="65" y="6" width="8" height="88" rx="4"/>
<path d="M11 6 h25 l-7 11 7 11 h-25 z"/>
<path d="M42 6 h25 l-7 11 7 11 h-25 z"/>
<path d="M73 6 h25 l-7 11 7 11 h-25 z"/></g></svg>'''


def icon_virus(c):
    """A spiked particle with a few cut-outs."""
    spikes = []
    for i in range(10):
        a = math.radians(i * 36 - 90)
        x1, y1 = 50 + 23 * math.cos(a), 50 + 23 * math.sin(a)
        x2, y2 = 50 + 34 * math.cos(a), 50 + 34 * math.sin(a)
        spikes.append(f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>')
    return f'''<svg viewBox="0 0 100 100" aria-hidden="true">
<g stroke="{c}" stroke-width="7" stroke-linecap="round">{"".join(spikes)}</g>
<circle cx="50" cy="50" r="25" fill="{c}"/>
<circle cx="41" cy="42" r="5" fill="#151A23"/><circle cx="58" cy="56" r="6.5" fill="#151A23"/>
<circle cx="60" cy="38" r="3.5" fill="#151A23"/></svg>'''


def icon_ballot(c):
    """A ballot with a tick going into the box."""
    return f'''<svg viewBox="0 0 100 100" aria-hidden="true">
<rect x="37" y="0" width="26" height="52" rx="2" fill="{c}"/>
<path d="M43 18 L47 23 L58 11" fill="none" stroke="#151A23" stroke-width="4.5"
      stroke-linecap="round" stroke-linejoin="round"/>
<rect x="7" y="44" width="86" height="48" rx="5" fill="#151A23" stroke="{c}" stroke-width="8"/>
<rect x="24" y="54" width="52" height="11" rx="5.5" fill="{c}"/></svg>'''


def icon_chain(c):
    """Two links pulled apart: the chain is broken."""
    return f'''<svg viewBox="0 0 100 100" aria-hidden="true">
<g fill="none" stroke="{c}" stroke-width="11">
<rect x="4" y="40" width="44" height="28" rx="14"/>
<g transform="rotate(-18 74 34)"><rect x="56" y="20" width="40" height="28" rx="14"/></g>
</g>
<g stroke="{c}" stroke-width="5" stroke-linecap="round">
<path d="M52 44 L57 50"/><path d="M52 64 L57 58"/></g></svg>'''


def icon_spacecraft(c):
    """A satellite: body, two panels, a dish. Far from home."""
    return f'''<svg viewBox="0 0 100 100" aria-hidden="true">
<rect x="2" y="40" width="28" height="22" rx="2" fill="{c}" opacity=".8"/>
<rect x="70" y="40" width="28" height="22" rx="2" fill="{c}" opacity=".8"/>
<rect x="36" y="34" width="28" height="34" rx="3" fill="{c}"/>
<path d="M50 32 L50 20" stroke="{c}" stroke-width="7"/>
<path d="M34 20 A16 16 0 0 1 66 20 Z" fill="{c}"/></svg>'''


def icon_cyclone(c):
    """A spiral, tightening to an eye."""
    pts = []
    turns, steps = 2.4, 190
    for i in range(steps + 1):
        t = i / steps
        a = t * turns * 2 * math.pi - math.pi / 2
        r = 5 + 39 * (1 - t)
        pts.append((50 + r * math.cos(a), 50 + r * math.sin(a)))
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    return f'''<svg viewBox="0 0 100 100" aria-hidden="true">
<path d="{d}" fill="none" stroke="{c}" stroke-width="7"
      stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="50" cy="50" r="4.5" fill="{c}"/></svg>'''


# ---------------------------------------------------------------- copy

CARDS = [
    dict(region="MIDDLE EAST", accent="#FF5A5F", lead=True,
         head="IRAN STRIKES US BASE IN KUWAIT",
         detail="Ali Al-Salem base hit in retaliation for Qeshm strike; no US wounded.",
         icon=icon_drone),
    dict(region="DIPLOMACY", accent="#F7D046",
         head="TRUMP, XI, PUTIN MEET IN SHENZHEN",
         detail="Three-way talks due Thursday as the Gulf exchange continued.",
         icon=icon_flags),
    dict(region="AFRICA", accent="#7BD88F",
         head="DRC EBOLA OUTBREAK PASSES SIX MONTHS",
         detail="WHO: over 11,000 infected and more than 5,400 dead; still not controlled.",
         icon=icon_virus),
    dict(region="UNITED STATES", accent="#5AA9FF",
         head="ALASKA FLIPS CONTROL OF THE SENATE",
         detail="Peltola beats Sullivan; Democrats take a 56–44 Senate majority.",
         icon=icon_ballot),
    dict(region="CARIBBEAN", accent="#FF7A45",
         head="HAITI: AT LEAST 4,595 KILLED",
         detail="UN: also 2,050 injured from January to October 2026.",
         icon=icon_chain),
    dict(region="SPACE", accent="#B08CFF",
         head="VOYAGER 1 REACHES ONE LIGHT-DAY",
         detail="NASA: first human-made object to travel that far from Earth.",
         icon=icon_spacecraft),
    dict(region="SOUTH ASIA", accent="#2FD6C0",
         head="CYCLONE AKVAN TO INTENSIFY",
         detail="Forecast to strengthen as it approaches the coast.",
         icon=icon_cyclone),
]

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:1024px; height:1024px; background:#0B0E13; overflow:hidden; }
body { font-family:'Nimbus Sans','DejaVu Sans',sans-serif; color:#FFFFFF;
       -webkit-font-smoothing:antialiased; }
.page { width:1024px; height:1024px; padding:18px 26px 16px; display:flex;
        flex-direction:column; }
.mast { border-bottom:3px solid #2A3240; padding-bottom:9px; }
.date { font-size:100px; font-weight:700; letter-spacing:-3px; line-height:1;
        white-space:nowrap; }
.sub { margin-top:9px; font-size:19px; font-weight:700; letter-spacing:5.5px;
       color:#A6B5C8; }
.grid { margin-top:13px; flex:1; min-height:0; display:grid;
        grid-template-columns:1fr 1fr; grid-template-rows:150px repeat(3,1fr); gap:11px; }
.card { background:#151A23; border-radius:10px; border-left:7px solid var(--a);
        padding:11px 17px 11px 15px; overflow:hidden; display:flex;
        flex-direction:column; justify-content:center; }
.card.lead { grid-column:1 / -1; background:#1B2331; flex-direction:row;
             align-items:center; gap:18px; padding:14px 26px 14px 20px; }
.lead .icon { flex:0 0 86px; width:86px; height:86px; }
.lead .body { flex:1; min-width:0; }
.icon { width:48px; height:48px; flex:0 0 48px; }
.icon svg { width:100%; height:100%; display:block; }
.tag { font-size:21px; font-weight:700; letter-spacing:3.2px; color:var(--a); }
.head { font-size:33px; font-weight:700; line-height:1.04; letter-spacing:-0.7px;
        margin-top:7px; text-wrap:balance; }
.detail { font-size:18px; line-height:1.2; color:#D3DCE7; margin-top:6px;
          min-height:43px; text-wrap:pretty; }
.lead .tag { font-size:23px; letter-spacing:3.6px; }
.lead .head { font-size:42px; line-height:1.04; margin-top:6px; letter-spacing:-1px; }
.lead .detail { font-size:19px; margin-top:7px; min-height:0; }
"""


def card_html(c, lead=False):
    return (
        f'<div class="card{" lead" if lead else ""}" style="--a:{c["accent"]}">'
        f'<div class="icon">{c["icon"](c["accent"])}</div>'
        f'<div class="body">'
        f'<div class="tag">{c["region"]}</div>'
        f'<div class="head">{c["head"]}</div>'
        f'<div class="detail">{c["detail"]}</div>'
        f'</div></div>'
    )


CHECK = """
(function () {
  var out = [];
  var d = document.getElementById('date');
  var rg = document.createRange(); rg.selectNodeContents(d);
  out.push('DATE_W=' + Math.round(rg.getBoundingClientRect().width) + '/972');
  document.querySelectorAll('.card').forEach(function (c, i) {
    ['tag', 'head', 'detail'].forEach(function (k) {
      var el = c.querySelector('.' + k);
      if (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1)
        out.push('OVERFLOW c' + i + ' ' + k + ' ' + el.scrollWidth + '/' + el.clientWidth +
                 ' x ' + el.scrollHeight + '/' + el.clientHeight);
    });
    if (c.scrollHeight > c.clientHeight + 1)
      out.push('OVERFLOW c' + i + ' box ' + c.scrollHeight + '/' + c.clientHeight);
    var h = c.querySelector('.head').getBoundingClientRect();
    var b = c.getBoundingClientRect();
    out.push('c' + i + ' head_w=' + Math.round(h.width) + ' card_h=' + Math.round(b.height));
  });
  var r = document.createElement('div'); r.id = 'report';
  r.style.cssText = 'position:absolute;left:-9999px;top:0';
  r.textContent = out.join(' | ');
  document.body.appendChild(r);
})();
"""


def main():
    cards = "".join(card_html(c, c.get("lead", False)) for c in CARDS)
    html = (
        '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n'
        "<title>19 November 2026 - world news in one image</title>\n"
        f"<style>{CSS}</style></head>\n<body><div class=\"page\">\n"
        '  <div class="mast">\n'
        '    <div class="date" id="date">19 NOVEMBER 2026</div>\n'
        '    <div class="sub">THURSDAY &#183; WORLD NEWS &#183; ONE DAY</div>\n'
        "  </div>\n"
        f'  <div class="grid">{cards}</div>\n'
        f"</div>\n<script>{CHECK}</script>\n</body></html>\n"
    )
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote index.html", len(html), "bytes")


if __name__ == "__main__":
    main()
