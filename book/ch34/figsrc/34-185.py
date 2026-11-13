import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def row(y, items):
    pass
box(ax, 2, 40, 24, 9, 'sujet', label=r'$\theta$ = 20°', size='s')
box(ax, 32, 40, 24, 9, 'varie', label=r'3$\theta$ = 60°', size='s')
box(ax, 62, 40, 24, 9, 'resultat', label='cos 60° = 0,5', size='s')
arrow(ax, (26, 44.5), (32, 44.5), 'varie'); arrow(ax, (56, 44.5), (62, 44.5), 'varie')
box(ax, 2, 18, 24, 11, 'sujet', label='cos 20° = $c$\n≈ 0,9397'.replace('$c$', r'$c$'), size='s')
box(ax, 32, 24, 24, 9, 'fixe', label=r'4$c^3$ = 3,3192', size='s')
box(ax, 32, 11, 24, 9, 'fixe', label=r'3$c$ = 2,8191', size='s')
box(ax, 62, 18, 24, 11, 'resultat', label=r'4$c^3$ − 3$c$' + '\n≈ 0,5', size='s')
arrow(ax, (14, 40), (14, 29.8), 'sujet')
arrow(ax, (26, 25), (32, 28.5), 'varie'); arrow(ax, (26, 22), (32, 15.5), 'varie')
arrow(ax, (56, 28.5), (62, 25), 'varie'); arrow(ax, (56, 15.5), (62, 22), 'varie')
arrow(ax, (74, 40), (74, 29.8), 'resultat', both=True)
text(ax, 44, 4, r'×2 donne 8$c^3$ − 6$c$ − 1 = 0', 'sujet', 's')
save(fig, '34-185')
