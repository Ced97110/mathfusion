import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u, oy = 16, 14
for ox, tip, role, tt, cl, dl in [(8, (2, 1), 'varie', r'$\eta e = a e + b f$', r'$a$ = 2', r'$b$ = 1'), (54, (1, 1), 'autre', r'$\eta f = c e + d f$', r'$c$ = 1', r'$d$ = 1')]:
    L = (2 * u + 4) if ox == 8 else (u + 12)
    arrow(ax, (ox, oy), (ox + L, oy), 'fixe', lw=0.7); arrow(ax, (ox, oy), (ox, oy + u + 6), 'fixe', lw=0.7)
    line(ax, [(ox, oy), (ox + tip[0] * u, oy)], role, lw=1.6, dash=True); line(ax, [(ox + tip[0] * u, oy), (ox + tip[0] * u, oy + tip[1] * u)], role, lw=1.6, dash=True)
    arrow(ax, (ox, oy), (ox + tip[0] * u, oy + tip[1] * u), role, lw=1.3)
    text(ax, ox + tip[0] * u / 2, oy - 4, cl, role, 's'); text(ax, ox + tip[0] * u + 2.5, oy + u / 2, dl, role, 's', ha='left')
    text(ax, ox + 16, 47, tt, role, 'm')
text(ax, 46, oy, r'$e$', 'fixe', 's'); text(ax, 8, oy + u + 9, r'$f$', 'fixe', 's')
save(fig, '75-014')
