import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cw, rh = 13, 12
x0, y0 = 20, 18
for j, c in enumerate(['colonne 1', 'colonne 2']):
    text(ax, x0 + cw * (j + 0.5), y0 + 2 * rh + 9, c, 'fixe', 's')
    line(ax, [(x0 + cw * j + 1, y0 + 2 * rh + 5), (x0 + cw * (j + 1) - 1, y0 + 2 * rh + 5)], 'fixe', lw=1.2)
for i, (role, letters, lab, out) in enumerate([('sujet', 'ab', 'ligne 1', r'$ax + by$'), ('autre', 'cd', 'ligne 2', r'$cx + dy$')]):
    y = y0 + (1 - i) * rh
    text(ax, 10, y + rh / 2, lab, 'fixe', 's')
    for j, l in enumerate(letters):
        box(ax, x0 + cw * j, y, cw, rh, role, label=r'$%s$' % l, size='l', r=0.4)
    arrow(ax, (x0 + 2 * cw + 0.8, y + rh / 2), (56, y + rh / 2), role)
    box(ax, 57, y + 1.5, 29, rh - 3, role, label=out)
text(ax, 71, y0 + 2 * rh + 9, r'$(x,\ y)$ devient :', 'encre', 's')
ax.add_patch(Rectangle((x0 - 0.6, y0 + rh - 0.6), cw + 1.2, rh + 1.2, fill=False, ec=COL['varie'], lw=1.8, zorder=6))
text(ax, 44, 8, r'$a$ : ligne 1, colonne 1', 'varie', 's')
save(fig, '44-192')
