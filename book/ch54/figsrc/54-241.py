import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, r'dans $\mathbb{Z}/8$ : $x \to x^2-1$ modulo 8', 'sujet', 's')
for x in range(8):
    v = (x * x - 1) % 8
    root = v == 0
    col, row = x % 2, x // 2
    box(ax, 4 + col * 42, 48 - row * 11, 38, 9, 'resultat' if root else 'fixe', label=f'{x} → {v}')
assert [x for x in range(8) if (x * x - 1) % 8 == 0] == [1, 3, 5, 7]
box(ax, 4, 3, 80, 11, 'limite', label=r'4 racines (1, 3, 5, 7) $>$ degré 2')
save(fig, '54-241')
