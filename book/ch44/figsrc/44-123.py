import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
def grid(x0, y0, cols, rows, c, k, label, sub):
    for i in range(cols * rows):
        r, q = divmod(i, cols)
        good = i < k
        ax.add_patch(Rectangle((x0 + q * c, y0 + (rows - 1 - r) * c), c * 0.86, c * 0.86,
                     ec=COL['resultat' if good else 'fixe'], fc=FILL['resultat' if good else 'fixe'], lw=0.4, zorder=2))
    text(ax, x0 + cols * c / 2, 64, label, 'encre', 'm')
    text(ax, x0 + cols * c / 2, 6, sub, 'resultat', 's')
grid(4, 24, 9, 3, 3.0, 6, r'$n=3$', '6 sur 27')
grid(40, 12, 16, 16, 2.9, 24, r'$n=4$', '24 sur 256')
text(ax, 2, 3, '', 'encre', 's')
save(fig, '44-123')
