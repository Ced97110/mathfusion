import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
Fp = [(0,0),(0.7,0),(0.7,1.4),(1.6,1.4),(1.6,2.0),(0.7,2.0),(0.7,2.3),(2.0,2.3),(2.0,3.0),(0,3.0)]
k = 4.0
def F(x, y, role='sujet'): poly(ax, [(x + px*k, y + py*k) for px, py in Fp], role)
for i in range(3):
    for j in range(3): F(22 + i*24, 14 + j*16, 'sujet' if (i, j) != (0, 0) else 'sujet')
arrow(ax, (22, 8), (46, 8), 'varie')
text(ax, 34, 3.5, '3 cm', 'varie', 's')
arrow(ax, (15, 14), (15, 30), 'varie')
text(ax, 7, 22, '2 cm', 'varie', 's')
text(ax, 44, 72, r'$C_1$ : ni miroir, ni rotation', 'sujet', 'm')
text(ax, 44, 65, r'translations : $T \cong \mathbb{Z}\times\mathbb{Z}$', 'varie', 'm')
save(fig, '74-174')
