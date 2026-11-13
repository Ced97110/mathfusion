import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
def row(y, name, vals, roles, note, nrole):
    text(ax, 11, y + 4.5, name, 'encre', 'm')
    for i, (v, r) in enumerate(zip(vals, roles)):
        box(ax, 24 + 14 * i, y, 12, 9, r, label=str(v))
    brace(ax, 38, 64, y - 1, nrole, label=note)
row(48, '12 =', [2, 2, 3], ['sujet', 'limite', 'fixe'], 'reste 6 : contient 2', 'limite')
row(26, '30 =', [2, 3, 5], ['sujet', 'fixe', 'fixe'], 'reste 15 : sans 2', 'resultat')
save(fig, '80-348')
