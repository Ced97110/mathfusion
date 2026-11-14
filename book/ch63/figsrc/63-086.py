import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'$b$ minimale, $b_1=1$ ; on suppose $b_2\notin F$', 'sujet', 's')
text(ax, 50, 68, 'coord. 1', 'fixe', 's')
text(ax, 75, 68, 'coord. 2', 'fixe', 's')
labs = [r'$b$', r'$\eta_k(b)$', r'$b-\eta_k(b)$']
cells = [(r'$1$', r'$b_2$'), (r'$1$', r'$\eta_k(b_2)$'), (r'$0$', r'$b_2-\eta_k(b_2)\neq0$')]
roles = ['sujet', 'autre', 'varie']
for i in range(3):
    y = 48 - i * 17
    text(ax, 18, y + 7, labs[i], roles[i], 's')
    box(ax, 38, y, 24, 14, roles[i], label=cells[i][0], size='s')
    box(ax, 64, y, 22, 14, roles[i], label=cells[i][1], size='s')
text(ax, 44, 12, 'différence : plus courte que $b$', 'varie', 's')
text(ax, 44, 4, 'contradiction avec le minimum', 'limite', 's')
save(fig, '63-086')
