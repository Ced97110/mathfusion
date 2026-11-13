import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
cm = 5.5; po = 2.54 * cm; x0 = 4
text(ax, 2, 42, 'grande unité : po', 'sujet', 's', ha='left')
for k in range(4):
    box(ax, x0 + k * po, 28, po, 7, 'sujet', r=0.3)
text(ax, 72, 31.5, '4', 'sujet', 'xl', weight='bold')
text(ax, 2, 20, 'petite unité : cm', 'autre', 's', ha='left')
for k in range(10):
    box(ax, x0 + k * cm, 6, cm, 7, 'autre', r=0.3)
ax.add_patch(Rectangle((x0 + 10 * cm, 6), 0.16 * cm, 7, ec=COL['autre'], fc=FILL['autre'], lw=0.6, zorder=2))
text(ax, 72, 9.5, '10,16', 'autre', 'xl', weight='bold')
text(ax, 72, 41, 'petit nombre', 'sujet', 's')
text(ax, 72, 19, 'grand nombre', 'autre', 's')
save(fig, '11-012')
