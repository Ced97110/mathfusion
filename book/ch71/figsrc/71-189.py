import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, s = 22, 12, 15
arrow(ax, (ox - 6, oy), (ox + 3 * s + 2, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 5), (ox, oy + 3 * s), 'fixe', lw=0.8)
for i in range(3):
    text(ax, ox + i * s, oy - 4.5, str(i), 'fixe', 's'); text(ax, ox - 4, oy + i * s, str(i), 'fixe', 's')
text(ax, ox + 3 * s + 3, oy - 4.5, '$p$', 'fixe', 's'); text(ax, ox - 4, oy + 3 * s + 2, '$q$', 'fixe', 's')
for p in range(3):
    for q in range(3):
        if p + q <= 2: disc(ax, ox + p * s, oy + q * s, 2.2, 'sujet')
        else: disc(ax, ox + p * s, oy + q * s, 2.2, 'limite', fill=False)
line(ax, [(ox, oy + 2 * s), (ox + 2 * s, oy)], 'varie', dash=True)
text(ax, ox + s + 8, oy + s + 8, '$p+q\\leq 2$', 'varie', 's')
text(ax, 72, 40, 'six couples', 'sujet', 'm')
text(ax, 72, 34, 'permis', 'sujet', 's')
text(ax, 72, 20, 'hors liste', 'limite', 's')
save(fig, '71-189')
