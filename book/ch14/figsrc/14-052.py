import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
c = 5.0; x0, y0 = 4, 12
def cell(i, j, role):
    ax.add_patch(Rectangle((x0 + i * c, y0 + j * c), c, c, ec=COL[role], fc=FILL[role], lw=0.4, zorder=2))
for i in range(7):
    for j in range(7):
        if i < 3 and j < 3: cell(i, j, 'sujet')
        elif i >= 3 and j >= 3: cell(i, j, 'autre')
        else: cell(i, j, 'limite')
text(ax, x0 + 1.5 * c, y0 + 1.5 * c, '9', 'sujet', 'm', weight='bold')
text(ax, x0 + 5 * c, y0 + 5 * c, '16', 'autre', 'm', weight='bold')
text(ax, x0 + 5 * c, y0 + 1.5 * c, '12', 'limite', 'm', weight='bold')
text(ax, x0 + 1.5 * c, y0 + 5 * c, '12', 'limite', 'm', weight='bold')
brace(ax, x0, x0 + 3 * c, y0, 'sujet', '3')
brace(ax, x0 + 3 * c, x0 + 7 * c, y0, 'autre', '4')
text(ax, 62, 46, r'$(3+4)^2=49$', 'sujet', 'm')
text(ax, 62, 33, r'$3^2+4^2=25$', 'autre', 'm')
text(ax, 62, 20, 'il manque 24', 'limite', 'm')
save(fig, '14-052')
