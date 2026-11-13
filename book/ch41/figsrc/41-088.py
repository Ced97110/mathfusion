import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
bw, gap, x0 = 15, 7, 3.5
xs = [x0 + i * (bw + gap) for i in range(4)]
heads = [('sujet', r'$u\cdot v$'), ('fixe', r'$\|u\|\|v\|$'), ('varie', r'$\cos\theta$'), ('resultat', '$\\theta$\n(arccos)')]
for (role, lab), x in zip(heads, xs):
    box(ax, x, 51, bw, 11, role, label=lab, size='s')
for i in range(3):
    arrow(ax, (xs[i] + bw + 0.5, 56.5), (xs[i + 1] - 0.5, 56.5), 'fixe', lw=0.8)
rowsA = [r'$u=\langle2,0\rangle,\ v=\langle1,1\rangle$', ['2', r'$2\sqrt{2}$', '0,7071', '45°']]
rowsB = [r'$u=\langle3,0\rangle,\ v=\langle0,2\rangle$', ['0', r'$3\times2$', '0', '90°']]
for (lab, cells), y in ((rowsA, 31), (rowsB, 9)):
    text(ax, 44, y + 13, lab, 'encre', 's')
    for c, x in zip(cells, xs):
        box(ax, x, y, bw, 8, 'fixe', label=c, size='s')
save(fig, '41-088')
