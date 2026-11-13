import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
def row(y, a, b, ua, ub, la, lb, lt, head):
    text(ax, 44, y + 20, head, 'encre', 's')
    x0 = 4
    wa, wb = a * ua, b * ub
    box(ax, x0, y + 4, wa, 9, 'sujet', label=la, size='s')
    box(ax, x0 + wa, y + 4, wb, 9, 'varie', label=lb, size='s')
    brace(ax, x0, x0 + wa + wb, y + 2, 'resultat', label=lt, down=True, size='s')
row(50, 3, 4, 10, 10, '3', '4', '3 + 4 = 7', '$2^{3}$ · $2^{4}$ = $2^{7}$')
row(9, 30, 60, 0.9, 0.9, '30°', '60°', '30° + 60° = 90°', 'cis 30° · cis 60° = cis 90°')
text(ax, 80, 78, 'chapitre 14', 'fixe', 's')
text(ax, 76, 36, 'ce chapitre', 'fixe', 's')
save(fig, '39-080')
