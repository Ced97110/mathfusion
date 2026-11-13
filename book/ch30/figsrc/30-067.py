import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(70)
Y0, S = 36, 4.5
X = lambda d: 14 + d / 180 * 60
cot = lambda d: 1 / math.tan(math.radians(d))
line(ax, [(6, Y0), (82, Y0)], 'fixe')
for d in (0, 180):
    line(ax, [(X(d), 8), (X(d), 64)], 'fixe', dash=True)
line(ax, [(X(12 + 156 * i / 60), Y0 + S * cot(12 + 156 * i / 60)) for i in range(61)], 'sujet', lw=1.4)
disc(ax, X(90), Y0, 1.4, 'resultat')
text(ax, X(90) + 3, Y0 + 6, r'0 en $\pi/2$', 'resultat', 's', ha='left')
text(ax, X(90), 30, r'$\pi/2$', 'encre', 's')
text(ax, X(0), 4, '$x=0$', 'encre', 's'); text(ax, X(180), 4, r'$x=\pi$', 'encre', 's')
text(ax, 21, 61, r'$+\infty$', 'sujet', 's'); text(ax, 68, 10, r'$-\infty$', 'sujet', 's')
text(ax, 33, 59, r'$\cos x>0$', 'encre', 's'); text(ax, 55, 13, r'$\cos x<0$', 'encre', 's')
text(ax, 44, 68, 'sin x > 0 entre 0 et π', 'encre', 's')
save(fig, '30-067')
