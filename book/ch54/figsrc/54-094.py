import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cw = 6.8
def seq(x, y, vals, role):
    for i, v in enumerate(vals):
        box(ax, x + i * cw, y, cw - 0.4, 8, role, label=str(v), size='s')
A = [3, 5, 0]
add = [a + z for a, z in zip(A, [0, 0, 0])]
assert add == A
mul = [3 * 1, 3 * 0 + 5 * 1, 3 * 0 + 5 * 0 + 0 * 1]
assert mul == A
for y, op, other, title in [(40, '+', [0, 0, 0], 'ajouter la suite nulle'), (12, '×', [1, 0, 0], 'multiplier par (1, 0, 0, …)')]:
    text(ax, 44, y + 17, title, 'encre', 'm')
    seq(8, y, A, 'fixe')
    text(ax, 8 + 3 * cw + 1.5, y + 4, op, 'encre', 'l')
    seq(8 + 3 * cw + 5, y, other, 'sujet')
    text(ax, 8 + 6 * cw + 8, y + 4, '=', 'encre', 'l')
    seq(8 + 6 * cw + 12, y, A, 'resultat')
save(fig, '54-094')
