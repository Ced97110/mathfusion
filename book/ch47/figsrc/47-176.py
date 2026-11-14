import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, r'$H=\{1,\ s\}$ et le quart de tour $r$', 'encre', 'm')
for y, name, l2, r2 in ((32, r'$rH$', r'$rs$', 'sujet'), (10, r'$Hr$', r'$r^3s$', 'varie')):
    text(ax, 10, y + 5, name, r2, 'm')
    box(ax, 20, y, 22, 10, 'fixe', label=r'$r$', size='m')
    box(ax, 46, y, 22, 10, r2, label=l2, size='m')
box(ax, 45, 9, 24, 33, 'limite', fill=False, lw=0.9)
text(ax, 77, 26, r'$\neq$', 'limite', 'xl')
text(ax, 44, 3.5, r"$H$ n'est pas normal", 'limite', 's')
save(fig, '47-176')
