import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def row(y, title, a, b):
    text(ax, 3, y + 15, title, 'encre', 's', ha='left', weight='bold')
    box(ax, 3, y, 25, 11, 'sujet', label=a, size='s')
    text(ax, 31.5, y + 5.5, '+', 'encre', 'l', weight='bold')
    box(ax, 35, y, 25, 11, 'autre', label=b, size='s')
    text(ax, 74, y + 5.5, '= (5, 4)', 'resultat', 'm', weight='bold')
row(40, 'avec une base', r'5 $\times$ (1, 0)', r'4 $\times$ (0, 1)')
row(12, 'avec des sous-modules', '(5, 0)', '(0, 4)')
text(ax, 44, 4, 'écriture unique dans les deux cas', 'resultat', 's')
save(fig, '58-254')
