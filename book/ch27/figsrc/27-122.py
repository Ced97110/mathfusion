import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(62)
s = 10.0; A = (8, 8); B = (A[0]+6*s, 8)
cx = (25-16+36)/12; C = (A[0]+cx*s, 8+math.sqrt(25-cx**2)*s)
poly(ax, [A, B, C], 'sujet')
text(ax, (A[0]+B[0])/2, 4, '6', 'sujet', 's')
text(ax, (A[0]+C[0])/2-3, (A[1]+C[1])/2+2, '5', 'sujet', 's')
text(ax, (B[0]+C[0])/2+3, (B[1]+C[1])/2+2, '4', 'sujet', 's')
t1 = math.degrees(math.atan2(B[1]-C[1], B[0]-C[0])); t2 = math.degrees(math.atan2(A[1]-C[1], A[0]-C[0])) + 360
ax.add_patch(Arc(C, 16, 16, theta1=t2, theta2=t1+360, color=COL['varie'], lw=1.4))
text(ax, C[0], C[1]-11, '?', 'varie', 'm')
text(ax, 72, 30, 'angle cherché', 'varie', 's')
text(ax, 44, 58, '4² + 5² = 41 ≠ 36', 'fixe', 's')
box(ax, 52, 46, 34, 8, 'resultat', label='loi des cosinus')
save(fig, '27-122')
