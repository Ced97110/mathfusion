import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, r'degré $n=2$ sur $\mathbb{R}$ : au plus 2 racines', 'sujet', 's')
sx, sy = 8.0, 6.0
def panel(cx, base, c, role):
    line(ax, [(cx - 19, base), (cx + 19, base)], 'fixe')
    xs = [i / 20 for i in range(-44, 45)]
    line(ax, [(cx + x * sx, base + (x * x + c) * sy) for x in xs if (x * x + c) * sy < 19], role, lw=1.2)
panel(23, 44, -1, 'sujet')
for v in (-1, 1):
    disc(ax, 23 + v * sx, 44, 1.5, 'resultat')
text(ax, 15, 38.5, '−1', 'resultat', 's')
text(ax, 31, 38.5, '1', 'resultat', 's')
text(ax, 23, 31, r'$x^2-1$ : 2 racines', 'resultat', 's')
panel(65, 44, 1, 'autre')
text(ax, 65, 31, r'$x^2+1$ : 0 racine', 'fixe', 's')
box(ax, 8, 8, 72, 14, 'resultat', label=r'racines $r \leq n$ : jamais 3 ici')
save(fig, '54-237')
