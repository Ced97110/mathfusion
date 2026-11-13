import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 8, 44, 30, 12, 'sujet', label='440', size='l'); box(ax, 50, 44, 30, 12, 'autre', label='442', size='l')
text(ax, 23, 59.5, 'diapason', 'sujet', 's'); text(ax, 65, 59.5, 'corde', 'autre', 's')
xs = (4, 32, 60)
labs = (('somme', '882', 'limite'), ('moyenne', '441', 'limite'), ('différence', '2', 'resultat'))
for x, (n, v, r) in zip(xs, labs):
    box(ax, x, 22, 24, 14, r, label=v, size='l')
    text(ax, x + 12, 39.5, n, r, 's')
    arrow(ax, (23 if x < 30 else 65, 43), (x + 12, 42), 'fixe', 0.6) if False else None
text(ax, 16, 17, 'non', 'limite', 's'); text(ax, 44, 17, 'non', 'limite', 's'); text(ax, 72, 17, 'oui', 'resultat', 's')
arrow(ax, (72, 12), (72, 7), 'resultat', 1.0) if False else None
text(ax, 44, 6, 'on entend : 2 fois par seconde', 'resultat', 's')
save(fig, '35-006')
