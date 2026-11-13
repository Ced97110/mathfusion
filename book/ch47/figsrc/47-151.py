import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
text(ax, 67, 44, r'$\mathbb{Z}/2\mathbb{Z}$', 'encre', 'm')
for y, role, lab, vals in [(29, 'sujet', 'N : pair', [0, 2, 4]), (9, 'varie', '1+N : impair', [1, 3, 5])]:
    text(ax, 2, y, lab, role, 's', ha='left')
    for i, v in enumerate(vals):
        disc(ax, 27 + 8 * i, y, 3.4, role, label=str(v), size='s')
for i in range(3): arrow(ax, (27 + 8 * i, 25.2), (27 + 8 * i, 12.8), 'fixe')
x0, c = 50, 10.5
roles = ['sujet', 'varie']; labs = ['pair', 'impair']
text(ax, x0 + c / 2, 37.5, '+', 'encre', 'l')
for j in range(2):
    text(ax, x0 + (j + 1.5) * c, 37.5, labs[j], roles[j], 's')
    text(ax, x0 + c / 2, 29.2 - j * c, labs[j], roles[j], 's')
    for i in range(2):
        box(ax, x0 + (j + 1) * c, 24 - i * c, c - 0.6, c - 0.6, roles[(i + j) % 2])
save(fig, '47-151')
