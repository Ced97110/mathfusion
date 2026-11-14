import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
ox, oy, sx, sy = 16, 12, 14, 0.5
P = lambda g, m: (ox + g * sx, oy + m * sy)
arrow(ax, (ox, oy), (ox + 62, oy), 'fixe'); arrow(ax, (ox, oy), (ox, oy + 62), 'fixe')
text(ax, ox + 67, oy, 'g', 'fixe', 'l'); text(ax, ox, oy + 66, 'm', 'fixe', 'l')
line(ax, [P(0, 0), P(4, 100)], 'resultat', dash=True)
line(ax, [P(0, 0), P(2, 50), P(4, 80)], 'limite', lw=1.2)
for p in [(0, 0), (2, 50), (4, 80)]: disc(ax, *P(*p), 1.6, 'sujet')
text(ax, P(0, 0)[0], oy - 5, '(0, 0)', 'sujet', 's'); text(ax, P(2, 50)[0] - 3, P(2, 50)[1] + 5, '(2, 50)', 'sujet', 's')
text(ax, P(4, 80)[0] + 6, P(4, 80)[1] - 4, '(4, 80)', 'sujet', 's')
text(ax, P(4, 100)[0], P(4, 100)[1] + 5, '(4, 100)', 'resultat', 's')
text(ax, 46, 20, '25 par gallon', 'limite', 's'); text(ax, 64, 36, '15 par gallon', 'limite', 's')
save(fig, '09-120')
