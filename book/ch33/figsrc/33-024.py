import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for xs, o, cap in (((8, 28), 9, r'$3^2 = (-3)^2 = 9$'), ((60, 80), 25, r'$5^2 = (-5)^2 = 25$')):
    xm = (xs[0] + xs[1]) / 2
    disc(ax, xs[0], 10, 5, 'sujet', label=f'−{3 if o == 9 else 5}')
    disc(ax, xs[1], 10, 5, 'sujet', label=f'{3 if o == 9 else 5}')
    disc(ax, xm, 42, 5.5, 'resultat', label=str(o))
    for x in xs:
        arrow(ax, (x + (xm - x) * 0.18, 15.5), (xm - (xm - x) * 0.18, 36.4), 'varie')
    text(ax, xm, 54, cap, 'encre', 's')
text(ax, 44, 26, 'au carré', 'varie', 's')
save(fig, '33-024')
