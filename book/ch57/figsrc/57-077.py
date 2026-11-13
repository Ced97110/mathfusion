import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 22, 53, 'dans ℤ', 'fixe', 's')
text(ax, 66, 53, 'anneau des règles', 'fixe', 's')
line(ax, [(46, 14), (46, 56)], 'fixe', lw=0.5, dash=True)
for y, n in [(36, '5'), (20, '12')]:
    box(ax, 4, y, 12, 9, 'sujet', label=n)
    arrow(ax, (18, y + 4.5), (28, y + 4.5), 'varie')
    text(ax, 23, y + 8, '×1', 'varie', 's')
    box(ax, 30, y, 12, 9, 'resultat', label=n)
box(ax, 50, 32, 34, 12, 'varie', label='ne rien changer')
text(ax, 67, 26, 'joue le rôle de 1', 'varie', 's')
text(ax, 44, 6, '1 laisse tout inchangé', 'resultat', 'm')
save(fig, '57-077')
