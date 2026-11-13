import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
D=-12
for x, d in zip([4, 24, 44], '789'):
    pass
box(ax, 4, 58+D, 7, 8, 'fixe', fill=False, dash=True)
for i, (xl, xr, d) in enumerate([(4, 11, '7'), (24, 31, '8'), (44, 51, '9')]):
    if i: box(ax, xl, 58+D, 7, 8, 'fixe', fill=False, dash=True)
    box(ax, xr, 58+D, 7, 8, 'fixe', label=d, size='l')
box(ax, 68, 58+D, 7, 8, 'sujet', label='1', size='l', lw=1.4)
box(ax, 75, 58+D, 7, 8, 'fixe', label='0', size='l')
for a, b in [(18.5, 23.5), (38.5, 43.5), (58.5, 67.5)]:
    arrow(ax, (a, 62+D), (b, 62+D), 'varie')
arrow(ax, (78.5, 66.5+D), (71.5, 66.5+D), 'varie', curve=0.6)
text(ax, 58, 72+D, 'tour complet de 0 à 9', 'varie', 's')
box(ax, 26, 24+D, 49, 8, 'sujet', label=None)
for k in range(10): disc(ax, 30 + 4.5 * k, 28+D, 1.4, 'sujet')
arrow(ax, (71.5, 32.5+D), (71.5, 57.5+D), 'sujet')
text(ax, 50, 19+D, 'une dizaine = 10 unités', 'sujet', 'm')
text(ax, 66, 46+D, 'case : position des dizaines', 'fixe', 's', ha='right')
line(ax, [(66.3, 47.4+D), (69, 58+D)], 'fixe', lw=0.6)
text(ax, 66, 52+D, 'chiffre : un signe de 0 à 9', 'autre', 's', ha='right')
line(ax, [(66.3, 53.4+D), (70.3, 60.6+D)], 'autre', lw=0.6)
save(fig, '01-072')
