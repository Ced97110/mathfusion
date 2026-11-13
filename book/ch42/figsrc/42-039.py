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


fig, ax = canvas(56)
box(ax, 4, 38, 30, 16, "sujet", dash=True); text(ax, 12, 46, "∅", "sujet", "xl")
text(ax, 25, 46, "0 objet", "sujet", "s")
box(ax, 4, 4, 80, 16, "fixe"); text(ax, 11, 12, "S", "fixe", "l", weight="bold")
for x, l in zip([30, 44, 58], "abc"): disc(ax, x, 12, 3.4, "fixe", label=l)
text(ax, 64, 49, "0 objet à vérifier", "resultat", "s")
text(ax, 64, 42, "0 échec", "resultat", "m", weight="bold")
arrow(ax, (19, 37), (19, 21), "resultat")
text(ax, 44, 29, r"$\varnothing\subseteq S$ est vrai", "resultat", "m", weight="bold")
save(fig, "42-039")

