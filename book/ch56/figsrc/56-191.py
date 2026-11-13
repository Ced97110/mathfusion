import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'idéal $(2,\,x)$ : terme constant pair', 'sujet', 's')
for y, poly, a0, a1, c0, c1, t0, t1, role, verdict in [
        (40, r'$2+3x$', '2', r'$3x$', 'sujet', 'varie', 'pair', 'quelconque', 'resultat', r'dans $(2,\,x)$ : $2\times1+x\times3$'),
        (6, r'$1+x$', '1', r'$x$', 'limite', 'varie', 'impair', 'quelconque', 'limite', r'pas dans $(2,\,x)$')]:
    text(ax, 10, y + 15, poly, 'encre', 'l')
    box(ax, 24, y + 9, 24, 12, c0, label=a0, size='l')
    box(ax, 52, y + 9, 24, 12, c1, label=a1, size='l')
    text(ax, 36, y + 4, t0, c0, 's')
    text(ax, 64, y + 4, t1, c1, 's')
    text(ax, 44, y - 2 if False else y + 24, verdict, role, 's')
save(fig, '56-191')
