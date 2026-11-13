import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
def nest(x0, role, labs):
    box(ax, x0, 6, 36, 62, role, size='s')
    box(ax, x0 + 4, 10, 28, 44, role, size='s')
    box(ax, x0 + 8, 14, 20, 22, role, size='s')
    text(ax, x0 + 18, 63, labs[0], role, 's', weight='bold')
    text(ax, x0 + 18, 49, labs[1], role, 's', weight='bold')
    text(ax, x0 + 18, 25, labs[2], role, 's', weight='bold')
nest(4, 'sujet', [r'$G$ : 12', r'$\langle2\rangle$ : 6', r'$K$ : 2'])
nest(48, 'autre', [r'$G/K$ : 6', r'$\langle2\rangle/K$ : 3', r'$K/K$ : 1'])
arrow(ax, (41, 40), (47, 40), 'varie')
text(ax, 44, 72, r'$H\mapsto H/K$', 'varie', 's')
save(fig, '48-091')
