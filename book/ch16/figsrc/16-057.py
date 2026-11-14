import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
rows = ((52, 'addition', ('x+3-3', 'x+0', 'x'), ('opposé\n3 − 3 = 0', 'neutre\nx + 0 = x')),
        (14, 'multiplication', (r'\frac{1}{3}\times 3x', r'1\times x', 'x'), ('inverse\n' + r'$3\times\frac{1}{3}=1$', 'neutre\n' + r'$1\times x=x$')))
for y, name, bx, lb in rows:
    text(ax, 2, y + 20, name, 'fixe', 's', ha='left', weight='bold')
    for i, t in enumerate(bx):
        x = 2 + i * 34
        box(ax, x, y, 16, 12, 'resultat' if i == 2 else 'sujet', label=r'$%s$' % t, size='s')
        if i < 2:
            arrow(ax, (x + 17, y + 6), (x + 33, y + 6), 'varie')
            text(ax, x + 25, y + 13, lb[i], 'varie', 's', va='bottom')
save(fig, '16-057')
