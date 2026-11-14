import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
line(ax, [(54, 6), (54, 50)], 'fixe', lw=0.6, dash=True)
gy = 16
A, B, S = (6, gy), (22, gy), (40, 38)
def ext(p, q, k):
    return (q[0] + (q[0] - p[0]) * k, q[1] + (q[1] - p[1]) * k)
line(ax, [(2, gy), (50, gy)], 'fixe')
line(ax, [A, ext(A, S, 0.18)], 'sujet', lw=1.3)
line(ax, [B, ext(B, S, 0.18)], 'varie', lw=1.3)
for p, r in ((A, 'sujet'), (B, 'varie'), (S, 'resultat')):
    disc(ax, p[0], p[1], 1.3, r)
text(ax, A[0], gy - 5, '$A$', 'sujet', 's')
text(ax, B[0], gy - 5, '$B$', 'varie', 's')
text(ax, S[0] - 4, S[1] + 3, '$S$', 'resultat', 'm')
text(ax, 26, 50, 'un seul point $S$', 'resultat', 's')
text(ax, 26, 6, 'à l’échelle ou par calcul', 'fixe', 's')
# droites parallèles : aucun point commun
line(ax, [(60, 14), (84, 40)], 'limite', lw=1.3)
line(ax, [(66, 10), (86, 31)], 'limite', lw=1.3)
text(ax, 72, 50, 'parallèles', 'limite', 's')
text(ax, 72, 6, 'aucun point commun', 'limite', 's')
save(fig, '38-018')
