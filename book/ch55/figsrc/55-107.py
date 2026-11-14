import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, ux, uy = 10, 12, 12.0, 4.0
X = lambda x: ox + x * ux
Y = lambda y: oy + y * uy
arrow(ax, (ox - 3, oy), (X(5.3), oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy - 4), (ox, Y(12) + 5), 'fixe', lw=0.9)
xs = [i * 5.2 / 60 for i in range(61)]
line(ax, [(X(x), Y(x * x - 7 * x + 12)) for x in xs], 'sujet', lw=1.3)
line(ax, [(X(3.5), oy - 3), (X(3.5), Y(5))], 'varie', lw=1.0, dash=True)
text(ax, X(3.5), Y(5) + 5, r'$(3+4)/2=3{,}5$', 'varie', 's')
for r in (3, 4):
    disc(ax, X(r), oy, 1.8, 'sujet')
    text(ax, X(r), oy - 5, str(r), 'sujet', 'm')
disc(ax, X(0), Y(12), 1.8, 'resultat')
text(ax, X(0) + 4, Y(12), r'$(0-3)(0-4)=12$', 'resultat', 's', ha='left')
text(ax, X(5.2) - 2, Y(2.64) + 8, r'$x^2-7x+12$', 'sujet', 's')
save(fig, '55-107')
