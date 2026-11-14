import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0 = 8; Wb = 60
brace(ax, x0, x0 + Wb, 49, 'fixe', '1', down=False)
box(ax, x0, 38, 30, 9, 'varie', label='cos 2A = 0,5', size='s')
box(ax, x0 + 30, 38, 30, 9, 'sujet', label='1 − 0,5 = 0,5', size='s')
arrow(ax, (x0 + 45, 37), (x0 + 45, 26), 'varie')
text(ax, x0 + 48, 31.5, '÷ 2', 'varie', 's', ha='left')
box(ax, x0 + 30, 16, 15, 9, 'resultat', label='0,25', size='s')
box(ax, x0 + 45, 16, 15, 9, 'fixe', label='0,25', size='s')
text(ax, x0 + 37.5, 10, '$\\sin^2$ 30° = 0,25', 'resultat', 's')
save(fig, '34-109')
