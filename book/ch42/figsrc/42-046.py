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

fig, ax = canvas(76)
box(ax, 4, 56, 44, 16, "fixe"); text(ax, 10, 64, "S", "fixe", "l", weight="bold")
for x, l in zip([24, 33, 42], "abc"): disc(ax, x, 64, 3.0, "fixe", label=l, size="s")
text(ax, 68, 67, "3 éléments", "fixe", "m", weight="bold"); text(ax, 68, 61, "des objets", "fixe", "s")
box(ax, 4, 4, 80, 44, "sujet", fill=False, dash=True)
text(ax, 18, 42, r"$\mathcal{P}(S)$", "sujet", "l")
text(ax, 62, 42, "8 éléments : des sacs", "sujet", "s")
pos = grid8(ax, 8.5, 8, 16.5, 11, 3, "sujet", special=1, srole="varie")
text(ax, 36, 36.5, "un sac = un élément", "varie", "s")
save(fig, "42-046")

