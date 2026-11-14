import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(60)
k = 12.5; A = (6, 10); H = (A[0]+5*k, 10); G = (H[0], 10+2*k)
poly(ax, [A, H, G], 'sujet')
line(ax, [(H[0]-3, 10), (H[0]-3, 13), (H[0], 13)], 'sujet')
text(ax, 30, 31, 'AG ≈ 5,385 m', 'sujet', 's')
text(ax, 34, 5, 'AH = 5 m (projeté)', 'resultat', 's')
ax.add_patch(Arc(A, 28, 28, theta1=0, theta2=21.8, color=COL['varie'], lw=1))
text(ax, 25, 13, '21,80°', 'varie', 's')
text(ax, 48, 54, 'AH = AG cos α', 'sujet', 'm')
arrow(ax, (48, 51), (48, 47.5), 'varie')
box(ax, 26, 39, 44, 8, 'autre', label='produit scalaire')
save(fig, '27-125')
