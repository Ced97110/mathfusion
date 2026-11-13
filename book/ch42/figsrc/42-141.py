import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 24, 51, r'$A \cup A$', 'encre', 'l')
ax.add_patch(Circle((24, 30), 16, ec=COL['autre'], fc='none', lw=1.0, ls='--', zorder=3))
ax.add_patch(Circle((24, 30), 12.5, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=2))
text(ax, 24, 39, r'$A$', 'sujet', 'm')
text(ax, 24, 11.5, r'$A$', 'autre', 'm')
for dx, n in [(-8, '2'), (0, '4'), (8, '6')]:
    text(ax, 24 + dx, 30, n, 'sujet', 'l')
text(ax, 45, 30, '=', 'resultat', 'l', weight='bold')
ax.add_patch(Circle((66, 30), 12.5, ec=COL['resultat'], fc=FILL['resultat'], lw=1.0, zorder=2))
text(ax, 66, 51, r'$A$', 'resultat', 'l')
for dx, n in [(-8, '2'), (0, '4'), (8, '6')]:
    text(ax, 66 + dx, 30, n, 'resultat', 'l')
text(ax, 44, 4.5, 'chaque nombre une seule fois', 'encre', 's')
save(fig, '42-141')
