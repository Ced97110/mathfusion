import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 19, 74, 'sous-espaces', 'sujet', 'm'); text(ax, 69, 74, r'sous-groupes de $V$', 'autre', 'm')
sets = [r'$\{(0,0)\}$', r'$\{(0,0),(1,0)\}$', r'$\{(0,0),(0,1)\}$', r'$\{(0,0),(1,1)\}$', r'$E$ : les 4 couples']
for i, s in enumerate(sets):
    y = 56 - i * 13
    box(ax, 2, y, 34, 10, 'sujet', label=s, size='s')
    box(ax, 52, y, 34, 10, 'autre', label=s, size='s')
    arrow(ax, (37, y + 5), (51, y + 5), 'resultat', both=True)
save(fig, '79-154')
