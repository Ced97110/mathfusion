import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
w, g = 15.0, 7.0
x0 = (88 - 4 * w - 3 * g) / 2
xs = [x0 + i * (w + g) for i in range(4)]
cx = [x + w / 2 for x in xs]
labs = [r'$f_0(c)=0$', r'$f_1(c)=0$', r'$f_2(c)=0$', r'$f_3(c)=0$']
roles = ['varie', 'sujet', 'sujet', 'limite']
for i in range(4):
    box(ax, xs[i], 36, w, 10, roles[i], label=labs[i], size='s', dash=(i in (0, 3)))
arrow(ax, (xs[1] - 0.5, 41), (xs[0] + w + 0.5, 41), 'varie', lw=1.2)
arrow(ax, (xs[2] + w + 0.5, 41), (xs[3] - 0.5, 41), 'varie', lw=1.2)
text(ax, cx[0], 50, 'déduit', 'varie', 's')
text(ax, cx[3], 50, 'déduit', 'varie', 's')
brace(ax, xs[1], xs[2] + w, 34.5, 'sujet', label='deux voisins nuls', size='s')
arrow(ax, (cx[3], 35), (cx[3], 19), 'limite', lw=1.0)
box(ax, 8, 4, 72, 14, 'resultat', label=r'or $f_3=9/4$, jamais nul :' + '\n' + 'contradiction', size='m')
save(fig, '69-096')
