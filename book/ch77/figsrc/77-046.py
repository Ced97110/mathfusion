import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$a_L : x \mapsto ax$', 'sujet', 'l', weight='bold')
for y, op, res in ((38, '$(2+i)_L$', '$(2+i)x$'), (22, '$3_L$', '$3x$'), (6, '$i_L$', '$ix$')):
    box(ax, 4, y, 12, 10, 'sujet', label='$x$')
    arrow(ax, (17, y + 5), (59, y + 5), 'varie'); text(ax, 38, y + 8.5, op, 'varie', 's')
    box(ax, 60, y, 24, 10, 'resultat', label=res)
save(fig, '77-046')
