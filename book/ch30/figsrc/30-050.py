import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
X = {-1: 24, 0: 44, 1: 64}
arrow(ax, (8, 52), (80, 52), 'fixe', both=True); text(ax, 85, 52, 'cos', 'fixe', 's')
for v, lab in ((-1, '−0,017452'), (0, '0'), (1, '0,017452')):
    line(ax, [(X[v], 50.8), (X[v], 53.2)], 'fixe'); text(ax, X[v], 47.5, lab, 'fixe', 's')
disc(ax, 24, 60, 4, 'varie', label='91°', size='s'); disc(ax, 64, 60, 4, 'sujet', label='89°', size='s')
text(ax, 44, 60, 'axe vertical', 'fixe', 's')
text(ax, 44, 38, 'sin reste proche de 1', 'fixe', 's')
box(ax, 4, 8, 38, 24, 'varie', label='0,99985 ÷ (−0,017452)\n= −57,29', size='s')
box(ax, 46, 8, 38, 24, 'sujet', label='0,99985 ÷ 0,017452\n= 57,29', size='s')
arrow(ax, (24, 55.5), (23, 32.8), 'varie'); arrow(ax, (64, 55.5), (65, 32.8), 'sujet')
save(fig, '30-050')
