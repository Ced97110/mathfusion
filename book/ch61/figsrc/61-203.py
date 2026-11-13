import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u, x0 = 15, 10
text(ax, 44, 71, 'a = 2 et b = 1', 'encre', 's')
def row(y, back):
    line(ax, [(x0, y), (x0 + 4 * u, y)], 'fixe')
    for v in range(5): line(ax, [(x0 + v * u, y - 1.2), (x0 + v * u, y + 1.2)], 'fixe')
    arrow(ax, (x0, y + 5), (x0 + 2 * u, y + 5), 'sujet', lw=1.4)
    if not back:
        arrow(ax, (x0 + 2 * u, y + 5), (x0 + 3 * u, y + 5), 'varie', lw=1.4)
        text(ax, x0 + u, y + 8.5, 'a', 'sujet'); text(ax, x0 + 2.5 * u, y + 8.5, 'b', 'varie')
        brace(ax, x0, x0 + 3 * u, y - 2, 'resultat', 'a + b')
    else:
        arrow(ax, (x0 + 2 * u, y + 9), (x0 + u, y + 9), 'varie', lw=1.4)
        text(ax, x0 + 0.5 * u, y + 8.5, 'a', 'sujet'); text(ax, x0 + 1.5 * u, y + 12.5, 'b', 'varie')
        brace(ax, x0, x0 + u, y - 2, 'resultat', 'a − b')
row(52, False); row(18, True)
save(fig, '61-203')
