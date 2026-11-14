import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def row(y, lo, val, ent, shown):
    f = numberline(ax, 6, 70, y, lo, lo + 4, labels=True, arrow_right=True)
    arrow(ax, (f(val), y + 9), (f(ent), y + 2.5), 'resultat', lw=1.2, curve=0.0)
    disc(ax, f(val), y + 10.5, 1.6, 'sujet')
    text(ax, f(val), y + 15, shown, 'sujet', 'm', weight='bold')
    text(ax, f(ent), y - 6.5, 'partie entière', 'resultat', 's')
    ax.add_patch(Circle((f(ent), y), 1.4, ec=COL['resultat'], fc=FILL['resultat'], lw=1.0, zorder=4))
row(42, 0, 2.35, 2, '2,35')
row(14, 6, 7.99, 7, '7,99')
save(fig, '08-029')
