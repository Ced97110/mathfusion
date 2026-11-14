import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(74)
box(ax, 18, 58, 52, 10, 'sujet', label=r'$\sin(3x-1{,}5)$')
arrow(ax, (44, 58), (44, 42), 'varie')
text(ax, 47, 50, r'on met 3 en facteur', 'varie', 's', ha='left')
text(ax, 41, 50, r'$1{,}5\div3=0{,}5$', 'varie', 's', ha='right')
box(ax, 18, 32, 52, 10, 'sujet', label=r'$\sin(3(x-0{,}5))$')
arrow(ax, (44, 32), (44, 17), 'resultat')
text(ax, 47, 24.5, 'on lit C', 'resultat', 's', ha='left')
box(ax, 18, 6, 52, 11, 'resultat', label=r'décalage $C=0{,}5$')
save(fig, '30-125')
