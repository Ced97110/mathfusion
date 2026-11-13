import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def grid(cx, roles, first):
    for k, r in enumerate(roles):
        x = cx - 12.75 + (k % 4) * 8.5; y = 54 - (k // 4) * 10
        disc(ax, x, y, 3.5, r, label='1' if k == 0 else None, size='s')
text(ax, 23, 68, r'$D_4$', 'sujet', 'l'); text(ax, 65, 68, r'$Q_8$', 'autre', 'l')
grid(23, ['fixe', 'fixe', 'varie', 'fixe'] + ['varie'] * 4, 1)
grid(65, ['fixe', 'varie', 'fixe', 'fixe'] + ['fixe'] * 4, 1)
text(ax, 23, 31, '5', 'varie', 22); text(ax, 65, 31, '1', 'varie', 22)
text(ax, 44, 19, r'$x^2 = 1,\ x \neq 1$', 'varie', 's')
box(ax, 3, 3, 82, 9, 'limite', label=r'$5 \neq 1$ : pas le même groupe')
save(fig, '44-199')
