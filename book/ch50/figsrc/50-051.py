import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
X0, CW, CH = 8.0, 9.0, 7.0
def cells(y, members, role, nums):
    for i in range(8):
        on = i in members
        box(ax, X0 + i * CW, y, CW - 0.8, CH, role if on else 'fixe', fill=on, r=0.5, lw=0.7)
        if nums: text(ax, X0 + i * CW + (CW - 0.8) / 2, y - 2.8, str(i), 'fixe', 's')
text(ax, 44, 59, r"horloge entière : $8 = 2^3$ éléments", 'resultat', 's')
cells(46, set(range(8)), 'resultat', False)
text(ax, 23, 40, 'maximal : oui', 'resultat', 's')
text(ax, 65, 40, '8 éléments : oui', 'resultat', 's')
text(ax, 44, 30, r"$\{0, 4\}$ : $2 = 2^1$ éléments", 'limite', 's')
cells(17, {0, 4}, 'limite', True)
text(ax, 23, 6, 'maximal : non', 'limite', 's')
text(ax, 65, 6, '8 éléments : non', 'limite', 's')
save(fig, '50-051')
