import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
s, ox, oy = 3.4, 6, 6
P = lambda x, y: (ox + x * s, oy + y * s)
for a in range(-10, 11):
    for b in range(-10, 11):
        x, y = 4 * a + 6 * b, 6 * a + 4 * b
        if 0 <= x <= 20 and 0 <= y <= 20:
            ax.plot([P(x, y)[0]], [P(x, y)[1]], 'o', color=COL['sujet'], ms=2.2, zorder=2)
arrow(ax, P(0, 0), P(10, 10), 'sujet', lw=1.2)
arrow(ax, P(0, 0), P(2, 8), 'sujet', lw=1.2)
line(ax, [P(10, 10), P(12, 18)], 'fixe', dash=True)
line(ax, [P(2, 8), P(12, 18)], 'fixe', dash=True)
disc(ax, *P(12, 18), 1.4, 'resultat')
arrow(ax, P(10, 10), P(20, 20), 'varie', lw=1.2)
disc(ax, *P(20, 20), 1.4, 'varie')
text(ax, 47, 38, r'$(10,\,10)$', 'sujet', 's', ha='left')
text(ax, 8, 36, r'$(2,\,8)$', 'sujet', 's', ha='left')
text(ax, 44, 78, r'$(12,\,18)=3f_1$', 'resultat', 's', ha='right')
text(ax, 84, 86, r'$2\times(10,\,10)$', 'varie', 's', ha='right')
text(ax, 84, 81, r'$=(20,\,20)$', 'varie', 's', ha='right')
text(ax, 84, 14, 'points de K', 'sujet', 's', ha='right')
save(fig, '59-004')
