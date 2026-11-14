import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def row(y, a, b, tag):
    text(ax, 3, y + 14, tag, 'fixe', 's', ha='left')
    box(ax, 4, y, 40, 11, 'varie', label=a, size='l')
    box(ax, 47, y, 14, 11, 'sujet', label=r'$\leq$', size='xl')
    box(ax, 64, y, 20, 11, 'fixe', label=b, size='l')
    text(ax, 24, y - 3, 'ce qui varie', 'varie', 's')
    text(ax, 54, y - 3, 'signe', 'sujet', 's')
    text(ax, 74, y - 3, 'limite', 'fixe', 's')
row(44, r'$3 + 2d$', '15', 'taxi')
row(12, r'$8 + 3d$', '20', 'cinéma')
save(fig, '17-004')
