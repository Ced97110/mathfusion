import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 80, r'Application de ℚ[$x$] vers ℝ', 'sujet', 's')
rows = [(64, 'fixe', 'fractions', 'fixe', 'inchangées', 'fixe'),
        (46, 'sujet', r'$x$', 'varie', r'$\sqrt{2}$', 'varie'),
        (28, 'sujet', r'$x^2$', 'resultat', r'$2$', 'resultat'),
        (10, 'sujet', r'$x^3$', 'resultat', r'$2\sqrt{2}$', 'resultat')]
for y, r1, a, r2, b, ra in rows:
    box(ax, 4, y, 28, 10, r1, label=a, size='m')
    box(ax, 56, y, 28, 10, r2, label=b, size='m')
    arrow(ax, (32, y + 5), (56, y + 5), ra)
text(ax, 44, 54.6, 'choix libre', 'varie', 's')
text(ax, 44, 36.6, 'imposé', 'resultat', 's')
text(ax, 44, 18.6, 'imposé', 'resultat', 's')
text(ax, 44, 72.6, 'laissées', 'fixe', 's')
assert abs((2 ** 0.5) ** 3 - 2 * 2 ** 0.5) < 1e-12
save(fig, '54-281')
