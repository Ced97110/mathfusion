import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 4, 44, 22, 10, 'sujet', label=r'$9^1=9$')
arrow(ax, (26, 49), (38, 49), 'varie')
box(ax, 38, 44, 46, 10, 'sujet', label=r'$9^2=81$ : reste 1')
box(ax, 4, 2, 80, 28, 'fixe', fill=False, dash=True)
text(ax, 14, 26.5, r'$U(10)$', 'fixe', 'm')
for i, v in enumerate(['3', '7', '9', '1']):
    box(ax, 10 + i * 18, 14, 14, 9, 'sujet' if v in '91' else 'fixe', label=v, size='m')
arrow(ax, (15, 43.5), (53, 23.5), 'sujet')
arrow(ax, (61, 43.5), (71, 23.5), 'sujet')
brace(ax, 46, 78, 13.5, 'sujet', label=r'$\langle 9\rangle$ : 2 cases')
save(fig, '47-191')
