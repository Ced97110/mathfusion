import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
f = numberline(ax, 6, 78, 36, 0, 9, labels=False)
for v in [0, 1, 4, 6, 9]:
    text(ax, f(v), 32, str(v), 'encre', 's')
for a, b, s in [(0, 1, r'$r_1$'), (1, 4, r'$r_3$'), (4, 6, r'$r_2$'), (6, 9, r'$r_3$')]:
    arrow(ax, (f(a), 37.5), (f(b), 37.5), 'varie', curve=-0.5)
    text(ax, (f(a) + f(b)) / 2, 37.5 + 2.2 + 3 * (f(b) - f(a)) / 24 + 3.5, s, 'varie', 's')
for v, s in [(4, '1 tour'), (8, '2 tours')]:
    line(ax, [(f(v), 32.8 - 2.2), (f(v), 28)], 'fixe', dash=True)
    text(ax, f(v), 25, s, 'fixe', 's')
box(ax, f(8), 33.5, f(9) - f(8), 5, 'resultat', fill=False, lw=0.6, r=0.3) if False else None
text(ax, 44, 14, r'$1+3+2+3=9=2\times4+1$', 'sujet', 'm')
box(ax, 14, 2, 60, 8, 'resultat')
text(ax, 44, 6, 'reste 1 : un quart de tour', 'resultat', 's')
text(ax, 44, 54, 'quarts de tour mis bout à bout', 'fixe', 's')
save(fig, '45-224')
