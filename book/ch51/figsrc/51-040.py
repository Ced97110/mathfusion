import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def col(cx, head, seq):
    text(ax, cx, 55, head, 'fixe', 'm')
    xs = [cx - 17, cx - 1]
    box(ax, cx - 17, 33, 10, 10, *[(seq[0][1])], label=seq[0][0], size='l')
    text(ax, cx - 3.5, 38, '⋅', 'encre', 'l')
    box(ax, cx - 0.5, 33, 10, 10, seq[1][1], label=seq[1][0], size='l')
    arrow(ax, (cx - 4.5, 31), (cx - 4.5, 23), 'resultat')
    box(ax, cx - 12, 11, 15, 10, 'resultat', label='$a$', size='l')
    text(ax, cx - 18.5 + 4, 16, '=', 'resultat', 'l')
col(22, '1 à droite', [('$a$', 'sujet'), ('1', 'varie')])
col(66, '1 à gauche', [('1', 'varie'), ('$a$', 'sujet')])
text(ax, 44, 3.5, 'a reste a, des deux côtés', 'resultat', 'm')
save(fig, '51-040')
