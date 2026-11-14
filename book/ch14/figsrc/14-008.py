import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for cx, b, res, prod in [(22, '2', '8', r'$2\times2\times2$'), (66, '5', '125', r'$5\times5\times5$')]:
    text(ax, cx - 2, 40, b, 'sujet', 'xl', weight='bold')
    text(ax, cx + 3, 44, '3', 'fixe', 'l')
    arrow(ax, (cx - 2, 28), (cx - 2, 34.5), 'sujet')
    text(ax, cx - 2, 24, 'base', 'sujet', 'm')
    text(ax, cx, 13, prod, 'fixe', 's')
    text(ax, cx, 6, '= ' + res, 'resultat', 'm', weight='bold')
text(ax, 44, 50, 'même exposant 3', 'fixe', 's')
line(ax, [(44, 5), (44, 30)], 'fixe', dash=True)
save(fig, '14-008')
