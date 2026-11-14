import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
P = 5.6
def row(y, counts, xs, arrows_x, labels, title, ty):
    text(ax, 44, ty, title, 'encre', 's', weight='bold')
    for n, x, role in zip(counts, xs, ['sujet', 'sujet', 'resultat'][-len(counts):] if False else None or ['sujet'] * (len(counts) - 1) + ['resultat']):
        for i in range(n):
            box(ax, x + i * P, y, 5, 5, role)
    for (a, b) in arrows_x:
        arrow(ax, (a, y + 2.5), (b, y + 2.5), 'varie')
        text(ax, (a + b) / 2, y + 7.3, 'dérivé', 'varie', 's')
    for x, lab in labels:
        text(ax, x, y - 4, lab, 'fixe', 's')
row(40, [5, 1], [2, 48], [(32, 46)],
    [(16, r'$\mathbb{Z}/5$'), (50.5, r'$G^{\prime}=\{e\}$')], 'horloge à 5 heures : 1 pas', 53)
row(14, [6, 3, 1], [2, 48, 75], [(37, 46), (64.5, 73)],
    [(18, r'$S_3$'), (55.3, r'$S_3^{\prime}=A_3$'), (77.5, r'$A_3^{\prime}=\{e\}$')], 'files de 3 élèves : 2 pas', 27)
save(fig, '64-069')
