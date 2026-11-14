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

fig, ax = canvas(64)
box(ax, 3, 42, 28, 16, "sujet", label=r"$A=B$", size="l")
arrow(ax, (33, 50), (55, 50), "varie", both=True, lw=1.6)
text(ax, 44, 55, "si et seulement si", "varie", "s")
box(ax, 57, 42, 28, 16, "autre", label="A ⊆ B\net B ⊆ A", size="s")
text(ax, 44, 33, r"$A=\{2,\,4\}$ et $B=\{2,\,4,\,6\}$", "encre", "s")
box(ax, 3, 6, 28, 16, "limite", label="A = B\nfaux", size="m")
box(ax, 45, 6, 18, 16, "resultat", label="A ⊆ B\nvrai", size="s")
box(ax, 66, 6, 18, 16, "limite", label="B ⊆ A\nfaux", size="s")
text(ax, 38, 14, "⇔", "varie", "l")
save(fig, "42-044")

