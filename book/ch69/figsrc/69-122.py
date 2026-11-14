import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'signes des termes de $F$', 'fixe', 's')
sg = ['+', '−', '+']
for x, s in zip([36, 44, 52], sg):
    disc(ax, x, 64, 3.2, 'fixe', label=s)
left = ['−', '+', '−']; right = ['+', '−', '+']
for x, s in zip([10, 20, 30], left):
    disc(ax, x, 22, 3.2, 'limite', label=s)
for x, s in zip([58, 68, 78], right):
    disc(ax, x, 22, 3.2, 'resultat', label=s)
arrow(ax, (38, 59), (21, 27), 'varie')
arrow(ax, (50, 59), (67, 27), 'varie')
text(ax, 13, 44, r'$e=1$ : $\times(-3)$', 'varie', 's')
text(ax, 75, 44, r'$e=2$ : $\times 9$', 'varie', 's')
text(ax, 20, 12, 'tous retournés', 'limite', 's')
text(ax, 68, 12, 'aucun changé', 'resultat', 's')
save(fig, '69-122')
