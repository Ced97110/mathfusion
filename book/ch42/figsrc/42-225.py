import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def link(ax, pa, pb, role, dy=0.0, curve=0.0):
    s = 1 if pb[0] > pa[0] else -1
    arrow(ax, (pa[0] + s * R, pa[1] + dy), (pb[0] - s * R, pb[1] + dy), role, curve=curve)
fig, ax = canvas(84)
xs = (14, 44, 74)
A = [60, 49, 38, 27]; B = [55, 43.5, 32]; C = [49, 37]
for x, t in zip(xs, ('$A$', '$B$', '$C$')): text(ax, x, 72, t, 'sujet', 'l')
text(ax, 29, 66, '$f$', 'sujet', 's'); text(ax, 59, 66, '$g$', 'sujet', 's')
for x, Y in zip(xs, (A, B, C)):
    for y in Y: disc(ax, x, y, R, 'sujet')
F = [(0, 0), (1, 0), (2, 1), (3, 2)]; G = [(0, 0), (1, 1), (2, 1)]
for i, j in F: link(ax, (xs[0], A[i]), (xs[1], B[j]), 'resultat' if (i, j) == (0, 0) or (i, j) == (2, 1) else 'sujet')
for j, k in G: link(ax, (xs[1], B[j]), (xs[2], C[k]), 'resultat' if (j, k) in ((0, 0), (1, 1)) else 'sujet')
text(ax, 29, 17, '$f$ surjective', 'sujet', 's'); text(ax, 59, 17, '$g$ surjective', 'sujet', 's')
text(ax, 44, 9, r'$g\circ f$ : chaque point de $C$', 'resultat', 'm')
text(ax, 44, 3.5, 'se remonte jusqu\u2019à $A$', 'resultat', 'm')
save(fig, '42-225')
