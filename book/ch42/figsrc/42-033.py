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


fig, ax = canvas(62)
text(ax, 7, 50, "{", "encre", 30, ha="center")
text(ax, 81, 50, "}", "encre", 30, ha="center")
box(ax, 13, 42, 28, 16, "sujet", label=r"$x\in S$", size="l")
line(ax, [(47, 38), (47, 60)], "varie", lw=2.2)
box(ax, 53, 42, 22, 16, "autre", label=r"$x$ pair", size="l")
text(ax, 47, 33, "tels que", "varie", "l", weight="bold")
brace(ax, 13, 41, 40, "sujet", None, depth=1.6)
brace(ax, 53, 75, 40, "autre", None, depth=1.6)
text(ax, 27, 26, "d’où viennent", "sujet", "m"); text(ax, 27, 21, "les objets", "sujet", "m")
text(ax, 64, 26, "la condition", "autre", "m"); text(ax, 64, 21, "à vérifier", "autre", "m")
text(ax, 44, 8, "La barre sépare les deux parties", "encre", "s")
save(fig, "42-033")

