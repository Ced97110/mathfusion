import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$9x+3(4-3x)=12$', 'sujet', 'l')
data = [('2', r'$18+3\times(-2)$'), ('0', r'$0+3\times 4$'), ('-5', r'$-45+3\times 19$')]
for i, (v, calc) in enumerate(data):
    y = 50 - i * 14
    box(ax, 4, y, 20, 9, 'varie', label=r'$x=%s$' % v)
    arrow(ax, (25, y + 4.5), (30, y + 4.5), 'fixe')
    text(ax, 46, y + 4.5, calc, 'encre', 'm')
    box(ax, 66, y, 18, 9, 'resultat', label='12', weight='bold')
    arrow(ax, (59, y + 4.5), (65.5, y + 4.5), 'fixe')
text(ax, 44, 13, r'$9x+12-9x=12$', 'resultat', 'm')
text(ax, 44, 6.5, 'les termes en x s’annulent', 'fixe', 's')
save(fig, '31-066')
