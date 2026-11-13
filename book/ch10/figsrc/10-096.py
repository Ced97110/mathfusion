import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 6
text(ax, 44, 54, r'$3(x+2)=3x+6$', 'encre', 'l')
box(ax, 14, 14, 36, 3 * u, 'sujet', label=r'$3x$', size='l', dash=True)
box(ax, 50, 14, 2 * u, 3 * u, 'varie', label='6', size='l')
brace(ax, 14, 50, 12, 'sujet', r'$x$', down=True); brace(ax, 50, 62, 12, 'varie', '2', down=True)
brace(ax, 14, 62, 34, 'fixe', r'$x+2$', down=False)
text(ax, 8, 23, '3', 'fixe', 'l')
save(fig, '10-096')
