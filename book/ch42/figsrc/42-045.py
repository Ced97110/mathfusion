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

fig, ax = canvas(72)
xs = [20, 36, 52, 68]
box(ax, 4, 44, 80, 14, "sujet"); text(ax, 11, 51, "A", "sujet", "l", weight="bold")
box(ax, 4, 16, 80, 14, "autre"); text(ax, 11, 23, "B", "autre", "l", weight="bold")
for x, l in zip(xs, ["5", "10", "15", "20"]):
    disc(ax, x, 51, 3.6, "sujet", label=l, size="s"); disc(ax, x, 23, 3.6, "autre", label=l, size="s")
    arrow(ax, (x - 1.5, 43), (x - 1.5, 31), "resultat"); arrow(ax, (x + 1.5, 31), (x + 1.5, 43), "varie")
text(ax, 44, 65, "A : multiples de 5 de 1 à 20", "sujet", "s")
text(ax, 44, 11, "↓ chaque A est dans B : oui", "resultat", "s")
text(ax, 44, 6.8, "↑ chaque B est dans A : oui", "varie", "s")
text(ax, 44, 2.6, "deux oui : A = B", "encre", "s", weight="bold")
save(fig, "42-045")

