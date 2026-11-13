import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
g = lambda v: 6 + (v + 10) * 3.0
line(ax, [(g(0), 18), (g(0), 58)], 'fixe', dash=True); text(ax, g(0), 62, '0', 'fixe', 'm')
box(ax, g(0), 44, 13 * 3, 9, 'sujet', label='départ : 13', size='s')
box(ax, g(-7), 26, 7 * 3, 9, 'autre', label='7 de plus', size='s')
box(ax, g(0), 26, 13 * 3, 9, 'varie', label='13 jusqu’à 0', size='s')
brace(ax, g(-7), g(13), 24, 'resultat', label='baisse : 20')
text(ax, 44, 8, '20 est plus grand que 13', 'resultat', 's')
save(fig, '13-125')
