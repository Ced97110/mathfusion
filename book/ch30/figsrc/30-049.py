import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, cw = 14, 14.2
text(ax, 7, 40, 'angle', 'fixe', 's'); text(ax, 7, 24, 'tan', 'fixe', 's')
angs = ['80°', '89°', '89,9°', '90°', '91°']
vals = ['5,67', '57,29', '572,96', "n'existe\npas", '−57,29']
roles = ['sujet', 'sujet', 'sujet', 'limite', 'autre']
for i in range(5):
    box(ax, x0 + i * cw + 0.5, 35, cw - 1, 10, 'fixe', label=angs[i], size='s')
    box(ax, x0 + i * cw + 0.5, 17, cw - 1, 14, roles[i], label=vals[i], size='s')
cx = lambda i: x0 + i * cw + cw / 2
arrow(ax, (cx(0), 51), (cx(2), 51), 'varie'); text(ax, cx(1), 55, "s'approche de 90°", 'varie', 's')
arrow(ax, (cx(0), 12), (cx(2), 12), 'varie'); text(ax, cx(1), 7, 'grandit', 'varie', 's')
save(fig, '30-049')
