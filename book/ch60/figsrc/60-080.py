import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
def row(y, size, n, top, bot):
    text(ax, 44, y + 16, top, 'sujet', 'l')
    gw = size * 5
    for g in range(n):
        x0 = 6 + g * (gw + 5)
        box(ax, x0, y, gw, 8, 'sujet', fill=False, lw=1.0, r=0.6)
        for j in range(size):
            disc(ax, x0 + 2.5 + 5 * j, y + 4, 1.6, 'sujet')
    x1 = 6 + n * (gw + 5) - 5
    brace(ax, 6, x1, y, 'resultat', label=bot, down=True)
row(50, 3, 4, '3 | 12', '12 = 4 × 3')
row(16, 2, 3, '2 | 6', '6 = 3 × 2')
save(fig, '60-080')
