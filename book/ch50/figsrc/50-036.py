import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$G$ : 12 éléments, $p=2$', 'encre', 'm')
def row(y, k, role, lab, ly):
    text(ax, 44, ly, lab, role, 'm')
    for i in range(12):
        disc(ax, 11 + 6 * i, y, 2.2, role if i < k else 'fixe')
row(40, 4, 'sujet', r'4 éléments $=2^2$ : un 2-Sylow', 49)
row(18, 2, 'varie', r'2 éléments $=2^1$ : trop petit', 27)
save(fig, '50-036')
