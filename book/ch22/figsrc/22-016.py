import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 30.0; x0, y0 = 10, 12
A, B, C, D = (x0, y0), (x0+s, y0), (x0+s, y0+s), (x0, y0+s)
poly(ax, [A, B, C], 'sujet'); poly(ax, [A, C, D], 'autre')
text(ax, x0 + 0.72*s, y0 + 0.3*s, '1/2', 'sujet', 'l')
text(ax, x0 + 0.28*s, y0 + 0.7*s, '1/2', 'autre', 'l')
text(ax, x0 + s/2, y0 + s + 5, 'carré d\'aire 1', 'encre', 's')
text(ax, 64, 38, 'la diagonale\ncoupe en 2\ntriangles égaux', 'encre', 'm')
text(ax, 64, 18, '1 ÷ 2 = 1/2\npour chacun', 'resultat', 'm')
save(fig, '22-016')
