import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 4, 56, 80, 24, 'fixe')
text(ax, 44, 74, 'classe de 2 modulo 7', 'fixe', 'm')
for i, n in enumerate(['2', '9', '16', '…']):
    box(ax, 9 + i * 19, 60, 15, 9, 'encre', label=n)
text(ax, 44, 50, 'même idée avec les polynômes', 'varie', 's')
box(ax, 4, 14, 80, 32, 'sujet')
text(ax, 44, 40, r'$r=x+(f)$ : classe de $x$', 'sujet', 'm')
box(ax, 8, 28, 22, 8, 'encre', label=r'$x$', size='s')
box(ax, 33, 28, 49, 8, 'encre', label=r'$x+(x^2-2)$', size='s')
text(ax, 44, 20, r'$x$ plus un multiple de $f$', 'sujet', 's')
text(ax, 44, 6, r'$r^2=2$', 'resultat', 'l')
save(fig, '62-053')
