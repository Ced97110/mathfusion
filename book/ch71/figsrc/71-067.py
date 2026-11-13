import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def mat(x, y, w, h, v, role):
    box(ax, x, y, w, h, role)
    for k, s in enumerate(v):
        text(ax, x + w * (0.27 + 0.46 * (k % 2)), y + h * (0.72 - 0.44 * (k // 2)), s, role, 'm')
mat(3, 24, 24, 22, ['2', '0', '0', '1'], 'sujet')
mat(61, 24, 24, 22, ['1,5', '0,5', '0,5', '1,5'], 'varie')
arrow(ax, (28, 35), (60, 35), 'varie')
text(ax, 44, 40, r'$P^{-1}AP$', 'varie', 'm')
text(ax, 44, 30, 'même matrice, autre base', 'fixe', 's')
text(ax, 15, 17, r'$\det A=2$', 'sujet', 'm')
text(ax, 73, 17, r'$\det=2$', 'resultat', 'm')
text(ax, 44, 17, '=', 'resultat', 'l')
text(ax, 44, 6, 'le déterminant est conservé', 'resultat', 's')
save(fig, '71-067')
