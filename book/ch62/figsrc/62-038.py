import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$x-r\mid f$', 'encre', 'xl')
# nombres
text(ax, 9, 50, r'$6=$', 'fixe', 'l')
box(ax, 18, 45, 16, 10, 'fixe', label=r'$3$')
text(ax, 38, 50, r'$\times$', 'fixe', 'l')
box(ax, 42, 45, 16, 10, 'fixe', label=r'$2$')
text(ax, 72, 50, r'3 divise 6', 'fixe', 's')
# polynômes
text(ax, 11, 26, r'$x^2-9=$', 'sujet', 'm')
box(ax, 26, 20, 26, 12, 'sujet', label=r'$x-3$')
text(ax, 56, 26, r'$\times$', 'fixe', 'l')
box(ax, 60, 20, 26, 12, 'fixe', label=r'$x+3$')
brace(ax, 26, 52, 19, 'sujet', label='divise $f$', down=True)
brace(ax, 60, 86, 19, 'fixe', label='autre polynôme', down=True)
save(fig, '62-038')
