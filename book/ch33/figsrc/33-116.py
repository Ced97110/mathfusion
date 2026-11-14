import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
u = 3.6; A = (24, 18); B = (A[0]+4*u, A[1]); C = (B[0], A[1]+3*u)
def sq(P, e1, e2, n, role):
    pts = [P, (P[0]+n*e1[0], P[1]+n*e1[1]), (P[0]+n*(e1[0]+e2[0]), P[1]+n*(e1[1]+e2[1])), (P[0]+n*e2[0], P[1]+n*e2[1])]
    poly(ax, pts, role)
    for k in range(1, n):
        line(ax, [(P[0]+k*e1[0], P[1]+k*e1[1]), (P[0]+k*e1[0]+n*e2[0], P[1]+k*e1[1]+n*e2[1])], role, lw=0.3)
        line(ax, [(P[0]+k*e2[0], P[1]+k*e2[1]), (P[0]+k*e2[0]+n*e1[0], P[1]+k*e2[1]+n*e1[1])], role, lw=0.3)
sq((A[0], A[1]-4*u), (u, 0), (0, u), 4, 'sujet')
sq(B, (u, 0), (0, u), 3, 'sujet')
sq(A, (0.8*u, 0.6*u), (-0.6*u, 0.8*u), 5, 'resultat')
poly(ax, [A, B, C], 'fixe')
text(ax, A[0]+2*u, A[1]-2*u, '16', 'sujet', 'l', weight='bold'); text(ax, B[0]+1.5*u, B[1]+1.5*u, '9', 'sujet', 'l', weight='bold')
text(ax, A[0]-0.1*u, A[1]+3.2*u, '25', 'resultat', 'l', weight='bold')
text(ax, 70, 58, r'$3^2+4^2=25$', 'encre', 'm'); text(ax, 70, 50, r'$AC=\sqrt{25}=5$', 'resultat', 'm')
text(ax, 70, 28, r'$AB=4$', 'sujet', 's'); text(ax, 70, 22, r'$BC=3$', 'sujet', 's')
save(fig, '33-116')
