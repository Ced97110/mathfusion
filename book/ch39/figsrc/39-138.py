import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ox, oy, u = 8, 37, 4.2
P = lambda a, b: (ox + a * u, oy + b * u)
arrow(ax, (ox, oy), (ox + 4.8 * u, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 4.8 * u), (ox, oy + 4.8 * u), 'fixe', lw=0.6)
arrow(ax, (ox, oy), P(3, 4), 'sujet', lw=1.1)
arrow(ax, (ox, oy), P(3, -4), 'varie', lw=1.1)
line(ax, [P(3, 4), P(3, -4)], 'fixe', dash=True, lw=0.7)
disc(ax, *P(3, 4), 1.2, 'sujet'); disc(ax, *P(3, -4), 1.2, 'varie')
text(ax, P(3, 4)[0] + 2, P(3, 4)[1] + 3.5, r'$3+4i$', 'sujet', 's', ha='left')
text(ax, P(3, -4)[0] + 2, P(3, -4)[1] - 3.5, r'$3-4i$', 'varie', 's', ha='left')
text(ax, ox + 14, oy + 5, 'signe de\nla partie imaginaire', 'fixe', 's', ha='left') if False else None
X = 38
text(ax, X, 67, r'$(3+4i)(3-4i)$', 'sujet', ha='left')
text(ax, X, 58, r'$=9+16=25$', 'resultat', ha='left')
text(ax, X, 46, r'$\dfrac{1}{3+4i}=\dfrac{3-4i}{25}$', 'resultat', ha='left')
text(ax, X, 33, r'$\dfrac{1}{1+i}=\dfrac{1-i}{2}$', 'autre', ha='left')
text(ax, X, 21, r'tout $a+bi\neq 0$ :', 'fixe', 's', ha='left')
text(ax, X, 14, r'$\dfrac{a-bi}{a^2+b^2}$', 'fixe', ha='left')
save(fig, '39-138')
