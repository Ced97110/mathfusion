import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 14, 38, 60, 12, 'sujet', label=r'$4\pm8$', size='l')
brace(ax, 14, 74, 52, 'sujet', 'tout le haut', down=False)
line(ax, [(14, 34), (74, 34)], 'encre', lw=1.4)
box(ax, 39, 14, 10, 12, 'varie', label=r'$4$', size='l')
arrow(ax, (44, 27.5), (44, 32.5), 'varie')
text(ax, 44, 6, r'$2a=2\times2=4$', 'varie', 's')
save(fig, '23-056')
