import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, 'deux opérations sur l’horloge', 'encre', 'm')
for y, a, b, res, role in [(70, r'$9+7=16$', r'$16=12+4$', '4', 'sujet'), (48, r'$9\times7=63$', r'$63=5\times12+3$', '3', 'varie')]:
    box(ax, 2, y - 6, 28, 12, role, label=a, size='m')
    arrow(ax, (30.5, y), (36.5, y), role)
    box(ax, 37, y - 6, 34, 12, 'fixe', label=b, size='m')
    arrow(ax, (71.5, y), (76.5, y), role)
    disc(ax, 82, y, 4.5, 'resultat', label=res, size='m')
f = numberline(ax, 6, 76, 24, 0, 36, 1, True, 'fixe', False, every=12)
for v in (0, 12, 24, 36): disc(ax, f(v), 24, 1.6, 'sujet')
text(ax, 44, 10, 'bloc de 0 : multiples de 12', 'sujet', 's')
save(fig, '43-150')
