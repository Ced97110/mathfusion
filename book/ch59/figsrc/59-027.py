import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'1re case de $(x,\,y)$ = $x$', 'encre', 's')
text(ax, 44, 60, 'ronds bleus : 1res cases de K', 'sujet', 's')
f = numberline(ax, 8, 74, 34, 0, 12, arrow_right=False, size='s', every=2)
for v in range(13):
    if v % 2 == 0: disc(ax, f(v), 34, 1.6, 'sujet')
arrow(ax, (f(4), 38), (f(10), 38), 'varie', curve=-0.4, lw=0.9)
text(ax, f(7), 50, r'$4+6=10$', 'varie', 's')
arrow(ax, (f(4) + 1, 29.5), (f(12) - 1, 29.5), 'resultat', curve=0.35, lw=0.9)
text(ax, f(8), 18.5, r'$3\times4=12$', 'resultat', 's')
box(ax, 14, 2, 60, 10, 'sujet', label=r'$I=(2)$ : tous multiples de 2', size='s')
save(fig, '59-027')
