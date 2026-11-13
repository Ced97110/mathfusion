import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
box(ax, 26, 84, 36, 11, 'sujet', label='8,315', size='l')
for y, f, r in [(66, '× 10', '83,15'), (50, '× 100', '831,5'), (34, '× 1 000', '8315')]:
    text(ax, 14, y + 5, f, 'varie', 'm', weight='bold')
    box(ax, 30, y, 28, 10, 'resultat', label=r, size='l')
    arrow(ax, (22, y + 5), (29, y + 5), 'varie')
text(ax, 72, 55, 'la virgule se\ndéplace', 'resultat', 's')
line(ax, [(4, 28), (84, 28)], 'fixe', dash=True)
text(ax, 14, 20, '× 20', 'limite', 'm', weight='bold')
box(ax, 30, 15, 28, 10, 'limite', label='83,15', size='l')
text(ax, 72, 20, 'faux : 166,3', 'limite', 's')
text(ax, 44, 7, r'$8{,}315\times20=166{,}3$', 'resultat', 'm')
save(fig, '08-053')
