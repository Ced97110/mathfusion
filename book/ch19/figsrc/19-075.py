import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for x0, role, ti, bot, res in [(3, 'limite', 'ordre différent', '2 − 6 = −4', '= −2 : faux'),
                               (47, 'resultat', 'même ordre', '6 − 2 = 4', '= 2 : juste')]:
    box(ax, x0, 4, 38, 64, role)
    c = x0 + 19
    text(ax, c, 61, ti, role, 'm', weight='bold')
    text(ax, c, 47, '13 − 5 = 8', role, 'm')
    line(ax, [(c - 14, 39), (c + 14, 39)], role, lw=1.2)
    text(ax, c, 31, bot, role, 'm')
    text(ax, c, 15, res, role, 'l', weight='bold')
save(fig, '19-075')
