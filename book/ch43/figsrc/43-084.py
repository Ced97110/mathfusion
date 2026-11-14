import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(85)
R = {1: 1, 2: 2, 3: 0, 4: 1, 5: 2, 6: 0}
ys = {n: 76 - (n - 1) * 11 for n in R}; ty = {1: 66, 2: 43, 0: 20}
text(ax, 14, 83, r'$S$', 'fixe', 'm'); text(ax, 70, 83, r'$T$', 'fixe', 'm')
for n, r in R.items():
    hot = n in (1, 4)
    arrow(ax, (17, ys[n]), (62, ty[r]), 'sujet' if hot else 'fixe', lw=1.2 if hot else 0.6)
for n in R: disc(ax, 14, ys[n], 3, 'sujet' if n in (1, 4) else 'fixe', label=str(n))
for v, y in ty.items(): disc(ax, 66, y, 3.4, 'sujet' if v == 1 else 'fixe', label=str(v))
text(ax, 80, 54, r'$f$ : reste', 'fixe', 's')
text(ax, 44, 4, r'$1\ E_f\ 4$ car $f(1)=f(4)$', 'sujet', 'm', weight='bold')
save(fig, '43-084')
