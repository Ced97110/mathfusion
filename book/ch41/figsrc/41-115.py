import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
w, g = 12.5, 1.6
x0 = (88 - 6 * w - 5 * g) / 2
xs = [x0 + i * (w + g) for i in range(6)]
common = [r'$u_1^2v_1^2$', r'$u_1^2v_2^2$', r'$u_2^2v_1^2$', r'$u_2^2v_2^2$']
ya, yb = 30, 8
text(ax, 44, 52, r'$\|u\times v\|^2+(u\cdot v)^2$', 'encre', 'm')
for i, lab in enumerate(common):
    box(ax, xs[i], ya, w, 9, 'sujet', label=lab, size='s')
    box(ax, xs[i], yb, w, 9, 'sujet', label=lab, size='s')
    line(ax, [(xs[i] + w / 2, ya), (xs[i] + w / 2, yb + 9)], 'fixe', dash=True, lw=0.6)
box(ax, xs[4], ya, w, 9, 'varie', label=r'$-2P$', size='s')
box(ax, xs[5], ya, w, 9, 'varie', label=r'$+2P$', size='s')
text(ax, (xs[4] + xs[5] + w) / 2, 43, 'se compensent', 'varie', 's')
brace(ax, xs[4], xs[5] + w, ya + 9, 'varie', down=False, depth=1.6)
text(ax, 72, 19.5, r'est égal à $\|u\|^2\,\|v\|^2$', 'encre', 'm')
text(ax, 44, 2.5, r'$P=u_1v_1u_2v_2$', 'varie', 's')
save(fig, '41-115')
