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

fig, ax = canvas(82)
box(ax, 4, 58, 16, 16, "sujet", label=r"$\mathcal{P}$", size="xl")
text(ax, 33, 66, "(", "encre", "xl"); text(ax, 51, 66, ")", "encre", "xl")
box(ax, 38, 58, 8, 16, "fixe", label=r"$S$", size="l")
text(ax, 12, 52, "tous les", "sujet", "s"); text(ax, 12, 48, "sous-ensembles", "sujet", "s")
text(ax, 42, 52, "les 3 objets", "fixe", "s"); text(ax, 42, 48, "a, b, c", "fixe", "s")
text(ax, 72, 66, r"$=\ 8$ sacs", "encre", "m")
grid8(ax, 8.5, 6, 16.5, 11, 3, "sujet")
text(ax, 44, 38.5, r"$\mathcal{P}(\{a,b,c\})$", "sujet", "m")
save(fig, "42-047")
