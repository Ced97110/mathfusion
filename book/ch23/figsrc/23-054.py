import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 44, 95, r'$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$', 'sujet', 'l')
S = [(r'$a=2,\ b=-4,\ c=-6$','sujet'), (r'$b^2-4ac=16+48=64$','fixe'), (r'$\sqrt{64}=8$','fixe'), (r'$x=(4\pm8)/4$','varie')]
ys = [70, 52, 34, 16]
for (t, r), y in zip(S, ys): box(ax, 14, y, 60, 11, r, label=t)
for i in range(3): arrow(ax, (44, ys[i]-0.3), (44, ys[i+1]+11.3), 'fixe')
box(ax, 8, 1, 30, 10, 'resultat', label=r'$x=3$'); box(ax, 50, 1, 30, 10, 'resultat', label=r'$x=-1$')
arrow(ax, (36, 15.5), (24, 11.5), 'varie'); arrow(ax, (52, 15.5), (64, 11.5), 'varie')
save(fig, '23-054')
