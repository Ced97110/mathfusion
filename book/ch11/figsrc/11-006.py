import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cm = 7.0; po = 2.54 * cm; x0 = 8
box(ax, x0, 46, 4 * po, 6, 'sujet', r=0.3)
text(ax, x0 + 2 * po, 56, 'ruban : 4 po', 'sujet', 'm')
for k in range(4):
    box(ax, x0 + k * po, 30, po, 7, 'varie', r=0.3, label=str(k + 1), size='s')
brace(ax, x0, x0 + 4 * po, 28, 'varie', label="4 poses d'1 po")
for k in range(10):
    box(ax, x0 + k * cm, 10, cm, 7, 'autre', r=0.3)
ax.add_patch(Rectangle((x0 + 10 * cm, 10), 0.16 * cm, 7, ec=COL['fixe'], fc=FILL['fixe'], lw=0.6, zorder=2))
brace(ax, x0, x0 + 10 * cm, 8, 'autre', label="10 poses d'1 cm")
text(ax, x0 + 10 * cm + 1, 20.5, 'reste 0,16', 'fixe', 's')
save(fig, '11-006')
