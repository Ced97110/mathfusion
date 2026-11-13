import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
p, sz, x0, y0 = 7, 6, 2, 14
for r in range(6):
    for c in range(8):
        box(ax, x0 + c * p, y0 + r * p, sz, sz, 'sujet' if r >= 3 else 'fixe', r=0.3, lw=0.5)
text(ax, 30, 62, r'$GL_2(F)$ : 48 matrices', 'fixe', 'm')
text(ax, 73, y0 + 5.25 * p, '$SL_2(F)$\n24 de\ndéterminant 1', 'sujet', 's')
text(ax, 73, y0 + 1.75 * p, '24 avec un\nautre\ndéterminant', 'fixe', 's')
text(ax, 30, 6, r'$F$ : 3 éléments, $n=2$', 'encre', 's')
save(fig, '73-122')
