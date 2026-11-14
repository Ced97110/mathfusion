import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
for cx, role, centre, nb in [(22, 'sujet', '000', ['100', '010', '001']), (66, 'varie', '111', ['011', '101', '110'])]:
    cy = 24
    ax.add_patch(Circle((cx, cy), 21, ec=COL[role], fc='none', lw=0.9, ls='--', zorder=1))
    for k, w in enumerate(nb):
        a = math.radians(90 + 120 * k)
        x, y = cx + 13 * math.cos(a), cy + 13 * math.sin(a)
        line(ax, [(cx + 6.2 * math.cos(a), cy + 6.2 * math.sin(a)), (x - 4.6 * math.cos(a), y - 4.6 * math.sin(a))], role)
        disc(ax, x, y, 4.6, role, label=w, size='s')
    disc(ax, cx, cy, 5.2, role, label=centre, size='s')
    ax.add_patch(Circle((cx, cy), 6.2, ec=COL['encre'], fc='none', lw=1.3, zorder=3))
    text(ax, cx, 50, f'boule autour de {centre}', role, 's')
save(fig, '68-016')
