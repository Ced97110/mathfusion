import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for i in range(6):
    box(ax, 6 + i * 13, 42, 11, 9, 'sujet' if i < 3 else 'fixe')
brace(ax, 6, 30, 52.5, 'sujet', label=r'$A_3$ : 3', down=False)
brace(ax, 45, 82, 52.5, 'fixe', label='les 3 autres', down=False)
brace(ax, 6, 82, 41, 'encre', label=r'$S_3$ : 6 permutations', down=True)
text(ax, 44, 30, r'$6\div3=2$ : une racine carrée', 'varie', 's')
box(ax, 6, 6, 28, 12, 'autre', label=r'$K$')
arrow(ax, (34, 12), (54, 12), 'varie')
text(ax, 44, 16, r'$+\sqrt{d}$', 'varie', 's')
box(ax, 54, 6, 28, 12, 'autre', label=r'$K(\sqrt{d})$')
text(ax, 44, 23, r'ex. $y^3-2$ : $d=-108$', 'fixe', 's')
save(fig, '65-111')
