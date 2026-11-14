import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
ox, oy = 12, 12
X = lambda k: ox + k * 17; Y = lambda v: oy + v * 1.6
arrow(ax, (ox, oy), (85, oy), 'fixe', lw=0.9); arrow(ax, (ox, oy), (ox, 86), 'fixe', lw=0.9)
for k in range(5):
    line(ax, [(X(k), oy - 1), (X(k), oy + 1)], 'fixe'); text(ax, X(k), 7.5, str(k), 'fixe', 's')
pts = [(X(k / 20), Y((k / 20) * (k / 20 - 1) ** 2)) for k in range(0, 81)]
line(ax, pts, 'resultat', lw=1.3)
for k, v, dx, dy in [(2, 2, -3, 5), (3, 12, -6, 5), (4, 36, -6, 4)]:
    disc(ax, X(k), Y(v), 1.8, 'sujet'); text(ax, X(k) + dx, Y(v) + dy, str(v), 'sujet', 'm')
text(ax, 32, 64, r'$k(k-1)^2$', 'resultat', 'l')
text(ax, 84.5, 7.5, r'$k$', 'fixe', 's')
text(ax, 6, 48, 'coloriages corrects', 'fixe', 's', rot=90)
save(fig, '80-383')
