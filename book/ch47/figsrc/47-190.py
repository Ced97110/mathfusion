import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
vals = ['3', '9', '7', '1']
for i, v in enumerate(vals):
    x = 6 + i * 22
    text(ax, x + 7, 42, rf'$3^{i + 1}$', 'fixe', 's')
    box(ax, x, 26, 14, 10, 'sujet', label=v, size='l')
    if i < 3: arrow(ax, (x + 14, 31), (x + 22, 31), 'varie')
text(ax, 6 + 2 * 22 + 7, 21.5, '27 : reste 7', 'fixe', 's')
text(ax, 6 + 3 * 22 + 7, 21.5, '81 : reste 1', 'fixe', 's')
brace(ax, 6, 86, 16, 'sujet', label=r'$\langle 3\rangle=U(10)$ : 4 cases', size='m')
save(fig, '47-190')
