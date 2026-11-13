import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
def cells(x, y, n, role, lab=None):
    for i in range(n): box(ax, x + i * 8, y, 7, 7, role, label=None if lab is None else lab[i], size='s')
text(ax, 4, 79, 'tableau 2×2', 'sujet', 's', ha='left')
cells(4, 66, 4, 'sujet', ['$a$', '$b$', '$c$', '$d$']); brace(ax, 4, 35, 65, 'sujet', '4 nombres')
text(ax, 4, 53, r'complexe $2+3i$', 'sujet', 's', ha='left')
cells(4, 40, 2, 'sujet', ['2', '3']); brace(ax, 4, 19, 39, 'sujet', '2 nombres')
text(ax, 64, 62, 'la liste s’arrête :\ndimension finie', 'sujet', 's', weight='bold')
text(ax, 4, 28, 'polynômes', 'autre', 's', ha='left')
cells(4, 15, 5, 'autre', ['1', r'$x$', r'$x^2$', r'$x^3$', r'$x^4$'])
arrow(ax, (45, 18.5), (82, 18.5), 'autre')
text(ax, 44, 6, 'sans fin : dimension infinie', 'autre', 's', weight='bold')
save(fig, '76-020')
