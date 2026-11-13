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


fig, ax = canvas(55)
box(ax, 4, 35, 28, 14, "sujet", label=r"$a\in A$", size="l")
box(ax, 56, 35, 28, 14, "resultat", label=r"$a\in S$", size="l")
arrow(ax, (33, 42), (55, 42), "varie", lw=2.0)
text(ax, 44, 46.5, r"$\Rightarrow$", "varie", "l")
text(ax, 18, 30, "condition", "sujet", "s"); text(ax, 70, 30, "ce qui s’ensuit", "resultat", "s")
box(ax, 4, 3, 28, 14, "limite", dash=True, label=r"$c\in A$", size="l")
text(ax, 18, 20.5, "faux", "limite", "s")
arrow(ax, (33, 10), (55, 10), "fixe", lw=1.2)
box(ax, 56, 3, 28, 14, "fixe", dash=True, label="rien n’est dit", size="s")
save(fig, "42-037")

