import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 73, r'multiplication modulo 5', 'fixe', 's')
for i, k in enumerate([1, 2, 3, 4]):
    y = 54 - i * 12
    box(ax, 8, y, 30, 9, 'sujet', label=rf'$0\times{k}=0$')
    arrow(ax, (38, y + 4.5), (56, 40), 'resultat')
disc(ax, 63, 40, 6, 'resultat', label='0')
text(ax, 63, 31, 'toujours 0', 'resultat', 's')
box(ax, 54, 6, 20, 10, 'limite', fill=False, dash=True, label='1')
text(ax, 64, 20.5, 'jamais atteint', 'limite', 's')
save(fig, '44-163')
