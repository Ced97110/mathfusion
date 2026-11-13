import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
g = 34.0
h = 16.0
xs = 80.0
A = (xs - h / math.tan(math.radians(18)), g)
B = (xs - h / math.tan(math.radians(21.25)), g)
S = (xs, g + h)
poly(ax, [A, B, S], 'resultat')
line(ax, [(A[0] - 6, g), (xs + 3, g)], 'fixe', lw=0.7)
line(ax, [S, (xs, g)], 'fixe', dash=True, lw=0.7)
text(ax, S[0], S[1] + 3, 'S', 'sujet', 's')
text(ax, A[0] - 1, g - 3.5, 'A : α = 18°', 'fixe', 's', ha='right')
text(ax, B[0] + 1, g - 3.5, 'B : β = 21,25°', 'fixe', 's', ha='left')
text(ax, 42, g + 17, 'angle en S : 3,25°', 'resultat', 's', weight='bold')
arrow(ax, (54, g + 15), (66, g + 9.5), 'resultat', curve=-0.2)
text(ax, 44, 22, 'β − α = 21,25° − 18° = 3,25°', 'resultat', 's', weight='bold')
box(ax, 2, 2, 41, 14, 'resultat', label=r'$\sin(\beta-\alpha)$ ≈ 0,05669', size='s')
box(ax, 45, 2, 41, 14, 'limite', label=r'$\sin\beta-\sin\alpha$ ≈ 0,05342', size='s')
text(ax, 22, 18.5, 'on soustrait d’abord', 'resultat', 's')
text(ax, 66, 18.5, 'faux', 'limite', 's', weight='bold')
save(fig, '38-038')
