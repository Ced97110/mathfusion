import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
box(ax, 2, 80, 36, 12, 'fixe', label=r'$q^n=\sum_{d|n}d\,N(d,q)$', size='s')
arrow(ax, (39, 86), (47, 86), 'varie')
box(ax, 48, 80, 38, 12, 'varie', label=r'$\mu$ : signes $+1$, $-1$, $0$', size='s')
text(ax, 44, 72, r'isole $N(n,q)$ en une formule', 'resultat', 's')
cases = [(r'$k=1$', r'$\mu(k)=1$'),
         (r'$k$ = produit de $r$ premiers distincts', r'$\mu(k)=(-1)^r$'),
         (r'$e^2$ divise $k$, $e>1$', r'$\mu(k)=0$')]
for i, (a, b) in enumerate(cases):
    y = 52 - i * 18
    box(ax, 2, y - 6, 50, 12, 'fixe', label=a, size='s')
    arrow(ax, (53, y), (59, y), 'fixe')
    box(ax, 60, y - 6, 26, 12, 'sujet', label=b, size='s')
text(ax, 44, 6, 'trois cas, trois valeurs', 'encre', 's')
save(fig, '67-118')
