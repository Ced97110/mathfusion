import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
text(ax, 22, 53, '16 polynômes de degré 4', 'encre', 's')
roles = {3: 'resultat', 9: 'resultat', 15: 'resultat', 5: 'limite'}
for i in range(16):
    r, c = divmod(i, 4)
    box(ax, 4 + 9 * c, 42 - 9 * r - 1, 9, 9, roles.get(i, 'fixe'), lw=0.8, r=0.5)
items = [(44, 'resultat', r"$x^4+x+1$"), (37, 'resultat', r"$x^4+x^3+1$"), (30, 'resultat', r"$x^4+x^3+x^2+x+1$")]
for y, role, s in items:
    box(ax, 44, y - 2.5, 5, 5, role, r=0.5); text(ax, 52, y, s, role, 's', ha='left')
box(ax, 44, 18.5, 5, 5, 'limite', r=0.5)
text(ax, 52, 24, r"$x^4+x^2+1$", 'limite', 's', ha='left')
text(ax, 52, 18.5, r"$=(x^2+x+1)^2$", 'limite', 's', ha='left')
box(ax, 44, 6.5, 5, 5, 'fixe', r=0.5); text(ax, 52, 9, '12 autres : se coupent', 'fixe', 's', ha='left')
save(fig, '80-415')
