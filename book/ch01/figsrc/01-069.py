import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, 'ville : 397 000 habitants', 'encre', 's')
for x in [22.5, 35, 47.5, 60, 72.5]:
    box(ax, x, 46, 11, 9, 'fixe')
text(ax, 53.75, 59, '5 cases : max 99 999', 'limite', 's')
text(ax, 15.5, 50.5, '3', 'limite', 'l')
arrow(ax, (15.5, 45), (15.5, 35.5), 'varie')
text(ax, 19, 40.5, '+ 1 case', 'varie', 's', ha='left')
for x, d in zip([10, 22.5, 35, 47.5, 60, 72.5], '397000'):
    if x == 10: box(ax, x, 25, 11, 9, 'sujet', label=d, size='l', lw=1.4)
    else: box(ax, x, 25, 11, 9, 'fixe', label=d, size='l')
text(ax, 15.5, 21, 'centaines de mille', 'sujet', 's')
text(ax, 44, 12, r'3 $\times$ 100 000 = 300 000', 'resultat', 'm')
save(fig, '01-069')
