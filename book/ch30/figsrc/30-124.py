import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(80)
box(ax, 3, 60, 37, 10, 'sujet', label=r'$\sin(2x-\pi/2)$')
box(ax, 49, 60, 36, 10, 'autre', label=r'$\sin(2(x-\pi/4))$')
text(ax, 44.5, 65, '=', 'encre', 'l')
text(ax, 44, 52, 'pour x = 1', 'fixe', 's')
arrow(ax, (21.5, 60), (21.5, 46), 'fixe'); arrow(ax, (67, 60), (67, 46), 'fixe')
box(ax, 3, 36, 37, 10, 'resultat', label=r'$2\cdot1-\pi/2\approx0{,}429$', size='s')
box(ax, 49, 36, 36, 10, 'resultat', label=r'$2(1-\pi/4)\approx0{,}429$', size='s')
text(ax, 44.5, 41, '=', 'resultat', 'l')
arrow(ax, (67, 36), (46, 21), 'varie', curve=0.2)
box(ax, 4, 12, 40, 10, 'varie', label=r'$2\times\pi/4=\pi/2$')
text(ax, 66, 17, 'on met 2 en facteur', 'varie', 's')
save(fig, '30-124')
