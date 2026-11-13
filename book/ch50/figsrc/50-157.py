import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, 'huit 3-cycles, tous des carrés', 'sujet', 's')
xs = [8 + i * 10.5 for i in range(8)]
for i, x in enumerate(xs): disc(ax, x, 55, 3.3, 'sujet' if i < 6 else 'limite')
box(ax, xs[0] - 6, 14, xs[5] - xs[0] + 12, 22, 'resultat')
text(ax, (xs[0] + xs[5]) / 2, 18.5, r'$H$ : 6 places', 'resultat', 's')
for i, x in enumerate(xs):
    if i < 6:
        arrow(ax, (x, 51.5), (x, 36.8), 'sujet')
        disc(ax, x, 25, 3.3, 'sujet', fill=False)
    else:
        arrow(ax, (x, 51.5), (x, 42), 'limite')
text(ax, (xs[6] + xs[7]) / 2, 37, '2 sans\nplace', 'limite', 's')
text(ax, 44, 6, r'8 > 6 : contradiction', 'limite', 'm', weight='bold')
save(fig, '50-157')
