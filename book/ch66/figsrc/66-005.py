import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import gcd
fig, ax = canvas(74)
labs = {5: r'$n=5$ : $\varphi(5)=4$ verts (sans diviseur commun)', 6: r'$n=6$ : $\varphi(6)=2$ verts'}
for n, y in [(5, 52), (6, 26)]:
    ks = list(range(1, n + 1)); x0 = 44 - (12 * n - 2) / 2
    for i, k in enumerate(ks):
        ok = gcd(k, n) == 1
        box(ax, x0 + 12 * i, y, 10, 9, 'resultat' if ok else 'fixe', label=str(k))
    text(ax, 44, y + 14, labs[n], 'resultat', 's')
arrow(ax, (44, 23), (44, 16.5), 'varie')
box(ax, 4, 4, 80, 12, 'sujet', label=r'$n\ \rightarrow\ \varphi(n)\ \rightarrow$ le $n$-gone se construit ?', size='s')
save(fig, '66-005')
