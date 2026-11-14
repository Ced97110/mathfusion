import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
E = [(0, 0), (1, 0), (0, 1), (1, 1)]  # (a, b) = a + b*alpha, alpha^2 = alpha + 1
N = ['0', '1', r'$\alpha$', r'$\alpha+1$']
def add(p, q): return ((p[0] + q[0]) % 2, (p[1] + q[1]) % 2)
def mul(p, q):
    a, b = p; c, d = q
    return ((a * c + b * d) % 2, (a * d + b * c + b * d) % 2)
def table(x0, title, op, sym, hi):
    text(ax, x0 + 20, 55, title, 'encre', 'm')
    text(ax, x0 + 4, 46, sym, 'encre', 'm')
    for j in range(4): text(ax, x0 + 8 + 8 * j + 4, 46, N[j], 'sujet', 's')
    for i in range(4):
        text(ax, x0 + 4, 38 - 8 * i + 0, N[i], 'sujet', 's')
        for j in range(4):
            r = op(E[i], E[j]); v = N[E.index(r)]
            box(ax, x0 + 8 + 8 * j, 34 - 8 * i, 8, 8, 'resultat' if hi(E[i], E[j], r) else 'fixe', label=v, size='s', r=0.4, lw=0.5)
table(2, 'Addition', add, '+', lambda p, q, r: r == (0, 0))
table(46, 'Multiplication', mul, '×', lambda p, q, r: r == (1, 0))
text(ax, 44, 5, 'vert : les 0 (haut), les 1 (bas)', 'encre', 's')
save(fig, '67-011')
