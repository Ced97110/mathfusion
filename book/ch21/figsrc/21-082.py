import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def row(y, title, wrong):
    text(ax, 44, y + 22, title, 'encre', 's')
    box(ax, 4, y, 10, 9, 'fixe', True, '7')
    box(ax, 17, y, 10, 9, 'varie', True, r'$-$')
    if not wrong:
        box(ax, 30, y, 28, 9, 'sujet', True, r'$(2+1)$')
        box(ax, 62, y, 18, 9, 'resultat', True, r'$=4$')
        brace(ax, 18, 57, y + 10, 'varie', 'le moins agit sur 2 et 1', down=False)
    else:
        box(ax, 30, y, 10, 9, 'sujet', True, '2')
        box(ax, 43, y, 14, 9, 'fixe', True, r'$+1$')
        box(ax, 62, y, 18, 9, 'limite', True, r'$=6$')
        brace(ax, 18, 39, y + 10, 'varie', 'le moins agit sur 2', down=False)
row(34, 'avec parenthèses', False)
row(4, 'sans parenthèses', True)
save(fig, '21-082')
