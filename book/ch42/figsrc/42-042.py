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
box(ax, 4, 38, 80, 16, "autre"); text(ax, 11, 46, "B", "autre", "l", weight="bold")
for x, l, r in zip([30, 44, 58], "abc", ["autre", "autre", "varie"]): disc(ax, x, 46, 3.4, r, label=l)
box(ax, 4, 6, 80, 16, "sujet"); text(ax, 11, 14, "A", "sujet", "l", weight="bold")
for x, l in zip([30, 44], "ab"): disc(ax, x, 14, 3.4, "sujet", label=l)
ax.add_patch(Circle((58, 14), 3.4, ec=COL["varie"], fc="none", lw=0.8, ls="--", zorder=2))
for x in (30, 44): arrow(ax, (x, 23), (x, 37), "resultat")
text(ax, 72, 30, "inclus", "resultat", "s")
text(ax, 73, 14, "c manque", "varie", "s")
text(ax, 73, 46, r"$A\subset B$", "encre", "l", weight="bold")
save(fig, "42-042")
