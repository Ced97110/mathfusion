import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
s = 8; A = (8, 14); B = (A[0]+4*s, A[1]); C = (B[0], A[1]+3*s)
poly(ax, [A, B, C], 'fixe')
line(ax, [(B[0]-2.5, B[1]), (B[0]-2.5, B[1]+2.5), (B[0], B[1]+2.5)], 'fixe')
line(ax, [B, C], 'varie', lw=2.2); line(ax, [A, C], 'autre', lw=2.2)
line(ax, [(A[0]+9*math.cos(a), A[1]+9*math.sin(a)) for a in [i*math.atan(3/4)/20 for i in range(21)]], 'sujet', lw=1.0)
text(ax, A[0]+12.5, A[1]+3, r'$\theta$', 'sujet', 'm')
text(ax, (A[0]+B[0])/2, A[1]-4, '4', 'fixe', 'm')
text(ax, B[0]+3, (B[1]+C[1])/2, '3 : en face', 'varie', 's', ha='left')
text(ax, A[0]+9, A[1]+19, '5 : hypoténuse', 'autre', 's', rot=37)
box(ax, 54, 38, 32, 14, 'resultat', label=r'$\sin\theta=\frac{3}{5}$')
save(fig, '33-146')
