import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(72)
a = 0.35
x0, gy, u = 5, 36, 20
X = lambda t: x0 + u * a * (t - math.sin(t))
Y = lambda t: gy + u * a * (1 - math.cos(t))
ts = np.linspace(0, 10, 400)
line(ax, [(X(t), Y(t)) for t in ts], 'sujet', lw=1.5)
line(ax, [(x0 - 2, gy), (X(10) + 4, gy)], 'fixe', lw=0.8)
disc(ax, X(10), Y(10), 1.3, 'resultat')
text(ax, X(10) - 3, Y(10) + 7, 't = 10 :\n(3,69 ; 0,64)', 'resultat', 's', ha='right')
brace(ax, x0, X(math.pi), gy - 2, 'varie', label='avec √ : demi-arche', depth=1.6)
brace(ax, x0, X(10), gy - 13, 'sujet', label='avec t : tout le mouvement', depth=1.6)
text(ax, 44, 67, r'$x=at-a\sin t,\ y=a-a\cos t$', 'sujet', 'm')
text(ax, 44, 61, r'ou $x=at-\sqrt{2ay-y^2}$', 'varie', 's')
save(fig, '40-120')
