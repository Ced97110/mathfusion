import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(73)
D=-12
X0, X1 = 8, 78
rows = [(70+D, 'fixe'), (49+D, 'resultat'), (28+D, 'fixe')]
fs = [numberline(ax, X0, X1, y, 0, 20, 1, labels=False, role=r) for y, r in rows]
f = fs[0]
for v in (0, 10, 20): text(ax, f(v), 24.6+D, str(v), 'fixe', 's')
line(ax, [(f(10), 25.5+D), (f(10), 72.5+D)], 'fixe', lw=0.7, dash=True)
def lab(x, y, t, role, tx, ty, dx):
    y+=D; ty+=D
    text(ax, tx, ty, t, role, 's')
    line(ax, [(tx + dx, ty - 1.4), (x, y + 0.9)], role, lw=0.6)
# A
text(ax, 3, 81+D, 'facteur 5 : deux écritures', 'limite', 's', ha='left')
disc(ax, 25.5, 70+D, 0.9, 'limite')
lab(25.5, 70, '« 5 »', 'limite', 19, 75, 1); lab(25.5, 70, '« 10 »', 'limite', 32, 75, -1)
# B
text(ax, 3, 60+D, 'facteur 10 : une écriture', 'resultat', 's', ha='left')
disc(ax, f(9), 49+D, 0.9, 'resultat'); disc(ax, f(10), 49+D, 0.9, 'resultat')
lab(f(9), 49, '« 9 »', 'resultat', 35, 54, 1); lab(f(10), 49, '« 10 »', 'resultat', 49, 54, -1)
# C
text(ax, 3, 39+D, 'facteur 20 : des trous', 'limite', 's', ha='left')
disc(ax, f(9), 28+D, 0.9, 'fixe'); disc(ax, f(20), 28+D, 0.9, 'fixe')
lab(f(9), 28, '« 9 »', 'fixe', 35, 33, 1)
text(ax, 78, 33+D, '« 10 »', 'fixe', 's')
line(ax, [(f(10), 28+D), (f(19), 28+D)], 'limite', lw=2.2)
text(ax, 58.75, 32.5+D, 'aucune écriture', 'limite', 's')
save(fig, '01-071')
