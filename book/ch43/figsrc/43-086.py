import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'$f^{-1}(1)=\{1,\ 4\}$', 'varie', 'l', weight='bold')
xs = {n: 8 + (n - 1) * 14.4 for n in range(1, 7)}
R = {1: 1, 2: 2, 3: 0, 4: 1, 5: 2, 6: 0}; tx = {0: 14, 1: 44, 2: 74}
for n, r in R.items():
    hot = n in (1, 4)
    arrow(ax, (xs[n], 49.5), (tx[r], 21.5), 'varie' if hot else 'fixe', lw=1.2 if hot else 0.5)
for n in R: disc(ax, xs[n], 53, 3.2, 'varie' if n in (1, 4) else 'fixe', label=str(n))
for v, x in tx.items(): disc(ax, x, 18, 3.4, 'sujet' if v == 1 else 'fixe', label=str(v))
text(ax, 44, 8, r'$c=1$ : on remonte vers les départs', 'sujet', 's')
text(ax, 4, 43, r'$S$', 'fixe', 's', ha='left'); text(ax, 4, 28, r'$T$', 'fixe', 's', ha='left')
save(fig, '43-086')
