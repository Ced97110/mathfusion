import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)

def mat(x, y, rows, diag, off):
    cw, ch = 11, 10
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            box(ax, x + j * cw, y - i * ch, cw, ch, diag if i == j else off, label=v)

text(ax, 20, 45, 'doubler chaque case', 'resultat', 's')
text(ax, 68, 45, 'échanger les cases', 'limite', 's')
mat(9, 33, [['2', '0'], ['0', '2']], 'sujet', 'fixe')
mat(57, 33, [['0', '1'], ['1', '0']], 'fixe', 'limite')
text(ax, 20, 17, 'garde chaque morceau', 'resultat', 's')
text(ax, 20, 11, 'hors diagonale : 0', 'resultat', 's')
text(ax, 68, 17, 'riz pur → lentilles pur', 'limite', 's')
text(ax, 68, 11, 'hors diagonale : 1', 'limite', 's')
save(fig, '58-275')
