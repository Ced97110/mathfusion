import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(58)
CX = 56
order = [3, 5, 6, 7, 1, 2, 4]
top = ['resultat', 'resultat', 'sujet', 'resultat', 'sujet', 'sujet', 'sujet']
bot = ['sujet'] * 4 + ['resultat'] * 3
xs, p = bitrow(fig, ax, CX, 52, '1234567', 'encre', k=5)
cells(ax, xs, p, 52, 8, top)
bitrow(fig, ax, CX, 28, '3567124', 'encre', k=5)
cells(ax, xs, p, 28, 8, bot)
for q in range(7):
    j = order.index(q + 1)
    arrow(ax, (xs[q], 47.5), (xs[j], 32.5), 'fixe', lw=0.7)
text(ax, 2, 52, 'Hamming', 'fixe', 's', ha='left')
text(ax, 2, 28, 'Judson', 'fixe', 's', ha='left')
brace(ax, xs[0] - p / 2 + 0.4, xs[3] + p / 2 - 0.4, 22.5, 'sujet', label='4 de message', depth=1.8)
brace(ax, xs[4] - p / 2 + 0.4, xs[6] + p / 2 - 0.4, 22.5, 'resultat', label='3 de contrôle', depth=1.8)
text(ax, 44, 7, r'$H = (A \mid I_m)$', 'sujet', 'l', weight='bold')
crop(fig, ax, 2.3, 58.0)
save(fig, '68-138')
