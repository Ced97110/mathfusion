import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
s, ox, oy = 7.0, 8, 8
for i in range(8):
    for j in range(8):
        disc(ax, ox + i * s, oy + j * s, 0.5, 'fixe')
arrow(ax, (ox, oy), (ox + 4 * s, oy + 6 * s), 'sujet', lw=1.5)
arrow(ax, (ox, oy), (ox + 6 * s, oy + 4 * s), 'autre', lw=1.5)
disc(ax, ox + 4 * s, oy + 6 * s, 1.2, 'sujet')
disc(ax, ox + 6 * s, oy + 4 * s, 1.2, 'autre')
text(ax, ox + 4 * s - 8, oy + 6 * s + 4, r'$f_1=(4,\,6)$', 'sujet', 'm')
text(ax, ox + 6 * s + 8, oy + 4 * s - 4, r'$f_2=(6,\,4)$', 'autre', 'm')
text(ax, 73, 14, 'deux directions', 'fixe', 's')
text(ax, 73, 9, 'différentes', 'fixe', 's')
save(fig, '59-002')
