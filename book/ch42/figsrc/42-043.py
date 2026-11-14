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

fig, ax = canvas(70)
box(ax, 4, 50, 80, 16, "sujet"); text(ax, 11, 58, "A", "sujet", "l", weight="bold")
box(ax, 4, 4, 80, 16, "autre"); text(ax, 11, 12, "B", "autre", "l", weight="bold")
for x, l in zip([34, 48, 62], "246"):
    disc(ax, x, 58, 3.4, "sujet", label=l); disc(ax, x, 12, 3.4, "autre", label=l)
arrow(ax, (24, 49), (24, 21), "varie", lw=1.4)
text(ax, 17, 35, r"$A\subseteq B$", "varie", "s", ha="center")
arrow(ax, (72, 21), (72, 49), "varie", lw=1.4)
text(ax, 79, 35, r"$B\subseteq A$", "varie", "s", ha="center")
box(ax, 30, 28, 28, 14, "resultat", label=r"$A=B$", size="l")
save(fig, "42-043")

