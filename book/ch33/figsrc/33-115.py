import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
s = 8; A = (8, 14); B = (A[0]+4*s, A[1]); C = (B[0], A[1]+3*s)
poly(ax, [A, B, C], 'sujet')
line(ax, [(B[0]-2.5, B[1]), (B[0]-2.5, B[1]+2.5), (B[0], B[1]+2.5)], 'sujet')
for k in (1, 2): ax.plot([B[0]-1, B[0]+1], [B[1]+k*s]*2, color=COL['sujet'], lw=0.7, zorder=3)
for k in (1, 2, 3): ax.plot([A[0]+k*s]*2, [A[1]-1, A[1]+1], color=COL['sujet'], lw=0.7, zorder=3)
line(ax, [(A[0]+9*math.cos(a), A[1]+9*math.sin(a)) for a in [i*math.atan(3/4)/20 for i in range(21)]], 'varie', lw=1.0)
text(ax, A[0]+12.5, A[1]+3, r'$\theta$', 'varie', 'm')
text(ax, A[0]-3, A[1]-3, '$A$', 'encre'); text(ax, B[0]+3, B[1]-3, '$B$', 'encre'); text(ax, C[0]+3, C[1]+1, '$C$', 'encre')
text(ax, (A[0]+B[0])/2, A[1]-5, r'$AB=4$', 'sujet', 'm'); text(ax, B[0]+4, (B[1]+C[1])/2, r'$BC=3$', 'sujet', 'm', ha='left')
box(ax, 56, 40, 30, 12, 'varie', label=r'$\tan\theta=\frac{3}{4}$')
save(fig, '33-115')
