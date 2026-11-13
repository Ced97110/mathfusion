import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
for k in range(3):
    ox = 6 + k * 28; oy = 12
    role = 'sujet' if k == 1 else 'fixe'
    poly(ax, [(ox, oy), (ox + 18, oy), (ox + 24, oy + 14), (ox + 6, oy + 14)], role)
    text(ax, ox + 12, oy - 5, rf'$P_{k+1}$', role, 'm')
    if k == 1:
        arrow(ax, (ox + 3, oy + 2), (ox + 17, oy + 2), 'sujet', lw=1.2)
        arrow(ax, (ox + 3, oy + 2), (ox + 8, oy + 12), 'autre', lw=1.2)
        text(ax, ox + 11, oy + 6, r'$e_2$', 'sujet', 's')
        text(ax, ox + 15, oy + 10, r'$f_2$', 'autre', 's')
text(ax, 44, 43, 'le plan de la paire 2', 'sujet', 'm')
text(ax, 44, 36, 'un plan par paire', 'fixe', 's')
save(fig, '75-052')
