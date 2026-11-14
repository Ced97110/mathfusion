import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
x0, cy, kx, ky = 44, 38, 0.2, 0.3
X = lambda d: x0 + d * kx
Y = lambda v: cy + v * ky
g = lambda d: math.degrees(math.asin(math.sin(math.radians(d))))
line(ax, [(8, cy), (82, cy)], 'fixe', lw=0.7); line(ax, [(x0, 8), (x0, 70)], 'fixe', lw=0.7)
line(ax, [(X(-110), Y(-110)), (X(110), Y(110))], 'fixe', lw=0.8, dash=True)
line(ax, [(X(d), Y(g(d))) for d in range(-180, -89, 3)], 'limite', lw=1.6)
line(ax, [(X(d), Y(g(d))) for d in range(90, 181, 3)], 'limite', lw=1.6)
line(ax, [(X(d), Y(g(d))) for d in range(-90, 91, 3)], 'resultat', lw=2.4)
for d in (-90, 90):
    line(ax, [(X(d), cy - 1.2), (X(d), cy + 1.2)], 'fixe', lw=0.8)
text(ax, X(-90), cy + 5, r'$-\pi/2$', 'resultat', 's'); text(ax, X(90), cy - 5, r'$\pi/2$', 'resultat', 's')
line(ax, [(X(20), Y(20)), (X(160), Y(20))], 'fixe', lw=0.7, dash=True)
disc(ax, X(20), Y(20), 1.5, 'resultat'); disc(ax, X(160), Y(20), 1.5, 'limite')
text(ax, X(20) - 1, Y(20) + 4.5, '20°', 'resultat', 's'); text(ax, X(160), Y(20) + 4.5, '160°', 'limite', 's')
text(ax, 22, 68, r'$\arcsin(\sin x)$', 'sujet', 's'); text(ax, 72, 66, r'$y = x$', 'fixe', 's')
save(fig, '33-106')
