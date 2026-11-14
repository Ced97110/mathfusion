import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
gy = 14
A, B, S = (8, gy), (30, gy), (66, 40)
line(ax, [(2, gy), (86, gy)], 'fixe')
poly(ax, [A, B, S], 'fixe')
# prolongements : une seule visée laisse S n'importe où sur sa droite
def ext(p, q, k):
    return (q[0] + (q[0] - p[0]) * k, q[1] + (q[1] - p[1]) * k)
line(ax, [S, ext(A, S, 0.2)], 'sujet', lw=0.8, dash=True)
line(ax, [S, ext(B, S, 0.2)], 'varie', lw=0.8, dash=True)
line(ax, [A, S], 'sujet', lw=1.4)
line(ax, [B, S], 'varie', lw=1.4)
for p, r in ((A, 'sujet'), (B, 'varie'), (S, 'resultat')):
    disc(ax, p[0], p[1], 1.4, r)
text(ax, A[0], gy - 5, '$A$', 'sujet', 'm')
text(ax, B[0], gy - 5, '$B$', 'varie', 'm')
text(ax, S[0] - 2, S[1] + 4, '$S$', 'resultat', 'l')
text(ax, 24, 30, 'visée depuis $A$', 'sujet', 's')
text(ax, 54, 14 + 5, 'visée depuis $B$', 'varie', 's')
text(ax, 62, 50, 'les deux se coupent en $S$', 'resultat', 's')
save(fig, '38-009')
