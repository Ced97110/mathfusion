import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def venn(ax, cx, cy, r, d):
    A = (cx - d / 2, cy); B = (cx + d / 2, cy); C = (cx, cy - d * 0.866)
    for p, role in ((A, 'sujet'), (B, 'varie'), (C, 'autre')):
        disc(ax, p[0], p[1], r, role, fill=False, lw=1.3)
    g = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
    def away(p, q, k):
        dx, dy = p[0] - q[0], p[1] - q[1]; n = math.hypot(dx, dy)
        return (p[0] + dx / n * k, p[1] + dy / n * k)
    mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    Z = {'A': away(A, g, .55 * r), 'B': away(B, g, .55 * r), 'C': away(C, g, .55 * r), 'ABC': g,
         'AB': away(mid(A, B), C, .43 * r), 'AC': away(mid(A, C), B, .43 * r), 'BC': away(mid(B, C), A, .43 * r)}
    L = {'A': away(A, g, r + 4.5), 'B': away(B, g, r + 4.5), 'C': away(C, g, r + 4.5)}
    return A, B, C, Z, L

fig, ax = canvas(96)
A, B, C, Z, L = venn(ax, 44, 68, 24, 24)
for k, s in (('A', '1'), ('B', '1'), ('C', '1')):
    text(ax, Z[k][0], Z[k][1], s, 'resultat', 'l')
for k in ('AB', 'AC', 'BC'):
    text(ax, Z[k][0], Z[k][1], r'$2-1=1$', 'resultat', 's')
text(ax, Z['ABC'][0], Z['ABC'][1], r'$3-3+1=1$', 'resultat', 's')
for k, s, r in (('A', 'A', 'sujet'), ('B', 'B', 'varie'), ('C', 'C', 'autre')):
    text(ax, L[k][0], L[k][1], s, r, 'l', weight='bold')
save(fig, '80-349')
