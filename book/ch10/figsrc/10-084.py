import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def panel(x0, title, ecarts, total, role):
    text(ax, x0 + 17, 56, title, 'encre', 's')
    base = 32
    line(ax, [(x0, base), (x0 + 36, base)], 'fixe')
    for i, e in enumerate(ecarts):
        x = x0 + 3 + 9 * i
        box(ax, x, base if e > 0 else base + e * 3, 5, abs(e) * 3, 'varie', r=0.3)
        text(ax, x + 2.5, base + e * 3 + (2.2 if e > 0 else -2.2), ('+%d' if e > 0 else '−%d') % abs(e), 'varie', 's')
    text(ax, x0 + 17, 8, total, role, 'm', weight='bold')
panel(4, 'tous du même signe', [4, 4, 4, 4], 'total +16', 'varie')
panel(48, 'signes mêlés', [2, -3, 3, -2], 'total 0', 'resultat')
save(fig, '10-084')
