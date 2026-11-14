import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, '2{3[4(5 + 1)]}', 'sujet', 'xl', weight='bold')
box(ax, 3, 5, 82, 44, 'sujet'); text(ax, 44, 45, 'accolades { }', 'sujet', 'm')
box(ax, 9, 9, 70, 32, 'fixe'); text(ax, 44, 37, 'crochets [ ]', 'fixe', 'm')
box(ax, 15, 13, 58, 20, 'fixe'); text(ax, 44, 29, 'parenthèses ( )', 'fixe', 'm')
text(ax, 44, 20, '5 + 1', 'encre', 'l')
save(fig, '12-049')
