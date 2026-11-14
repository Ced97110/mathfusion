import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# two equations with x and y -> resultant with x only -> its roots on the x axis
box(ax, 4, 66, 36, 9, 'sujet', label=r'$f$ : avec $x$ et $y$', size='s')
box(ax, 48, 66, 36, 9, 'varie', label=r'$g$ : avec $x$ et $y$', size='s')
arrow(ax, (22, 66), (38, 56), 'varie')
arrow(ax, (66, 66), (50, 56), 'varie')
text(ax, 44, 61, r'sans $y$', 'varie', 's')
box(ax, 14, 47, 60, 9, 'resultat', label='résultant : en $x$ seul', size='m')
# curve of the resultant over the x axis
u = 11.0
ox, oy = 44.0, 22.0
Q = lambda x, y: (ox + u * x, oy + 3.0 * y)
arrow(ax, Q(-2.3, 0), Q(2.5, 0), 'fixe', lw=0.6)
text(ax, Q(2.5, 0)[0] + 2, oy - 2.2, r'$x$', 'fixe', 's')
xs = [t / 20 for t in range(-40, 41)]
line(ax, [Q(x, x * x * (x * x - 3)) for x in xs], 'resultat', lw=1.3)
for x in (-(3 ** 0.5), 0.0, 3 ** 0.5):
    disc(ax, *Q(x, 0), 1.1, 'resultat')
text(ax, 44, 10, 'il vaut 0 aux abscisses communes', 'resultat', 's')
save(fig, '70-005')
