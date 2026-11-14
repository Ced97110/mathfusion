import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, r'$0\,v=\mathbf{0}$', 'sujet', 'l', weight='bold')
for y, (a, b) in [(30, ('4', '7')), (10, ('1', '−2'))]:
    box(ax, 4, y, 12, 10, 'sujet', label=a, size='s')
    box(ax, 16, y, 12, 10, 'sujet', label=b, size='s')
    arrow(ax, (31, y + 5), (53, y + 5), 'varie', lw=1.5)
    text(ax, 42, y + 9, r'$\times\,0$', 'varie', 's')
    box(ax, 56, y, 12, 10, 'resultat', label='0', size='s')
    box(ax, 68, y, 12, 10, 'resultat', label='0', size='s')
text(ax, 62, 45, 'vecteur nul', 'resultat', 's')
save(fig, '58-108')
