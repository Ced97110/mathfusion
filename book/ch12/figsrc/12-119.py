import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 8.0; x0 = 14; y0 = 8
box(ax, x0, y0, 5 * u, 4 * u, 'sujet', r=0.2)
box(ax, x0 + 5 * u, y0, 2 * u, 4 * u, 'varie', r=0.2)
text(ax, x0 + 2.5 * u, y0 + 2 * u, r'$ab$', 'sujet', 'xl'); text(ax, x0 + 6 * u, y0 + 2 * u, r'$ac$', 'varie', 'xl')
brace(ax, x0, x0 + 5 * u, y0, 'sujet', label=r'$b=5$')
brace(ax, x0 + 5 * u, x0 + 7 * u, y0, 'varie', label=r'$c=2$')
brace(ax, x0, x0 + 7 * u, y0 + 4 * u, 'fixe', label=r'$b+c=7$', down=False)
text(ax, 7, y0 + 2 * u, r'$a=4$', 'fixe', 'm')
save(fig, '12-119')
