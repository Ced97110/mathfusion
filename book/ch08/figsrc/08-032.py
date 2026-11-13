import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 56, r'$2{,}35$', 'encre', 'xl', weight='bold')
box(ax, 3, 6, 38, 40, 'sujet')
box(ax, 47, 6, 38, 40, 'autre')
text(ax, 22, 40, 'dit la valeur', 'sujet', 'm', weight='bold')
text(ax, 22, 32, 'deux et', 'sujet', 's')
text(ax, 22, 27.5, 'trente-cinq centièmes', 'sujet', 's')
for i in range(2): ax.add_patch(Rectangle((7 + i * 11, 9), 10, 10, ec=COL['sujet'], fc=COL['sujet'], lw=0.6, zorder=2))
for c in range(10):
    for r in range(10):
        k = c * 10 + (9 - r)
        ax.add_patch(Rectangle((29 + c * 0.9, 9 + r * 0.9), 0.9, 0.9, ec='white', fc=COL['sujet'] if k < 35 else FILL['fixe'], lw=0.2, zorder=2))
text(ax, 66, 40, 'dit l’écriture', 'autre', 'm', weight='bold')
text(ax, 66, 32, 'deux virgule', 'autre', 's')
text(ax, 66, 27.5, 'trente-cinq', 'autre', 's')
for i, ch in enumerate(['2', ',', '3', '5']):
    text(ax, 55 + i * 7, 14, ch, 'autre', 'l', weight='bold')
arrow(ax, (38, 52), (28, 47.5), 'sujet', lw=0.9)
arrow(ax, (50, 52), (60, 47.5), 'autre', lw=0.9)
save(fig, '08-032')
