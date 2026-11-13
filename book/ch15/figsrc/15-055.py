import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 76, '3', 'sujet', 'l'); line(ax, [(40.5, 73), (47.5, 73)], 'sujet')
text(ax, 44, 70, r'$x$', 'varie', 'l'); text(ax, 56, 73, '− 16', 'sujet', 'l')
text(ax, 15, 70, 'lettre en bas', 'varie', 's'); arrow(ax, (24.5, 70), (40.5, 70), 'varie')
box(ax, 3, 14, 39, 32, 'resultat'); box(ax, 46, 14, 39, 32, 'limite')
arrow(ax, (40, 64), (22.5, 47), 'varie'); arrow(ax, (48, 64), (65.5, 47), 'varie')
for cx, r, v in ((22.5, 'resultat', '2'), (65.5, 'limite', '0')):
    text(ax, cx, 40, rf'$x = {v}$', r, 'l')
    text(ax, cx, 32, rf'$3 \div {v} - 16$', r, 'm')
text(ax, 22.5, 22, r'$= -14{,}5$', 'resultat', 'm')
text(ax, 65.5, 22, 'impossible', 'limite', 'm')
text(ax, 44, 5, 'pas un polynôme', 'limite', 'l')
save(fig, '15-055')
