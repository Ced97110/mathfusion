import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cols = [(12, 1, False), (33.5, 2, False), (55, 3, True), (76.5, 6, True)]
for cx, n, tr in cols:
    role = 'resultat' if tr else 'fixe'
    box(ax, cx - 10, 18, 20, 42, role, fill=False)
    text(ax, cx, 55, f'ordre {n}', role, 's')
    P = [(cx, 44), (cx - 6, 32), (cx + 6, 32)]
    for p in P:
        disc(ax, p[0], p[1], 1.8, 'sujet')
    if n == 2:
        arrow(ax, (P[1][0] + 2.5, 32), (P[2][0] - 2.5, 32), 'varie', both=True)
    if n == 3:
        arrow(ax, (P[0][0] - 1.5, P[0][1] - 2.3), (P[1][0] + 1.2, P[1][1] + 2.5), 'varie')
        arrow(ax, (P[1][0] + 2.5, 32), (P[2][0] - 2.5, 32), 'varie')
        arrow(ax, (P[2][0] - 1.2, P[2][1] + 2.5), (P[0][0] + 1.5, P[0][1] - 2.3), 'varie')
    if n == 6:
        arrow(ax, (P[1][0] + 2.5, 32), (P[2][0] - 2.5, 32), 'varie', both=True)
        arrow(ax, (P[0][0] - 1.5, P[0][1] - 2.3), (P[1][0] + 1.2, P[1][1] + 2.5), 'varie', both=True)
        arrow(ax, (P[0][0] + 1.5, P[0][1] - 2.3), (P[2][0] - 1.2, P[2][1] + 2.5), 'varie', both=True)
    text(ax, cx, 23, 'transitif' if tr else 'pas transitif', role, 's')
box(ax, 8, 3, 72, 10, 'resultat', label=r'orbite de 3 points : 3 divise l’ordre', size='s')
save(fig, '65-067')
