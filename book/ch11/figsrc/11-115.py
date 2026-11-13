import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
u = 2.7; y0 = 12; h = 4*u
xs = 2.5
text(ax, 44, 38, 'même base 6, même hauteur 4', 'fixe', 's')
for off in (0, 2, 5):
    P = [(xs, y0), (xs+6*u, y0), (xs+6*u+off*u, y0+h), (xs+off*u, y0+h)]
    poly(ax, P, 'sujet')
    line(ax, [P[0], P[3]], 'varie', lw=1.4)
    cx = xs + 3*u
    text(ax, cx, y0-4, f'décalage {off}', 'varie', 's')
    text(ax, cx+off*u/2, y0+h+4.5, 'A = 6 × 4 = 24', 'resultat', 's')
    xs += 6*u + off*u + 6
save(fig, '11-115')
