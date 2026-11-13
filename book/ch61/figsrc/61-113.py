import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
Q = r'$\mathbb{Q}$'
for y, role, gens, lab in [(30, 'sujet', [r'$\sqrt{2}$'], r'$\mathbb{Q}(\sqrt{2})$'), (8, 'autre', [r'$\sqrt{2}$', r'$\sqrt{3}$'], r'$\mathbb{Q}(\sqrt{2},\sqrt{3})$')]:
    box(ax, 2, y, 14, 12, 'fixe', label=Q, size='l')
    x = 24
    for g in gens:
        text(ax, x - 4, y + 6, '+', 'encre', 'l'); box(ax, x, y + 1, 12, 10, 'varie', label=g, size='m'); x += 20
    arrow(ax, (x - 6, y + 6), (x + 2, y + 6), 'encre')
    box(ax, x + 3, y, 88 - x - 5, 12, role, label=lab, size='s')
text(ax, 44, 46, '1 générateur', 'sujet', 'm', weight='bold'); text(ax, 44, 24.5, '2 générateurs', 'autre', 'm', weight='bold')
save(fig, '61-113')
