import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 16, 61, r'$x$', 'encre', 'l')
text(ax, 72, 61, r'$x^2$', 'encre', 'l')
text(ax, 44, 61, r'$\varphi:x\mapsto x^p$', 'varie', 's')
els = ['0', '1', r'$\alpha$', r'$\alpha+1$']
ys = [46, 34, 22, 10]
for i, (s, y) in enumerate(zip(els, ys)):
    r = 'varie' if i >= 2 else 'fixe'
    box(ax, 6, y, 20, 9, r, label=s)
    box(ax, 62, y, 20, 9, r, label=els[i])
tgt = [0, 1, 3, 2]
for i, y in enumerate(ys):
    arrow(ax, (26, y + 4.5), (62, ys[tgt[i]] + 4.5), 'varie' if i >= 2 else 'fixe', lw=0.9)
text(ax, 44, 3, 'p = 2 : on élève au carré', 'varie', 's')
save(fig, '67-052')
