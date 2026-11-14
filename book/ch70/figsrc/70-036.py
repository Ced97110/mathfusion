import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, r'même écriture pour $g$ : $b_m$, $m$', 'autre', 's')
X0, BW, GAP = 22, 15, 1.5
def row(y, labels, name):
    text(ax, 2, y + 4.5, name, 'fixe', 's', ha='left')
    n = len(labels)
    for k, s in enumerate(labels):
        role = 'sujet' if k in (0, n - 1) else 'varie'
        box(ax, X0 + k * (BW + GAP), y, BW, 9, role, label=s, size='s', r=0.5)
row(46, [r'$a_ny^n$', '…', r'$a_0$'], r'degré $n$')
row(28, [r'$a_2y^2$', r'$a_1y$', r'$a_0$'], r'$n=2$')
row(10, [r'$a_3y^3$', r'$a_2y^2$', r'$a_1y$', r'$a_0$'], r'$n=3$')
save(fig, '70-036')
