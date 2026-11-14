import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 2, 50, r'$2\mathbb{Z}$ : les entiers pairs', 'sujet', 'm', ha='left', weight='bold')
f = numberline(ax, 8, 78, 20, 0, 8, 1, arrow_right=False)
for v in range(9):
    if v % 2 == 0:
        disc(ax, f(v), 28, 2.6, 'sujet')
disc(ax, f(1), 28, 2.6, 'limite', fill=False)
text(ax, f(1), 35, r'$1$ pas pair', 'limite', 's')
text(ax, 44, 10, r'$e\times2=2$ demande $e=1$', 'varie', 'm')
assert 2 // 2 == 1 and 1 % 2 == 1
save(fig, '56-162')
