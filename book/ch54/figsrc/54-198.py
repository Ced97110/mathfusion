import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 80, r'une classe = les polynômes de même reste', 'sujet', 's')
for y, name, f, r in [(46, r'classe de $0$', r'$x^3+x$', r'$0$'),
                      (14, r'classe de $3x+1$', r'$x^2+3x+2$', r'$3x+1$')]:
    box(ax, 2, y, 84, 28, 'sujet', fill=False, dash=True, lw=1.0)
    text(ax, 5, y + 24, name, 'sujet', 's', ha='left')
    box(ax, 6, y + 4, 30, 12, 'fixe', label=f)
    arrow(ax, (36, y + 10), (54, y + 10), 'varie')
    text(ax, 45, y + 14.5, r'$\div(x^2+1)$', 'varie', 's')
    box(ax, 54, y + 4, 28, 12, 'resultat', label=r, weight='bold')
text(ax, 44, 7, r'reste vert : degré $<2$, un seul par classe', 'resultat', 's')
save(fig, '54-198')
