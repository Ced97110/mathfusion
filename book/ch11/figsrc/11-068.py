import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
def row(y, head, calc, tot, rep, rest):
    text(ax, 44, y + 20, head, 'fixe', 'm')
    box(ax, 4, y + 3, 30, 11, 'sujet', label=calc, size='m')
    arrow(ax, (35, y + 8.5), (42, y + 8.5), 'fixe')
    box(ax, 43, y + 3, 14, 11, 'fixe', label=tot, size='m')
    arrow(ax, (58, y + 8.5), (63, y + 8.5), 'fixe')
    box(ax, 64, y + 3, 10, 11, 'varie', label=rep, size='m')
    box(ax, 75, y + 3, 10, 11, 'resultat', label=rest, size='m')
    text(ax, 69, y - 1, 'report', 'varie', 's'); text(ax, 80, y - 1, 'écrit', 'resultat', 's')
row(42, 'colonne de 0 à 9', '8 + 7', '15', '1', '5')
row(5, 'colonne de 0 à 59', '40 + 35', '75', '1', '15')
save(fig, '11-068')
