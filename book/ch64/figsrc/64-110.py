import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
R = 9.5
def pent(cx, cy):
    return [(cx + R * math.cos(math.radians(90 - 72 * k)), cy + R * math.sin(math.radians(90 - 72 * k))) for k in range(5)]
def draw(cx, perm, role, labels):
    P = pent(cx, 28)
    for i in range(1, 6):
        if labels: disc(ax, P[i - 1][0], P[i - 1][1], 2.4, 'fixe', label=str(i), size='s')
        else: disc(ax, P[i - 1][0], P[i - 1][1], 1.2, 'fixe')
    for i, j in perm.items():
        (x0, y0), (x1, y1) = P[i - 1], P[j - 1]
        d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
        s = 2.8 if labels else 1.8
        arrow(ax, (x0 + ux * s, y0 + uy * s), (x1 - ux * s, y1 - uy * s), role, lw=1.0)
alpha = {1: 2, 2: 3, 3: 4, 4: 5, 5: 1}
alpha1 = {1: 2, 2: 4, 3: 1, 4: 5, 5: 3}   # beta alpha beta^-1, calculé
alpha2 = {1: 3, 3: 4, 4: 1}               # alpha1 alpha^-1, calculé
draw(14, alpha, 'sujet', True); draw(44, alpha1, 'varie', False); draw(74, alpha2, 'resultat', True)
text(ax, 14, 47, r'$\alpha$', 'sujet', 'm')
text(ax, 44, 47, r'$\alpha_1=\beta\alpha\beta^{-1}$', 'varie', 's')
text(ax, 74, 47, r'$\alpha_2=\alpha_1\alpha^{-1}$', 'resultat', 's')
text(ax, 14, 14, '5 objets bougent', 'sujet', 's')
text(ax, 44, 14, '5 objets bougent', 'varie', 's')
text(ax, 74, 14, '3 objets bougent', 'resultat', 's')
text(ax, 74, 6, r'$(1\,3\,4)$ : un 3-cycle', 'resultat', 's')
save(fig, '64-110')
