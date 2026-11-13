import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
U = 24; y0 = 36
for x in (4, 30):
    ax.add_patch(Rectangle((x, y0), U, U, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
gx = 60; c = U / 10
for col in range(10):
    for r in range(10):
        k = col * 10 + r
        role = 'varie' if col < 3 else ('resultat' if col == 3 and r < 5 else 'fixe')
        fc = COL[role] if role != 'fixe' else FILL['fixe']
        ax.add_patch(Rectangle((gx + col * c, y0 + r * c), c, c, ec='white', fc=fc, lw=0.3, zorder=2))
ax.add_patch(Rectangle((gx, y0), U, U, ec=COL['fixe'], fc='none', lw=0.8, zorder=3))
text(ax, 29, 66, '2 unités', 'sujet', 's')
text(ax, 72, 66, '1 unité en 100 parts', 'fixe', 's')
text(ax, 11, 22, '2', 'sujet', 'l', weight='bold'); text(ax, 19, 22, '+', 'encre', 'l')
text(ax, 31, 22, '3/10', 'varie', 'l', weight='bold'); text(ax, 43, 22, '+', 'encre', 'l')
text(ax, 56, 22, '5/100', 'resultat', 'l', weight='bold')
text(ax, 11, 9, '=', 'encre', 'l'); text(ax, 19, 9, '2', 'sujet', 'l', weight='bold')
text(ax, 27, 9, '+', 'encre', 'l'); text(ax, 42, 9, '35/100', 'encre', 'l', weight='bold')
save(fig, '08-023')
