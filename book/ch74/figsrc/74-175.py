import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
Fp = [(0,0),(0.7,0),(0.7,1.4),(1.6,1.4),(1.6,2.0),(0.7,2.0),(0.7,2.3),(2.0,2.3),(2.0,3.0),(0,3.0)]
k = 3.2
def F(x, y, role): poly(ax, [(x + px*k, y + py*k) for px, py in Fp], role)
F(6, 56, 'sujet')
text(ax, 18, 60, 'un seul F : l’identité', 'sujet', 'm', ha='left')
f = numberline(ax, 8, 64, 20, 0, 12, step=3)
for v in (0, 3, 6, 9, 12): F(f(v) - 3, 25, 'sujet')
arrow(ax, (f(0), 38), (f(3), 38), 'varie')
text(ax, (f(0)+f(3))/2, 42, '3 cm', 'varie', 's')
text(ax, 76, 20, '…', 'fixe', 'xl')
text(ax, 38, 8, 'glissements : 3, 6, 9, 12, …', 'varie', 'm')
save(fig, '74-175')
