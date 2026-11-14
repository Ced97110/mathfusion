import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$f=x^2$ divisé par $g=2x-1$, $b_m=2$', 'sujet', 'm')
labels = [r'$x^2$', r'$2x^2$', r'$x$', r'$2x$', r'$1$']
roles = ['sujet', 'fixe', 'fixe', 'fixe', 'resultat']
bw, gap, y0, bh = 11, 7.25, 36, 9
xs = [2 + i * (bw + gap) for i in range(5)]
for x, lab, r in zip(xs, labels, roles):
    box(ax, x, y0, bw, bh, r, label=lab)
acts = [r'$\times2$', r'$-x\,g$', r'$\times2$', r'$-1\,g$']
for i, a in enumerate(acts):
    p = (xs[i] + bw, y0 + bh / 2); q = (xs[i + 1], y0 + bh / 2)
    arrow(ax, p, q, 'varie')
    text(ax, (p[0] + q[0]) / 2, y0 + bh + 3, a, 'varie', 's')
brace(ax, xs[0] + bw / 2, xs[3] + bw / 2, y0 - 1.5, 'varie', label=r'$\times2$ deux fois : $b_m^{\,k}=4$, $k=2$', depth=1.6)
text(ax, 44, 12, r'$4x^2=(2x+1)(2x-1)+1$', 'resultat', 'l')
text(ax, 44, 4, 'reste 1 : degré 0, plus petit que 1', 'resultat', 's')
save(fig, '54-148')
