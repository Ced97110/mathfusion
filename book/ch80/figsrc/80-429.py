import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
text(ax, 44, 61, r"$\vee$ lu comme $+$ modulo 2", 'encre', 's')
X = [22, 38, 54]; Y = [44, 30, 16]
vals = [[r"$\vee$", '0', '1'], ['0', '0', '1'], ['1', '1', '0']]
for i in range(3):
    for j in range(3):
        role = 'fixe' if (i == 0 or j == 0) else 'sujet'
        if (i, j) == (2, 2): role = 'limite'
        box(ax, X[j], Y[i], 16, 12, role, label=vals[i][j], size='m')
text(ax, 44, 8, r"$a\vee a=a$ est faux pour $a=1$", 'limite', 's')
save(fig, '80-429')
