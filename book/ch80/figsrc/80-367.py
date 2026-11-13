import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
xs = [32, 52, 72]; ys = [12, 34, 56, 78]
lv = [[(52, '30')], list(zip(xs, ['15', '10', '6'])), list(zip(xs, ['5', '3', '2'])), [(52, '1')]]
for a, b in [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1), (2, 2)]:
    line(ax, [(xs[a], ys[1] + 5), (xs[b], ys[2] - 5)], 'fixe')
for x in xs: line(ax, [(52, ys[0] + 5), (x, ys[1] - 5)], 'fixe'); line(ax, [(x, ys[2] + 5), (52, ys[3] - 5)], 'fixe')
for i, row in enumerate(lv):
    role = 'sujet' if i % 2 == 0 else 'varie'
    for x, s in row: box(ax, x - 7, ys[i] - 5, 14, 10, role, label=s, size='m')
    text(ax, 2, ys[i], r'$|U|=%d$ : %s' % (i, '+' if i % 2 == 0 else '−'), role, 's', ha='left')
text(ax, 52, 93, r'$f(\emptyset)=\sum(-1)^{|U|}\,g(U)$', 'resultat', 'm')
save(fig, '80-367')
