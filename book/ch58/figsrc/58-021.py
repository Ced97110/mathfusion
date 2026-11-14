import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# (5, 4) = (5, 0) + (0, 4) : riz pur sur l'axe horizontal, lentilles pur sur l'axe vertical
x0, y0, u = 16, 9, 8.0
P = lambda a, b: (x0 + a * u, y0 + b * u)
for a in range(0, 7):
    line(ax, [P(a, 0), P(a, 5)], 'fixe', lw=0.25)
for b in range(0, 6):
    line(ax, [P(0, b), P(6, b)], 'fixe', lw=0.25)
line(ax, [P(5, 0), P(5, 4)], 'sujet', lw=1.0, dash=True)
line(ax, [P(0, 4), P(5, 4)], 'autre', lw=1.0, dash=True)
arrow(ax, P(0, 0), P(5, 0), 'sujet', lw=1.8)
arrow(ax, P(0, 0), P(0, 4), 'autre', lw=1.8)
disc(ax, *P(5, 0), 1.5, 'sujet'); disc(ax, *P(0, 4), 1.5, 'autre'); disc(ax, *P(5, 4), 1.7, 'resultat')
text(ax, P(5, 0)[0], P(5, 0)[1] - 4.5, '(5, 0)', 'sujet', 's', weight='bold')
text(ax, P(0, 4)[0] - 3, P(0, 4)[1], '(0, 4)', 'autre', 's', weight='bold', ha='right')
text(ax, P(5, 4)[0] + 3.5, P(5, 4)[1] + 1.5, '(5, 4)', 'resultat', 's', weight='bold', ha='left')
text(ax, 36, 13.5, 'riz pur', 'sujet', 's', weight='bold')
text(ax, 19, 26, 'lentilles pur', 'autre', 's', ha='left', weight='bold')
text(ax, 44, 65, r'$(5,\ 4) = (5,\ 0) + (0,\ 4)$', 'encre', 'l', weight='bold')
text(ax, 44, 58.5, r'pour tout stock : $(x,\ y) = (x,\ 0) + (0,\ y)$', 'resultat', 's', weight='bold')
save(fig, '58-021')
