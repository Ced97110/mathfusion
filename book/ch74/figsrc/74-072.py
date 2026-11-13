import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u, oy = 8, 16
def panel(ox, v, title):
    for i in range(5):
        for j in range(4): disc(ax, ox + i*u, oy + j*u, 0.8, 'sujet')
    arrow(ax, (ox, oy), (ox + u, oy), 'varie', lw=1.3)
    arrow(ax, (ox, oy), (ox + v*u, oy + u), 'varie', lw=1.3)
    text(ax, ox + u/2, oy - 3.8, '$x$', 'varie', 'm')
    text(ax, ox + v*u + (4 if v else -3.5), oy + u + (2.5 if v else 0), '$y$', 'varie', 'm')
    text(ax, ox + 2*u, oy + 3*u + 7, title, 'varie', 'm')
panel(10, 0, 'couple 1'); panel(52, 1, 'couple 2')
text(ax, 44, 5, 'mêmes points : un seul réseau', 'resultat', 'm')
save(fig, '74-072')
