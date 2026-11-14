import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mini(ax, x, y, w, h, present, role="sujet"):
    box(ax, x, y, w, h, role, lw=0.7, r=0.6)
    r = min(h * 0.26, w * 0.1)
    for i, p in enumerate(present):
        cx = x + w * (0.2 + 0.3 * i)
        if p: disc(ax, cx, y + h / 2, r, role, lw=0.6)
        else: ax.add_patch(Circle((cx, y + h / 2), r, ec=COL["fixe"], fc="none", lw=0.5, ls="--", zorder=2))
SUBS = [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
def grid8(ax, x0, y0, cw, ch, gap, role="sujet", special=None, srole="fixe"):
    pos = []
    for k, s in enumerate(SUBS):
        x = x0 + (k % 4) * (cw + gap); y = y0 + (1 - k // 4) * (ch + gap)
        mini(ax, x, y, cw, ch, s, srole if k == special else role); pos.append((x, y))
    return pos


fig, ax = canvas(50)
pos = grid8(ax, 6, 10, 17, 13, 2.6, "sujet", special=7, srole="fixe")
text(ax, 44, 45, "7 stricts (en bleu)", "sujet", "m", weight="bold")
text(ax, 44, 40.5, "sur 8 sous-ensembles de B", "fixe", "s")
x7, y7 = pos[7]
text(ax, x7 + 8.5, y7 - 3.6, "égal à B : écarté", "fixe", "s")
save(fig, "42-041")
