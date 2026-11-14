import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, 'ℕ = 0, 1, 2, 3, …', 'sujet', 'l')
f = numberline(ax, 26, 76, 28, 0, 8)
for v in range(9):
    disc(ax, f(v), 28, 1.6, 'sujet')
line(ax, [(3, 28), (24, 28)], 'limite', dash=True)
text(ax, 13, 22, 'rien à gauche', 'limite', 's')
brace(ax, f(0), f(8), 19, 'sujet', label='on compte', down=True)
save(fig, '13-086')
