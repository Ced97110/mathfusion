import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [r'$x^2-0{,}01$', r'$2x$', r'$0{,}01$']
bx = [20, 38, 56]
bw = 14
for c, x in zip(cols, bx):
    text(ax, x + bw / 2, 55, c, 'sujet', 's')
rows = [(r'$x=-1$', ['+', '−', '+'], r'$V(-1)=2$', 38), (r'$x=1$', ['+', '+', '+'], r'$V(1)=0$', 22)]
for lab, sg, v, y in rows:
    text(ax, 10, y + 5, lab, 'encre', 'm')
    for i, (s, x) in enumerate(zip(sg, bx)):
        box(ax, x, y, bw, 10, 'sujet', label=s, size='l')
        if i < 2 and sg[i] != sg[i + 1]:
            arrow(ax, (x + bw + 0.4, y + 5), (bx[i + 1] - 0.4, y + 5), 'varie', lw=1.2)
    text(ax, 78, y + 5, v, 'encre', 'm')
box(ax, 12, 4, 64, 10, 'resultat', label=r'2 racines : $2-0=2$', size='m')
save(fig, '69-093')
