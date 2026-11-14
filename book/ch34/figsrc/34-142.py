import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx, cy, kx, ky = 44, 28, 36, 17
X = lambda x: cx + kx * x; Y = lambda y: cy + ky * y
line(ax, [(X(-1.1), cy), (X(1.1), cy)], 'fixe', lw=0.7)
xs = [i / 100 for i in range(-100, 101)]
line(ax, [(X(x), Y(4 * x ** 3 - 3 * x)) for x in xs], 'sujet', lw=1.3)
r = math.sqrt(3) / 2
for v, ang in ((-r, '150°'), (0, '90°'), (r, '30°')):
    disc(ax, X(v), cy, 1.5, 'resultat')
    text(ax, X(v), cy - 5, f'{v:.3f}'.replace('.', ',').replace('-', '−').rstrip('0') if v else '0', 'resultat', 's')
    text(ax, X(v), cy - 10.5, ang, 'varie', 's')
text(ax, X(0.62), Y(1.05), r'$4x^3-3x$', 'sujet', 's')
text(ax, X(-0.5), 54, r'$x=\cos\theta$ ; racines : $0$ et $\pm\sqrt{3}/2$', 'fixe', 's')
save(fig, '34-142')
