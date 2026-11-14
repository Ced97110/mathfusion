import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
s = 8; A = (8, 14); B = (A[0]+4*s, A[1]); C = (B[0], A[1]+3*s)
poly(ax, [A, B, C], 'fixe')
line(ax, [(B[0]-2.5, B[1]), (B[0]-2.5, B[1]+2.5), (B[0], B[1]+2.5)], 'fixe')
line(ax, [A, B], 'varie', lw=2.2); line(ax, [A, C], 'autre', lw=2.2)
line(ax, [(A[0]+9*math.cos(a), A[1]+9*math.sin(a)) for a in [i*math.atan(3/4)/20 for i in range(21)]], 'sujet', lw=1.0)
text(ax, A[0]+12.5, A[1]+3, r'$\theta$', 'sujet', 'm')
text(ax, (A[0]+B[0])/2, A[1]-4, '4 : collé à l’angle', 'varie', 's')
text(ax, B[0]+3, (B[1]+C[1])/2, '3', 'fixe', 'm', ha='left')
text(ax, A[0]+9, A[1]+19, '5 : hypoténuse', 'autre', 's', rot=37)
box(ax, 54, 38, 32, 14, 'resultat', label=r'$\cos\theta=\frac{4}{5}$')
save(fig, '33-117')
