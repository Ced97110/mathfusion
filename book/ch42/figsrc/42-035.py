import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mini(ax, x, y, w, h, present, role="sujet", fill_role=None):
    box(ax, x, y, w, h, role, lw=0.7, r=0.6)
    r = min(h * 0.26, w * 0.1)
    for i, p in enumerate(present):
        cx = x + w * (0.2 + 0.3 * i)
        if p: disc(ax, cx, y + h / 2, r, fill_role or role, lw=0.6)
        else: ax.add_patch(Circle((cx, y + h / 2), r, ec=COL["fixe"], fc="none", lw=0.5, ls="--", zorder=2))
SUBS = [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
def grid8(ax, x0, y0, cw, ch, gap, role="sujet", full_role=None, hl=None):
    pos = []
    for k, s in enumerate(SUBS):
        c, rr = k % 4, 1 - k // 4
        x = x0 + c * (cw + gap); y = y0 + rr * (ch + gap)
        mini(ax, x, y, cw, ch, s, full_role if (full_role and k == 7) else (("limite" if hl == k else role)) if False else (full_role if (full_role and k == 7) else role))
        pos.append((x, y))
    return pos


fig, ax = canvas(80)
box(ax, 4, 56, 80, 18, "fixe"); text(ax, 11, 65, "S", "fixe", "l", weight="bold")
for x, l in zip([24, 34, 44], "abc"): disc(ax, x, 65, 3.6, "fixe", label=l)
box(ax, 4, 22, 38, 18, "sujet"); text(ax, 11, 31, "A", "sujet", "l", weight="bold")
for x, l in zip([24, 34], "ab"): disc(ax, x, 31, 3.6, "sujet", label=l)
box(ax, 46, 22, 38, 18, "autre"); text(ax, 53, 31, "B", "autre", "l", weight="bold")
disc(ax, 64, 31, 3.6, "autre", label="a"); disc(ax, 76, 31, 3.6, "limite", label="t")
arrow(ax, (24, 41), (24, 54), "resultat"); arrow(ax, (34, 41), (34, 54), "resultat")
arrow(ax, (76, 41), (76, 53), "limite")
text(ax, 76, 49.5, "×", "limite", "m", weight="bold")
text(ax, 23, 14, "A : sous-ensemble de S", "resultat", "s"); text(ax, 23, 9, "tous ses objets sont dans S", "resultat", "s")
text(ax, 65, 14, "B : pas un sous-ensemble", "limite", "s"); text(ax, 65, 9, "t n’est pas dans S", "limite", "s")
save(fig, "42-035")

