import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 74, r'$b=5$ et $c=4$', 'fixe', 'm', weight='bold')
# part 1: the condition, drawn as two bars (25 and 16) to scale
text(ax, 4, 66, r'condition : $b^2>4c$', 'sujet', 'm', ha='left')
k = 1.5
box(ax, 4, 54, 25 * k, 7, 'sujet', label=r'$b^2=25$', size='s')
box(ax, 4, 45, 16 * k, 7, 'autre', label=r'$4c=16$', size='s')
text(ax, 4 + 25 * k + 3, 57.5, r'25 > 16', 'resultat', 's', ha='left')
arrow(ax, (44, 43), (44, 37), 'varie')
# part 2: the conclusion, checked with x = -1
text(ax, 4, 32, r'conclusion : il existe $x$', 'sujet', 'm', ha='left')
box(ax, 4, 20, 80, 8, 'resultat', label=r'$x=-1$ : $1-5+4=0$', size='m')
text(ax, 44, 12, r'$(-1)^2=1$ ; $5\times(-1)=-5$', 'fixe', 's')
save(fig, '70-009')
