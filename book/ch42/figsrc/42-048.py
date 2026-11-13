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

fig, ax = canvas(80)
disc(ax, 14, 70, 3.6, "sujet", label="a")
text(ax, 14, 62, "objet", "sujet", "s")
mini(ax, 27, 66, 18, 10, (1, 0, 0), "varie")
text(ax, 54, 71, "sac {a}", "varie", "s")
box(ax, 4, 4, 80, 38, "fixe", fill=False)
text(ax, 18, 37, r"$\mathcal{P}(S)$", "fixe", "l")
pos = grid8(ax, 8.5, 6, 16.5, 11, 3, "sujet", special=1, srole="varie")
arrow(ax, (14, 56), (14, 44.5), "limite", lw=1.3)
text(ax, 20, 50, "∉", "limite", "l")
arrow(ax, (36, 64.5), (36, 32.5), "resultat", lw=1.3)
text(ax, 42, 50, "∈", "resultat", "l")
save(fig, "42-048")

