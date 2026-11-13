import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
# a = λ b : la première case donne 1 = λ × 0, impossible
text(ax, 28, 49, r'$a = \lambda\, b$ ?', 'encre', 'l', weight='bold')
cw, ch = 9, 8
def col(x, vals, role, name):
    text(ax, x + cw / 2, 41, name, role, 'm', weight='bold')
    for i, v in enumerate(vals):
        box(ax, x, 29 - i * 9, cw, ch, role, label=v, size='m', r=0.5)
col(6, ['1', '2', '1'], 'sujet', r'$a$')
text(ax, 25, 24, r'$= \lambda \times$', 'varie', 'm', weight='bold')
col(36, ['0', '1', '−1'], 'autre', r'$b$')
box(ax, 4, 28.4, 43, 9.4, 'limite', fill=False, dash=True)
arrow(ax, (48, 33), (53, 33), 'limite', lw=1.0)
box(ax, 54, 22, 32, 22, 'limite', label='1re case :\n' + r'$1 = \lambda \times 0 = 0$' + '\nfaux', size='s')
save(fig, '58-189')
