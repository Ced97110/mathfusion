import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(58)
g = 20.0
ta, tb = math.tan(math.radians(18)), math.tan(math.radians(21.25))
# même figure, deux tailles : base 1 000 m (même échelle 0,004 mm par mètre)
for xs, k, d, h, dl, hl, ha in [(27.0, 0.004, 1000, 1975.55, 'd = 1 000 m', 'h ≈ 1 976 m', 'center'),
                                 (80.0, 0.004, 2000, 3951.1, 'd = 2 000 m', 'h ≈ 3 951 m', 'center')]:
    hh = h * k
    A = (xs - hh / ta, g); B = (xs - hh / tb, g); S = (xs, g + hh)
    poly(ax, [A, (xs, g), S], 'sujet')
    line(ax, [B, S], 'sujet', lw=1.2)
    line(ax, [(A[0] - 1.5, g), (xs + 1.5, g)], 'fixe', lw=0.7)
    xm = max((A[0] + B[0]) / 2, 9.0)
    text(ax, xm, g - 3.5, dl, 'fixe', 's', weight='bold')
    text(ax, xs - 2, g + hh + 3.5, hl, 'resultat', 's', weight='bold')
arrow(ax, (14, 50), (70, 50), 'varie')
text(ax, 42, 54, '× 2 : figure agrandie', 'varie', 's', weight='bold')
text(ax, 44, 6.5, 'mêmes angles : 18° et 21,25°', 'fixe', 's')
save(fig, '38-041')
