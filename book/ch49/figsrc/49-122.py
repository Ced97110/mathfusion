import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'$G/H$ : deux sens', 'encre', 'l')
line(ax, [(44, 8), (44, 56)], 'fixe', dash=True)
text(ax, 22, 52, r'$H$ normal', 'autre', 's')
for x, n in [(3, r'$xH$'), (14, r'$yH$')]:
    box(ax, x, 36, 9, 8, 'autre', label=n, size='s', r=0.5)
text(ax, 11, 30, r'$\times$', 'varie', 'm') if False else text(ax, 11, 30, 'produit', 'varie', 's')
arrow(ax, (11, 28), (11, 21), 'varie') if False else None
box(ax, 27, 36, 12, 8, 'resultat', label=r'$xyH$', size='s', r=0.5)
arrow(ax, (23.5, 40), (26.5, 40), 'varie')
text(ax, 22, 14, 'un groupe', 'resultat', 's')
text(ax, 66, 52, r'$H$ non normal', 'sujet', 's')
for i in range(4):
    box(ax, 50 + (i % 2) * 14, 32 + (i // 2) * 10, 12, 8, 'sujet', r=0.5)
text(ax, 66, 24, '4 classes', 'sujet', 's')
text(ax, 66, 17, 'pas de produit', 'limite', 's')
text(ax, 66, 10, 'un ensemble', 'sujet', 's')
save(fig, '49-122')
