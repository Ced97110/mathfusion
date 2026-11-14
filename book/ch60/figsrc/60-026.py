import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = lambda v: 8 + v * 5.8
def ruler(y):
    line(ax, [(f(0), y), (f(12), y)], 'fixe', lw=0.8)
    for v in range(13):
        ax.plot([f(v), f(v)], [y - 1, y + 1], color=COL['fixe'], lw=0.7, zorder=1.5)
    for v in (0, 6, 12): text(ax, f(v), y - 4.5, str(v), 'fixe', 's')
text(ax, 4, 56, 'horloge, heure 1 :\n12 additions pour revenir à 0', 'sujet', 's', ha='left')
ruler(42); disc(ax, f(12), 42, 1.9, 'resultat')
line(ax, [(f(0), 42), (f(12), 42)], 'sujet', lw=2.6)
text(ax, 4, 28, 'grille, toute case :\n6 additions → (0, 0)', 'autre', 's', ha='left')
ruler(14); line(ax, [(f(0), 14), (f(6), 14)], 'autre', lw=2.6); disc(ax, f(6), 14, 1.9, 'resultat')
text(ax, f(12), 20, '12 : jamais', 'limite', 's')
save(fig, '60-026')
