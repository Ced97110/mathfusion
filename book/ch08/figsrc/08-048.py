import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
X0, WD = 6, 76
def strip(y, n, fills):
    c = WD / n
    for i in range(n):
        r = fills.get(i)
        ax.add_patch(Rectangle((X0 + i * c, y), c, 6, ec=COL[r or 'fixe'], fc=FILL[r or 'encre'], lw=0.8 if n == 10 else 0.3, zorder=2))
text(ax, 44, 91, 'même taille : on additionne', 'resultat', 's')
strip(74, 10, {**{i: 'sujet' for i in range(4)}, **{i: 'autre' for i in range(4, 7)}})
text(ax, X0, 84, '4 dixièmes', 'sujet', 's', ha='left'); text(ax, X0 + 4 * 7.6, 84, '3 dixièmes', 'autre', 's', ha='left')
brace(ax, X0, X0 + 7 * 7.6, 73, 'resultat', '7 dixièmes')
text(ax, 44, 61, 'tailles différentes : non', 'limite', 's')
strip(46, 10, {i: 'sujet' for i in range(3)}); text(ax, X0, 56, '3 dixièmes', 'sujet', 's', ha='left')
strip(30, 100, {0: 'autre', 1: 'autre'}); text(ax, X0, 40, '2 centièmes', 'autre', 's', ha='left')
text(ax, 44, 23, 'pas 5 : parts différentes', 'limite', 's')
strip(12, 100, {**{i: 'sujet' for i in range(30)}, **{30: 'autre', 31: 'autre'}})
brace(ax, X0, X0 + 30 * 0.76, 11, 'sujet', '= 30 centièmes')
text(ax, 82, 7.3, '32 centièmes', 'resultat', 'm', ha='right')
save(fig, '08-048')
