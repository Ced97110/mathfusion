import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for y, t in zip([46, 34, 22], ['gourde', 'carte', 'lampe']):
    box(ax, 3, y - 4.5, 18, 9, 'sujet', label=t, size='s')
    arrow(ax, (22, y), (29, y), 'varie')
    box(ax, 30, y - 4.5, 12, 9, 'resultat', label='oui', size='s')
    text(ax, 46, y, 'ou', 'fixe', 's')
    box(ax, 50, y - 4.5, 12, 9, 'fixe', label='non', size='s')
box(ax, 68, 30, 18, 10, 'limite', fill=False, dash=True, label='à moitié', size='s')
text(ax, 77, 25, 'interdit', 'limite', 's')
text(ax, 32, 8, r'$2\times 2\times 2 = 8$ sacs', 'resultat', 'l')
save(fig, '42-022')
