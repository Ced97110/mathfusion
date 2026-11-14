import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 8, 58, 30, 11, 'sujet', label=r'$x^2+y^2$'); box(ax, 50, 58, 30, 11, 'autre', label=r'$x^2-y^2$')
text(ax, 44, 63.5, 'comparées', 'fixe', 's')
rows = [(r'$\mathbb{R}$', 'pas congruentes', 'limite'), (r'$\mathbb{C}$', 'congruentes', 'resultat'), (r'$\mathbb{Z}/5$', 'règle : discriminant', 'varie')]
for k, (k_, v, r) in enumerate(rows):
    y = 40 - k * 17
    box(ax, 8, y, 20, 12, 'fixe', label=k_, size='l'); arrow(ax, (30, y + 6), (38, y + 6), 'fixe'); box(ax, 40, y, 40, 12, r, label=v, size='m')
text(ax, 44, 4, 'la réponse dépend du corps', 'encre', 's')
save(fig, '71-201')
