import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cw, x0 = 9, 13
A = {0: 3, 3: 2}; B = {0: 2, 2: -1, 4: 4}
P = {}
for j, a in A.items():
    for k, b in B.items():
        P[j + k] = P.get(j + k, 0) + a * b
assert P == {0: 6, 2: -3, 3: 4, 4: 12, 5: -2, 7: 8}, P
f = lambda v: str(v).replace('-', '−')
def row(d, n, y, role, hi):
    for r in range(n):
        if r in d:
            rl = hi.get(r, role)
            box(ax, x0 + r * cw + 0.3, y, cw - 0.6, 8, rl, label=f(d[r]), size='s')
        else:
            box(ax, x0 + r * cw + 0.3, y, cw - 0.6, 8, 'fixe', fill=False, dash=True)
text(ax, 6, 58, r'$p$', 'sujet', 'l')
text(ax, 6, 46, r'$q$', 'autre', 'l')
text(ax, 6, 20, r'$pq$', 'resultat', 'l')
row(A, 4, 54, 'sujet', {0: 'varie', 3: 'varie'})
row(B, 5, 42, 'autre', {2: 'varie', 4: 'varie'})
row(P, 8, 16, 'resultat', {})
text(ax, x0 + 2.5 * cw, 30, 'rang 2', 'varie', 's')
text(ax, x0 + 7.5 * cw, 30, 'rang 7', 'varie', 's')
arrow(ax, (x0 + 2.5 * cw, 28), (x0 + 2.5 * cw, 25), 'varie')
arrow(ax, (x0 + 7.5 * cw, 28), (x0 + 7.5 * cw, 25), 'varie')
text(ax, 44, 8, r'rang 2 : $3\times(-1)=-3$', 'varie', 's')
text(ax, 44, 3, r'rang 7 : $2\times4=8$', 'varie', 's')
save(fig, '54-093')
