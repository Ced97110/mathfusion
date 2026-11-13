import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 12; x0 = 8
for i in range(3):
    box(ax, x0 + i * u, 38, u, 9, 'fixe', label=None)
brace(ax, x0, x0 + 3 * u, 47, 'fixe', label='$n=3$', down=False)
box(ax, x0, 20, 2 * u, 9, 'sujet', label='$E$ : 2')
box(ax, x0 + 2 * u, 20, 2 * u, 9, 'autre', label='$G$ : 2')
line(ax, [(x0 + 3 * u, 50), (x0 + 3 * u, 17)], 'limite', dash=True, lw=1.0)
text(ax, x0 + 3 * u + 10, 40, 'limite $n$', 'limite', 's')
brace(ax, x0, x0 + 4 * u, 20, 'limite', label='$2+2=4>3$', down=True)
save(fig, '71-187')
