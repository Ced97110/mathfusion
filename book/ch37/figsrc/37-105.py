import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'$x_1y_1$ et $-x_1y_1$ s’annulent', 'varie', 's')
r1 = [r'$x_2y_3$', r'$-x_2y_1$', r'$-x_1y_3$', r'$+x_1y_1$']
r2 = [r'$-x_3y_2$', r'$+x_3y_1$', r'$+x_1y_2$', r'$-x_1y_1$']
for (lab, ytop, terms) in ((r'$X_2Y_3 =$', 44, r1), (r'$-X_3Y_2 =$', 28, r2)):
    text(ax, 2, ytop - 4.5, lab, 'encre', 's', ha='left')
    for k, t in enumerate(terms):
        x = 19 + k * 17; cancel = (k == 3)
        box(ax, x, ytop - 9, 15, 9, 'varie' if cancel else 'sujet', label=t, size='s')
        if cancel: line(ax, [(x + 1, ytop - 8), (x + 14, ytop - 1)], 'fixe', lw=1.3)
arrow(ax, (44, 19), (44, 14), 'fixe')
text(ax, 47, 16.5, r'regroupés par $x$', 'fixe', 's', ha='left')
box(ax, 22, 2, 44, 10, 'resultat', label=r'$-4+28+0 = 24$', size='m')
save(fig, '37-105')
