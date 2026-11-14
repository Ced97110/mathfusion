import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)

def mat(x, y, rows, role, hl=None):
    hl = hl or {}
    cw, ch = 11, 9
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            r = hl.get((i, j), role)
            box(ax, x + j * cw, y - i * ch, cw, ch, r, label=v)

text(ax, 19, 41, 'ancienne base', 'sujet', 's')
text(ax, 69, 41, 'nouvelle base', 'autre', 's')
mat(8, 29, [['2', '1'], ['1', '3']], 'sujet')
mat(58, 29, [['0', '−1'], ['5', '5']], 'autre', {(0, 0): 'resultat'})
arrow(ax, (32, 28), (55, 28), 'varie', lw=1.1)
text(ax, 43.5, 32, 'même application', 'varie', 's')
text(ax, 43.5, 24, 'autre tableau', 'varie', 's')
text(ax, 69, 12, 'un zéro : calcul', 'resultat', 's')
text(ax, 69, 8, 'plus facile', 'resultat', 's')
text(ax, 19, 10, 'quelle base choisir ?', 'sujet', 's')
text(ax, 44, 3, 'programme des chapitres 59 et 60', 'fixe', 's')
save(fig, '58-272')
