import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 6
def panel(ox, oy):
    line(ax, [(ox, oy), (ox + 6.3 * u, oy)], 'fixe', lw=0.7); line(ax, [(ox, oy), (ox, oy + 3.4 * u)], 'fixe', lw=0.7)
    return lambda a, b: (ox + a * u, oy + b * u)
L = panel(5, 10); R = panel(47, 10)
text(ax, 44, 52, 'P (2 ; 1) et Q (5 ; 2)', 'encre', 's')
# m = 1 : two parallel lines x' = x - y
text(ax, 22, 46, 'm = 1', 'sujet', 's', weight='bold')
line(ax, [L(1, 0), L(4, 3)], 'sujet', lw=1.3); line(ax, [L(3, 0), L(6, 3)], 'autre', lw=1.3)
text(ax, L(4, 3)[0] - 1, 31.5, 'x′ = 1', 'sujet', 's'); text(ax, L(6, 3)[0] + 1, 31.5, 'x′ = 3', 'autre', 's')
# m = 3 : one line through both points
text(ax, 66, 46, 'm = 3', 'limite', 's', weight='bold')
line(ax, [R(0, 1 / 3), R(6, 7 / 3)], 'limite', lw=1.3)
text(ax, 66, 34, 'x′ = −1/3 pour les deux', 'limite', 's')
for P_, nm, r, pm in ((L, 'P', 'sujet', (2, 1)), (L, 'Q', 'autre', (5, 2)), (R, 'P', 'sujet', (2, 1)), (R, 'Q', 'autre', (5, 2))):
    x, y = P_(*pm); disc(ax, x, y, 1.3, r); text(ax, x + 2.3, y - 2.6, nm, r, 's')
text(ax, 22, 4, 'valeurs différentes', 'resultat', 's')
text(ax, 66, 4, 'même valeur : m = 3 interdit', 'limite', 's')
save(fig, '70-161')
