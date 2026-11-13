import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
for x, w, role, lab, sub in [(5, 26, 'sujet', 'deg', '« degré de »'), (35, 18, 'fixe', r'$f$', 'le polynôme'), (57, 26, 'resultat', r'$=3$', 'la position')]:
    box(ax, x, 64, w, 12, role, label=lab, size='xl')
    text(ax, x + w / 2, 59, sub, role, 's')
text(ax, 44, 46, r'$f=2-x+3x^3$', 'fixe', 'm')
y0, u, w = 22, 4, 7
coef = [2, -1, 0, 3]
X = lambda i: 20 + 16 * i
line(ax, [(8, y0), (80, y0)], 'fixe')
for i, a in enumerate(coef):
    role = 'resultat' if i == 3 else 'fixe'
    if a == 0:
        line(ax, [(X(i) - w / 2, y0), (X(i) + w / 2, y0)], 'fixe', lw=1.2)
    else:
        h = a * u
        ax.add_patch(Rectangle((X(i) - w / 2, min(y0, y0 + h)), w, abs(h), ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, X(i), 9, str(i), role, 's')
arrow(ax, (70, 55), (X(3), y0 + 3 * u + 3), 'resultat')
save(fig, '54-123')
