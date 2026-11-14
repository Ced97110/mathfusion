import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(cx, cy, R, n=12):
    return [(cx + R * math.cos(math.radians(90 - 360 / n * k)), cy + R * math.sin(math.radians(90 - 360 / n * k))) for k in range(n)]

fig, ax = canvas(60)
for p in ring(22, 31, 15): disc(ax, p[0], p[1], 2.8, 'sujet')
text(ax, 22, 31, r'$G$', 'sujet', 'l')
text(ax, 22, 8, '12 éléments', 'sujet', 'm')
arrow(ax, (39, 36), (50, 42), 'varie')
text(ax, 67, 43, r'$|G| = 12$', 'sujet', 'xl')
text(ax, 65, 31, 'les barres lisent :', 'fixe', 's')
text(ax, 65, 26, "nombre d'éléments de G", 'sujet', 's')
arrow(ax, (65, 23), (65, 17), 'varie')
box(ax, 50, 8, 30, 8, 'resultat', label='ordre du groupe', size='s')
save(fig, '50-001')
