import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
u = 6
cols = [(15, 1, [[1]]), (44, 2, [[2], [1, 1]]), (73, 3, [[3], [2, 1], [1, 1, 1]])]
for cx, a, parts in cols:
    for k, ps in enumerate(parts):
        x = cx - u * a / 2; y = 38 - 9 * k
        for p in ps:
            box(ax, x, y, u * p - 0.8, 7, 'sujet', label=str(p), size='s', r=0.5)
            x += u * p
    text(ax, cx, 8, rf'$a={a}$ : $P({a})={a}$', 'resultat', 's')
save(fig, '60-224')
