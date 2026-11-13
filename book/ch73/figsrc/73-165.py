import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'pente voulue : b = 6', 'encre', 'l')
cols = [(24, 'resultat', ['d = 2', r'$d^2-1=3$', r'$c\times 3=6$', 'c = 2 : réussi']),
        (64, 'limite', ['d = 1', r'$d^2-1=0$', r'$c\times 0=6$', 'aucun c : échec'])]
ys = [54, 40, 26, 12]
for cx, r, ls in cols:
    for i, (y, l) in enumerate(zip(ys, ls)):
        box(ax, cx - 18, y, 36, 9, r if i >= 1 else 'sujet', label=l, size='s')
        if i: arrow(ax, (cx, ys[i - 1]), (cx, y + 9.3), 'fixe')
save(fig, '73-165')
