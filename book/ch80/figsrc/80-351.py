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

fig, ax = canvas(112)
A, B, C, Z, L = venn(ax, 44, 82, 22, 26)
for k, s, r in (('A', 'A : 10', 'sujet'), ('B', 'B : 8', 'varie'), ('C', 'C : 6', 'autre')):
    text(ax, L[k][0], L[k][1], s, r, 'm', weight='bold')
x, y = Z['A']; disc(ax, x - 7, y, 1.7, 'fixe'); text(ax, x - 4, y, 'un seul club', 'fixe', 's', ha='left')
x, y = Z['AB']; disc(ax, x - 5, y, 1.7, 'varie'); text(ax, x - 2.5, y, 'Léa', 'varie', 's', ha='left')
x, y = Z['ABC']; disc(ax, x - 5.5, y, 1.7, 'resultat'); text(ax, x - 3, y, 'Paul', 'resultat', 's', ha='left')
text(ax, 44, 16, r'Léa : $2 - 1 = 1$ fois', 'varie', 's')
text(ax, 44, 10, r'Paul : $3 - 3 + 1 = 1$ fois', 'resultat', 's')
text(ax, 44, 4.5, r'le $+1$ est $A\cap B\cap C$', 'resultat', 's')
save(fig, '80-351')
