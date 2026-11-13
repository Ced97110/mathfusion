import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
keep = {1, 5, 7, 11}
text(ax, 44, 33, r'$\varphi$(12) = 4', 'resultat', 'l')
for k in range(1, 13):
    r = 'resultat' if k in keep else 'limite'
    box(ax, 3 + (k - 1) * 6.7, 14, 6.0, 8, r, label=str(k), size='s', r=0.6)
text(ax, 44, 7, 'vert : sans diviseur commun avec 12', 'resultat', 's')
save(fig, '46-134')
