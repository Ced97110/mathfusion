import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
yt, yb = 50.0, 28.0
f = numberline(ax, 14, 62, yt, 0, 2, 1)
numberline(ax, 14, 62, yb, 0, 2, 1)
text(ax, 2, 62, r'1er nombre : $2k=1$', 'sujet', 's', ha='left')
text(ax, 2, 40, r'2e nombre : $k=1$', 'sujet', 's', ha='left')
disc(ax, f(0.5), yt, 1.5, 'varie'); disc(ax, f(1), yb, 1.5, 'varie')
text(ax, f(0.5), yt + 5, r'$k=\frac{1}{2}$', 'varie', 's')
text(ax, f(1) + 7, yb + 4, r'$k=1$', 'varie', 's')
arrow(ax, (f(0.5) + 1, yt - 3.5), (f(1) - 0.5, yb + 3), 'limite', both=True)
text(ax, 74, 39, 'pas le même $k$', 'limite', 's')
text(ax, 44, 8, r'$(m\,;\,n)\in N\ \Leftrightarrow\ m=2n$', 'resultat', 'm')
save(fig, '57-128')
