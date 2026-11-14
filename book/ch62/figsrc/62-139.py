import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(92)
f = lambda x: (x - 1) ** 2 * (x + 2)
fp = lambda x: 3 * x ** 2 - 3
X = lambda x: 12 + x * 35
Yf = lambda v: 62 + v * 5          # panneau du haut : f
Yd = lambda v: 28 + v * 2.2        # panneau du bas : f'
xs = np.linspace(0, 2, 200)
# axes horizontaux des deux panneaux
line(ax, [(6, Yf(0)), (82, Yf(0))], 'fixe')
line(ax, [(6, Yd(0)), (82, Yd(0))], 'fixe')
# même abscisse x = 1 pour les deux
line(ax, [(X(1), 12), (X(1), 84)], 'fixe', dash=True)
line(ax, [(X(x), Yf(f(x))) for x in xs], 'sujet', lw=1.4)
line(ax, [(X(x), Yd(fp(x))) for x in xs], 'varie', lw=1.4)
# tangente horizontale en x = 1 : pente nulle
line(ax, [(X(0.65), Yf(0)), (X(1.35), Yf(0))], 'varie', lw=1.6)
disc(ax, X(1), Yf(0), 1.6, 'resultat')
disc(ax, X(1), Yd(0), 1.6, 'resultat')
text(ax, 84.5, Yf(f(2)) - 1, r'$f$', 'sujet', 'l')
text(ax, 84.5, Yd(fp(2)) - 1, r"$f\,'$", 'varie', 'l')
text(ax, 28, 81, 'touche l’axe', 'sujet', 's')
text(ax, 28, 77.5, 'sans traverser', 'sujet', 's')
text(ax, X(1), 56, 'pente nulle', 'varie', 's')
text(ax, X(1) + 2, 14.5, r"$f\,'$ s’annule ici", 'varie', 's', ha='left')
text(ax, X(1), 8, r'$x=1$', 'fixe', 's')
save(fig, '62-139')
