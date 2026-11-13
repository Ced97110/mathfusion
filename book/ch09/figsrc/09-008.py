import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u, y0 = 3.0, 12
for x0, k, step in [(6, 1, 1), (50, 2, 2)]:
    for x, h, role in [(x0, 3 * k, 'sujet'), (x0 + 12, 5 * k, 'varie')]:
        box(ax, x, y0, 10, h * u, role, r=0.3)
        for c in range(1, h):
            line(ax, [(x, y0 + c * u), (x + 10, y0 + c * u)], 'encre' if False else role, lw=0.3)
    for p in range(1, 5):
        line(ax, [(x0 + 12, y0 + p * step * u), (x0 + 22, y0 + p * step * u)], 'encre', lw=1.0)
    text(ax, x0 + 5, y0 + 3 * k * u + 3, r'$a=3$' if k == 1 else r'$2a=6$', 'sujet', 's')
    text(ax, x0 + 17, y0 + 5 * k * u + 3, r'$b=5$' if k == 1 else r'$2b=10$', 'varie', 's')
    text(ax, x0 + 11, 6, '3 parts sur 5', 'resultat', 's')
text(ax, 44, 30, '6/10 = 3/5', 'encre', 'l', weight='bold')
arrow(ax, (32, 24), (46, 24), 'varie')
text(ax, 39, 20, '× 2', 'varie', 's')
save(fig, '09-008')
