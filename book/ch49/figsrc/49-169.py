import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def sq(ax, cx, cy, h, hl, role, rr=2.6, lab=True, axis=True):
    P = {"A": (cx-h, cy-h), "B": (cx+h, cy-h), "C": (cx+h, cy+h), "D": (cx-h, cy+h)}
    poly(ax, list(P.values()), "fixe")
    if axis:
        o = {"A": "C", "C": "A", "B": "D", "D": "B"}[hl]
        (x0, y0), (x1, y1) = P[hl], P[o]; d = math.hypot(x1-x0, y1-y0); ux, uy = (x1-x0)/d, (y1-y0)/d
        line(ax, [(x0+ux*(rr+0.4), y0+uy*(rr+0.4)), (x1-ux*(rr+0.4), y1-uy*(rr+0.4))], role, lw=1.0, dash=True)
    for k, (x, y) in P.items():
        if k == hl: disc(ax, x, y, rr, role, label=k if lab else None, size="s")
        else: disc(ax, x, y, rr if lab else 1.0, "fixe", label=k if lab else None, size="s")

fig, ax = canvas(70)
sq(ax, 20, 44, 9, 'A', 'sujet'); sq(ax, 68, 44, 9, 'B', 'resultat')
arrow(ax, (34, 44), (54, 44), 'varie'); text(ax, 44, 50, r'$a = r$', 'varie', 's')
text(ax, 44, 38, r'$a\,(\mathrm{Stab}\,A)\,a^{-1}$', 'varie', 's')
text(ax, 20, 20, r'Stab $A = \{e,\ s\}$', 'sujet', 's')
text(ax, 68, 20, r"Stab $B = \{e,\ s'\}$", 'resultat', 's')
text(ax, 44, 8, r"$s' = r\,s\,r^{-1}$ : axe $BD$", 'varie', 's')
save(fig, '49-169')
