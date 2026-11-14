import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
xs = {n: 8 + (n - 1) * 14.4 for n in range(1, 7)}
R = {1: 1, 2: 2, 3: 0, 4: 1, 5: 2, 6: 0}; tx = {0: 12, 1: 34, 2: 56, 5: 78}
for n, r in R.items():
    hot = n in (1, 4)
    arrow(ax, (xs[n], 54.5), (tx[r], 26.5), 'varie' if hot else 'fixe', lw=1.2 if hot else 0.5)
for n in R: disc(ax, xs[n], 58, 3.2, 'varie' if n in (1, 4) else 'fixe', label=str(n))
for v, x in tx.items(): disc(ax, x, 23, 3.4, 'limite' if v == 5 else ('sujet' if v == 1 else 'fixe'), label=str(v))
text(ax, 34, 69, r'$f^{-1}(1)=\bar{1}=\{1,4\}$', 'varie', 'm', weight='bold')
text(ax, 70, 11, r'$f^{-1}(5)=\emptyset$', 'limite', 'm', weight='bold')
text(ax, 20, 11, 'atteint : une classe', 'varie', 's')
arrow(ax, (78, 15.5), (78, 18.5), 'limite')
save(fig, '43-087')
