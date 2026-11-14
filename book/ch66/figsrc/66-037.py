import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
text(ax, 44, 42, r'$\varphi(10)$ : premiers avec 10', 'sujet', 'm')
ok = {1, 3, 7, 9}
w = 8.0
for k in range(1, 11):
    x = 4 + (k - 1) * 8.1
    box(ax, x, 24, w, 10, 'resultat' if k in ok else 'fixe', label=str(k), r=0.6)
brace(ax, 4, 4 + 10 * 8.1 - 0.1, 22, 'fixe', label=None)
box(ax, 4, 2, 38, 9, 'resultat', label='4 sans diviseur commun')
box(ax, 46, 2, 38, 9, 'fixe', label='6 avec un diviseur')
save(fig, '66-037')
