import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
roots = [-1.879, 0.347, 1.532]
x0, U = 44, 17.0
labs = [r'$-1{,}88$', r'$0{,}35$', r'$1{,}53$']
def row(y, title, role):
    text(ax, 44, y + 20, title, role, 's')
    arrow(ax, (4, y), (84, y), 'fixe', lw=0.8)
    for r, lab in zip(roots, labs):
        disc(ax, x0 + r * U, y, 2.0, role)
        text(ax, x0 + r * U, y - 6, lab, role, 's')
# sur Q : le cycle des trois racines
row(60, r'sur $\mathbb{Q}$ : 3 éléments, racines échangées', 'sujet')
P = [x0 + r * U for r in roots]
arrow(ax, (P[0] + 1, 63), (P[1] - 1, 63), 'varie', curve=-0.5)
arrow(ax, (P[1] + 1, 63), (P[2] - 1, 63), 'varie', curve=-0.5)
arrow(ax, (P[2] - 1, 57), (P[0] + 1, 57), 'varie', curve=-0.35)
# sur R : chacune reste en place
row(20, r'sur $\mathbb{R}$ : chaque racine reste en place', 'resultat')
text(ax, 44, 4, 'groupe réduit à l\'identité', 'resultat', 's')
save(fig, '65-153')
