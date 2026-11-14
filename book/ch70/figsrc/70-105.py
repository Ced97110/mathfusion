import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 14, 64, 60, 12, 'sujet', label=r'$\mathrm{Res}_y(f,g)=x^2(x^2-3)$')
for cx, xv, a, b in [(22, 2, r'$4\times1=4$', 'tableau : 4'), (66, 3, r'$9\times6=54$', 'tableau : 54')]:
    box(ax, cx - 14, 46, 28, 10, 'varie', label=r'$x=%d$' % xv)
    arrow(ax, (cx, 63.5), (cx, 57.5), 'fixe', lw=0.7)
    box(ax, cx - 14, 30, 28, 10, 'sujet', label=a, size='s')
    arrow(ax, (cx, 45.5), (cx, 41.5), 'fixe', lw=0.7)
    box(ax, cx - 14, 14, 28, 10, 'autre', label=b, size='s')
    text(ax, cx, 27, '=', 'resultat', 'l')
text(ax, 44, 6, 'la forme reste, le nombre change', 'fixe', 's')
save(fig, '70-105')
