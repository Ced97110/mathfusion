import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# deux zones
box(ax, 2, 4, 40, 70, 'resultat')
box(ax, 46, 4, 40, 70, 'autre')
text(ax, 22, 68, 'résolubles', 'resultat', 'l', weight='bold')
text(ax, 66, 68, 'non résolubles', 'autre', 'l', weight='bold')
# zone de gauche : quatre groupes
left = ['abélien', r'ordre $p^n$', r'$S_3$ : 6', r'$S_4$ : 24']
for k, lab in enumerate(left):
    box(ax, 6, 49 - 12.5 * k, 32, 8, 'encre', label=lab)
# zone de droite : A5, S5, Sn, chacun contient le précédent
right = [r'$A_5$ : 60', r'$S_5$ : 120', r'$S_n$, $n\geq 5$']
ys = [49, 33, 17]
for k, lab in enumerate(right):
    box(ax, 50, ys[k], 32, 8, 'encre', label=lab)
for k in range(2):
    arrow(ax, (66, ys[k] - 0.3), (66, ys[k + 1] + 8.3), 'varie')
    text(ax, 70, ys[k] - 4, r'$\subset$', 'varie', 'm', ha='left')
text(ax, 66, 9, 'contient $A_5$ : non résoluble', 'autre', 's')
save(fig, '64-143')
