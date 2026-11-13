import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [20, 44, 68]; base = 18; unit = 12
text(ax, 44, 58, r'$x(x-1)$ sur ℤ/3ℤ, degré 2 < 3', 'sujet', 'm')
line(ax, [(8, base), (80, base)], 'fixe')
for i, x in enumerate(xs):
    v = (i * (i - 1)) % 3
    if v > 0:
        box(ax, x - 5, base, 10, v * unit, 'varie')
        text(ax, x, base + v * unit + 4, str(v), 'varie', 'l', weight='bold')
        text(ax, x, base - 9, 'pas nulle', 'varie', 's')
    else:
        disc(ax, x, base, 2.2, 'sujet')
        text(ax, x, base + 5, str(v), 'sujet', 'l', weight='bold')
        text(ax, x, base - 9, 'racine', 'sujet', 's')
    text(ax, x, base - 4, f'en {i}', 'encre', 's')
save(fig, '55-059')
