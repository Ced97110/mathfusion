import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 22, 78, '1 + 2 + 3 + 4', 'sujet', 'm')
text(ax, 66, 78, r'$4\times5/2$', 'autre', 'm')
for y, a, b in zip((64, 52, 40), ('1 + 2 = 3', '3 + 3 = 6', '6 + 4 = 10'), (r'4 + 1 = 5', r'$4\times5=20$', '20 / 2 = 10')):
    box(ax, 6, y, 32, 8, 'sujet', label=a)
    box(ax, 50, y, 32, 8, 'autre', label=b)
for x in (22, 66):
    arrow(ax, (x, 63.5), (x, 60.5), 'varie'); arrow(ax, (x, 51.5), (x, 48.5), 'varie')
line(ax, [(44, 36), (44, 82)], 'fixe', dash=True)
box(ax, 30, 22, 28, 8, 'resultat', label='10 = 10', size='l')
arrow(ax, (22, 39.5), (34, 30.5), 'resultat'); arrow(ax, (66, 39.5), (54, 30.5), 'resultat')
line(ax, [(4, 17), (84, 17)], 'fixe')
text(ax, 22, 12, 'n = 1 000 : 999 additions', 'sujet', 's')
text(ax, 66, 12, '3 opérations', 'autre', 's')
save(fig, '01-123')
