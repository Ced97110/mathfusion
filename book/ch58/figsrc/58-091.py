import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 57, r'$\mathbb{R}^n$', 'sujet', 'xl', weight='bold')
w, h, x0 = 14, 9, 30
def cells(y, labels, role='sujet'):
    for i, l in enumerate(labels):
        box(ax, x0 + i * w, y, w, h, role, label=l, size='s', dash=(l == '…'))
text(ax, 3, 42.5, r'$n=2$', 'encre', 's', ha='left')
cells(38, ['2,5', '1'])
text(ax, 3, 28.5, r'$n=3$', 'encre', 's', ha='left')
cells(24, [r'$u_1$', r'$u_2$', r'$u_3$'])
text(ax, 3, 14.5, r'$n$ quelconque', 'encre', 's', ha='left')
cells(10, [r'$u_1$', '…', r'$u_n$'])
brace(ax, x0, x0 + 3 * w, 10, 'sujet', label=r'$n$ cases')
save(fig, '58-091')
