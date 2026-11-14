import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, 'sur l’horloge à 6 heures', 'autre', 's')
rows = [(48, '2', '3', '6 = 0'), (30, '3', '4', '12 = 0')]
for y, a, b, res in rows:
    box(ax, 4, y, 14, 11, 'sujet', label=a, size='l')
    text(ax, 24, y + 5.5, '×', 'encre', 'l')
    box(ax, 30, y, 14, 11, 'sujet', label=b, size='l')
    text(ax, 50, y + 5.5, '=', 'encre', 'l')
    box(ax, 56, y, 28, 11, 'limite', label=res, size='l')
text(ax, 44, 17, 'un seul cas suffit', 'limite', 'm')
text(ax, 44, 8, 'mille cas non nuls ne prouvent rien', 'fixe', 's')
save(fig, '54-026')
