import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
y0 = 12
def mat(x, cw, labels, roles):
    for i in range(2):
        for j in range(2):
            box(ax, x + cw * j, y0 + 11 * (1 - i), cw - 1, 10, roles[i][j], label=labels[i][j], size='s', r=0.4)
    w = 2 * cw - 1
    for xe, d in ((x - 1.5, 1), (x + w + 1.5, -1)):
        line(ax, [(xe + d * 1.5, y0 - 1), (xe, y0 - 1), (xe, y0 + 22), (xe + d * 1.5, y0 + 22)], 'encre', lw=0.8)
mat(5, 9, [['λ', '0'], ['0', 'λ']], [['varie', 'fixe'], ['fixe', 'varie']])
text(ax, 27, y0 + 10.5, '−', 'encre', 'xl')
mat(33, 8, [['2', '0'], ['0', '3']], [['sujet', 'fixe'], ['fixe', 'sujet']])
text(ax, 53, y0 + 10.5, '=', 'encre', 'xl')
mat(59, 11, [['λ−2', '0'], ['0', 'λ−3']], [['resultat', 'fixe'], ['fixe', 'resultat']])
save(fig, '60-084')
