import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
s = 5.5; x0, y0 = 6, 12
b, h = 6, 4
poly(ax, [(x0, y0), (x0 + b * s, y0), (x0 + 2 * s, y0 + h * s)], 'sujet')
poly(ax, [(x0, y0), (x0 + 2 * s, y0 + h * s), (x0, y0 + h * s)], 'fixe')
poly(ax, [(x0 + b * s, y0), (x0 + b * s, y0 + h * s), (x0 + 2 * s, y0 + h * s)], 'fixe')
line(ax, [(x0, y0), (x0 + b * s, y0), (x0 + b * s, y0 + h * s), (x0, y0 + h * s), (x0, y0)], 'fixe', dash=True)
text(ax, x0 + b * s / 2, y0 - 4, '$b$ = 6 cm', 'varie', 's')
text(ax, x0 - 3, y0 + h * s / 2, '$h$ = 4', 'varie', 's', rot=90)
text(ax, x0 + 3.5 * s, y0 + 1.2 * s, 'triangle', 'sujet', 's')
text(ax, 62, 44, 'rectangle : 24 carrés', 'fixe', 's')
text(ax, 62, 36, 'triangle : 12 carrés', 'sujet', 's', weight='bold')
text(ax, 62, 28, 'gris : 12 carrés', 'fixe', 's')
text(ax, 62, 18, 'aire du triangle', 'resultat', 's')
text(ax, 62, 13, '= la moitié', 'resultat', 'm', weight='bold')
save(fig, '11-107')
