import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
xs = [3, 36, 69]
text(ax, 44, 47, 'écrire sur 100, puis réduire', 'varie', 's')
rows = [(26, '42 %', r'$\frac{42}{100}$', r'$\frac{21}{50}$', r'$\div$ 2'), (6, '25 %', r'$\frac{25}{100}$', r'$\frac{1}{4}$', r'$\div$ 25')]
for y, a, b, c, d in rows:
    box(ax, xs[0], y, 16, 14, 'sujet', label=a)
    box(ax, xs[1], y, 16, 14, 'fixe', label=b)
    box(ax, xs[2], y, 16, 14, 'resultat', label=c)
    arrow(ax, (20, y + 7), (35, y + 7), 'varie')
    arrow(ax, (53, y + 7), (68, y + 7), 'varie')
    text(ax, 60.5, y + 11, d, 'varie', 's')
save(fig, '09-079')
