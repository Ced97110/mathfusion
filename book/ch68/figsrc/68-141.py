import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(74)
CX = 56
order = [3, 5, 6, 7, 1, 2, 4]
top = ['resultat', 'resultat', 'sujet', 'resultat', 'sujet', 'sujet', 'sujet']
bot = ['sujet'] * 4 + ['resultat'] * 3
xs, p = bitrow(fig, ax, CX, 68, '1234567', 'fixe', k=5)
cells(ax, xs, p, 58, 8, top)
bitrow(fig, ax, CX, 58, '0011001', 'encre', k=5)
cells(ax, xs, p, 20, 8, bot)
bitrow(fig, ax, CX, 20, '1001001', 'encre', k=5)
bitrow(fig, ax, CX, 10, '3567124', 'fixe', k=5)
for q in range(7):
    j = order.index(q + 1)
    arrow(ax, (xs[q], 53.5), (xs[j], 24.5), 'varie', lw=0.7)
text(ax, 2, 63, 'ordre de\nHamming', 'fixe', 's', ha='left')
text(ax, 2, 15, 'ordre de\nJudson', 'fixe', 's', ha='left')
crop(fig, ax, 6.0, 74.0)
save(fig, '68-141')
