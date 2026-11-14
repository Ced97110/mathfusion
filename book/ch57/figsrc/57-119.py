import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 2, 84, 62, 'fixe')
text(ax, 6, 59, 'End($R$, +)', 'fixe', 'm', ha='left')
for x0, role, head, labs in ((6, 'autre', '$R_L$', ['$x$ ↦ 3$x$', '$x$ ↦ 2$x$', '…']),
                             (48, 'sujet', '$R_R$', ['$x$ ↦ $x$3', '$x$ ↦ $x$2', '…'])):
    box(ax, x0, 6, 34, 46, role)
    text(ax, x0 + 17, 45, head, role, 'l')
    for i, lab in enumerate(labs):
        box(ax, x0 + 5, 30 - 10 * i, 24, 8, role, label=lab, size='s')
save(fig, '57-119')
