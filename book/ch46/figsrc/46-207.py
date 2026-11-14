import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx = [14, 34, 54, 74]
for x, c, o, v in zip(cx, ['(1 3 5 8)', '(2 6)', '(4)', '(7)'], ['4 − 1', '2 − 1', '1 − 1', '1 − 1'], ['3', '1', '0', '0']):
    box(ax, x - 9, 50, 18, 9, 'sujet', label=c, size='s')
    arrow(ax, (x, 49), (x, 41), 'fixe', lw=0.8)
    box(ax, x - 7, 32, 14, 9, 'varie', label=o)
    arrow(ax, (x, 31), (x, 24), 'fixe', lw=0.8)
    disc(ax, x, 19, 4.2, 'resultat', label=v, size='l')
brace(ax, 8, 80, 12, 'resultat', label='somme = 3 + 1 + 0 + 0 = 4')
save(fig, '46-207')
