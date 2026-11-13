import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u, y0 = 2.5, 18
for x0, k in [(6, 1), (50, 2)]:
    box(ax, x0, y0, 9, 3 * k * u, 'sujet', r=0.3); box(ax, x0 + 12, y0, 9, 5 * k * u, 'varie', r=0.3)
    text(ax, x0 + 4.5, y0 + 3 * k * u + 3, str(3 * k), 'sujet', 's'); text(ax, x0 + 16.5, y0 + 5 * k * u + 3, str(5 * k), 'varie', 's')
    text(ax, x0 + 10.5, 11, f'{3*k} ÷ {5*k} = 0,6', 'resultat', 's')
arrow(ax, (30, 30), (46, 30), 'varie')
text(ax, 38, 34, '× 2', 'varie', 's')
text(ax, 38, 11, '=', 'resultat', 'l', weight='bold')
text(ax, 44, 4, 'même rapport 3/5', 'encre', 'm')
save(fig, '09-011')
