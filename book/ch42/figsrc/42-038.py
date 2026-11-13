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


fig, ax = canvas(52)
box(ax, 4, 34, 80, 16, "sujet"); text(ax, 11, 42, "S", "sujet", "l", weight="bold")
for x, l in zip([30, 44, 58], "abc"): disc(ax, x, 42, 3.4, "sujet", label=l)
box(ax, 4, 4, 80, 16, "sujet"); text(ax, 11, 12, "S", "sujet", "l", weight="bold")
for x, l in zip([30, 44, 58], "abc"): disc(ax, x, 12, 3.4, "sujet", label=l)
for x in (30, 44, 58): arrow(ax, (x, 21), (x, 33), "resultat")
text(ax, 71, 27, r"$S\subseteq S$", "resultat", "xl", weight="bold")
save(fig, "42-038")

