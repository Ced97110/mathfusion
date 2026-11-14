import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, '1 livre = 16 onces', 'sujet', 'm', weight='bold')
for k, n in enumerate([1, 3, 5]):
    y = 44 - k * 15
    box(ax, 4, y, 26, 9, 'sujet', label=f'{n} livre' + ('s' if n > 1 else ''), size='s')
    arrow(ax, (30, y + 4.5), (54, y + 4.5), 'varie'); text(ax, 42, y + 8, r'$\times$ 16', 'varie', 's')
    box(ax, 54, y, 30, 9, 'resultat', label=f'{16 * n} onces', size='s')
text(ax, 44, 5, '16 onces par livre, toujours', 'resultat', 's')
save(fig, '11-027')
