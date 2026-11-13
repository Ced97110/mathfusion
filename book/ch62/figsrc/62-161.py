import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
# vérification : dans F2[x]/(x^3+x+1), les 8 éléments annulent x^8 - x
MOD = 0b1011
def mul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1
        if a & 0b1000: a ^= MOD
        b >>= 1
    return r
def pw(a, n):
    r = 1
    for _ in range(n): r = mul(r, a)
    return r
assert all(pw(a, 8) == a for a in range(8))
labels = ['0', '1', r'$r_1$', r'$r_1+1$', r'$r_1^2$', r'$r_1^2+1$', r'$r_1^2+r_1$', r'$r_1^2+r_1+1$']
assert len(labels) == 8 == 2 ** 3
box(ax, 14, 72, 60, 11, 'autre', label=r'$x^8-x$ sur ℤ/2ℤ')
arrow(ax, (44, 72), (44, 62), 'varie', lw=1.2)
text(ax, 49, 67, 'corps de décomposition', 'varie', 's', ha='left')
box(ax, 2, 8, 84, 53, 'resultat')
text(ax, 44, 55, r'K : $2^3=8$ éléments', 'resultat', 'm', weight='bold')
for k, l in enumerate(labels):
    col, row = k % 4, k // 4
    box(ax, 5 + 20.5 * col, 34 - 14 * row, 18.5, 10, 'sujet', label=l, size='s')
text(ax, 44, 13, '8 racines = les 8 éléments', 'resultat', 's')
save(fig, '62-161')
