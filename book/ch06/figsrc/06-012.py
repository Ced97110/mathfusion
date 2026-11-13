import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 14, 49, '3', 'varie', 'l')
line(ax, [(8, 44.5), (20, 44.5)], 'encre', lw=1.2)
text(ax, 14, 40, '4', 'fixe', 'l')
arrow(ax, (24, 44.5), (36, 44.5), 'fixe')
text(ax, 58, 44.5, '« trois quarts »', 'encre')
for j in range(4):
    box(ax, 8 + j * 18, 14, 18, 10, 'varie' if j < 3 else 'fixe', r=0.3)
brace(ax, 8, 62, 24, 'varie', r'$a$ = 3 parts prises', down=False, size='m')
brace(ax, 8, 80, 14, 'fixe', r'$b$ = 4 parts égales', size='m')
save(fig, '06-012')
