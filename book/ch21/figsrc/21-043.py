import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 9, 44, r'$16=$', 'sujet', 'm'); text(ax, 9, 24, r'$40=$', 'sujet', 'm')
line(ax, [(16, 34), (66, 34)], 'fixe', lw=0.6, dash=True)
for i in range(4):
    x = 20 + 10 * i
    disc(ax, x, 44, 4, 'varie' if i < 3 else 'sujet', label='2')
    if i < 3:
        disc(ax, x, 24, 4, 'varie', label='2'); line(ax, [(x, 39.4), (x, 28.6)], 'varie', dash=True)
disc(ax, 60, 24, 4, 'sujet', label='5')
text(ax, 38, 12, 'trois 2 communs : retirés', 'varie', 's')
text(ax, 44, 58, '1. factoriser  2. retirer', 'encre', 's')
arrow(ax, (66, 34), (72, 34), 'resultat')
box(ax, 73, 25, 13, 18, 'resultat', label=r'$\frac{2}{5}$', size='l')
save(fig, '21-043')
