import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
xs = [3, 36, 69]
for x, h in zip(xs, ['fraction', 'décimal', 'pourcentage']):
    text(ax, x + 8, 55, h, 'fixe', 's')
rows = [(34, r'$\frac{3}{5}$', '0,6', '60 %', '3 ÷ 5', 'reste 0 : on s\'arrête', 'resultat'),
        (10, r'$\frac{1}{3}$', '0,333', '33,3 %', '1 ÷ 3', 'jamais 0 : on choisit', 'fixe')]
for y, a, b, c, d, note, role in rows:
    box(ax, xs[0], y, 16, 12, 'sujet', label=a)
    box(ax, xs[1], y, 16, 12, 'varie', label=b)
    box(ax, xs[2], y, 16, 12, 'resultat', label=c)
    arrow(ax, (20, y + 6), (35, y + 6), 'varie')
    arrow(ax, (53, y + 6), (68, y + 6), 'varie')
    text(ax, 27.5, y + 9.5, d, 'varie', 's')
    text(ax, 60.5, y + 9.5, '2 rangs', 'varie', 's')
    text(ax, 44, y - 3.5, note, role, 's')
save(fig, '09-078')
