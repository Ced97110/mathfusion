import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(58)
x0, k = 17, 6
t = 4.092 * k
box(ax, x0, 34, t, 8, 'varie', label='4,092', size='s')
box(ax, x0 + t, 34, 4.908 * k, 8, 'resultat', label='4,908', size='s')
brace(ax, x0, x0 + 9 * k, 42, 'fixe', label='secteur : 9 cm²', down=False)
brace(ax, x0 + 0.5, x0 + t - 0.5, 34, 'varie', label='triangle')
brace(ax, x0 + t + 0.5, x0 + 9 * k, 34, 'resultat', label='segment')
text(ax, 44, 17, r'$9 - 4{,}092 = 4{,}908$ cm$^2$', 'resultat', 'l')
text(ax, 44, 8, r'triangle $= \frac{1}{2}\times PQ \times ON$', 'fixe', 's')
save(fig, '29-099')
