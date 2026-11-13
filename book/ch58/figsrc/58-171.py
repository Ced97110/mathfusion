import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 50, 64, 'une base', 'sujet', 's')
text(ax, 72, 64, 'une autre base', 'autre', 's')
def group(x0, y, n, role):
    for i in range(n):
        box(ax, x0 + i * 8, y, 6.5, 6.5, role, r=0.5)
    xm = x0 + (n * 8 - 1.5) / 2
    brace(ax, x0, x0 + n * 8 - 1.5, y - 1.5, role, label=f'{n} vecteurs')
text(ax, 2, 50, r'$\mathbb{R}^3$', 'fixe', 'l', ha='left')
group(40, 47, 3, 'sujet'); group(64, 47, 3, 'autre')
text(ax, 2, 22, r'$\mathbb{Q}(\sqrt{2})$', 'fixe', 'l', ha='left')
group(44, 19, 2, 'sujet'); group(68, 19, 2, 'autre')
text(ax, 44, 4, 'toujours le même nombre ?', 'varie', 'm', weight='bold')
save(fig, '58-171')
