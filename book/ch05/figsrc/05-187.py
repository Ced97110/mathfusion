import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
bw, bh, xs = 22, 13, [4, 34, 64]
text(ax, 44, 62, 'diviser, garder le reste', 'encre', 'm', weight='bold')
for x, h, role in zip(xs, ('à diviser', 'diviseur', 'reste'), ('fixe', 'sujet', 'varie')):
    text(ax, x + bw / 2, 54, h, role, 's')
y1, y2 = 36, 12
r1 = [r'$x^2+5x+7$' + '\ndegré 2', r'$x+2$' + '\ndegré 1', '1\ndegré 0']
r2 = [r'$x+2$' + '\ndegré 1', '1\ndegré 0', '0']
roles1 = ['fixe', 'sujet', 'varie']
roles2 = ['fixe', 'resultat', 'fixe']
for x, t, ro in zip(xs, r1, roles1): box(ax, x, y1, bw, bh, ro, label=t, size='s')
for x, t, ro in zip(xs, r2, roles2): box(ax, x, y2, bw, bh, ro, label=t, size='s')
arrow(ax, (xs[1] + bw / 2, y1), (xs[0] + bw / 2, y2 + bh), 'varie')
arrow(ax, (xs[2] + bw / 2, y1), (xs[1] + bw / 2, y2 + bh), 'varie')
text(ax, xs[1] + bw / 2, 7, 'dernier reste non nul', 'resultat', 's')
save(fig, '05-187')
