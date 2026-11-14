import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def pair(y, n2, u2, role, sym, cap):
    box(ax, 3, y, 10, 10, 'sujet', label='8')
    box(ax, 13, y, 18, 10, 'autre', label='miles')
    box(ax, 47, y, 10, 10, 'sujet', label=n2)
    box(ax, 57, y, 28, 10, 'autre' if role == 'resultat' else 'limite', label=u2)
    text(ax, 39, y + 5, sym, role, 'xl')
    text(ax, 44, y - 5, cap, role, 'm', weight='bold')
pair(46, '3', 'miles', 'resultat', '=', 'même dénomination')
pair(16, '5', 'gallons', 'limite', r'$\neq$', 'dénominations différentes')
text(ax, 44, 62, 'la dénomination = le mot après', 'encre', 's')
save(fig, '09-024')
