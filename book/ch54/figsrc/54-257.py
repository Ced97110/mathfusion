import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 22, 69, r'$b$ et $d$ fractions', 'varie', 's')
text(ax, 66, 69, r'$b$ et $d$ entiers', 'resultat', 's')
S = 5.5  # mm par unité
def panel(cx, cy, role, pts):
    line(ax, [(cx - 18, cy), (cx + 18, cy)], 'fixe', lw=0.6)
    line(ax, [(cx, cy - 18), (cx, cy + 18)], 'fixe', lw=0.6)
    for sgn in (1, -1):
        c = [(cx + sgn * b * S, cy + sgn * S / b) for b in [0.32 + i * 0.02 for i in range(0, 135)] if 1 / b * S < 17.5 and b * S < 17.5]
        line(ax, c, 'fixe', lw=0.8)
    for b, d in pts:
        disc(ax, cx + b * S, cy + d * S, 1.1, role)
fr = []
for b in (1 / 3, 1 / 2, 2 / 3, 1, 3 / 2, 2, 3):
    fr += [(b, 1 / b), (-b, -1 / b)]
panel(22, 38, 'varie', fr)
panel(66, 38, 'resultat', [(1, 1), (-1, -1)])
text(ax, 22, 14, r'$bd=1$ : une infinité', 'varie', 's')
text(ax, 66, 14, r'$bd=1$ : 2 cas', 'resultat', 's')
text(ax, 44, 5, 'Gauss impose les entiers', 'sujet', 's')
save(fig, '54-257')
