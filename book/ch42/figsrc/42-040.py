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


fig, ax = canvas(58)
box(ax, 4, 38, 24, 16, "sujet", dash=True); text(ax, 16, 46, "∅", "sujet", "xl")
text(ax, 16, 33.5, "0 objet", "sujet", "s")
arrow(ax, (30, 46), (46, 46), "varie", lw=1.5); text(ax, 38, 50.5, "on cherche", "varie", "s")
box(ax, 48, 36, 36, 20, "limite", dash=True)
text(ax, 66, 49, "un objet de ∅", "limite", "s"); text(ax, 66, 43, "absent de S", "limite", "s")
text(ax, 66, 31, "introuvable", "limite", "m", weight="bold")
arrow(ax, (66, 27), (66, 21), "resultat")
box(ax, 4, 4, 80, 16, "resultat")
text(ax, 44, 15, "règle jamais violée", "resultat", "m", weight="bold"); text(ax, 44, 9, "donc vraie", "resultat", "m")
save(fig, "42-040")

