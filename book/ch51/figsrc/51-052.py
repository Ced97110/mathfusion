import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
n, bw, g = 7, 8.5, 3.0
x0 = (88 - (n * bw + (n - 1) * g)) / 2
for i in range(n):
    x = x0 + i * (bw + g)
    box(ax, x, 36, bw, 9, 'sujet', label='3', size='m')
    if i < n - 1:
        cx = x + bw + g / 2; line(ax, [(cx - 1.1, 40.5), (cx + 1.1, 40.5)], 'encre', lw=0.8); line(ax, [(cx, 39.4), (cx, 41.6)], 'encre', lw=0.8)
brace(ax, x0, 88 - x0, 36, 'varie', label='7 termes', down=True)
arrow(ax, (44, 22), (44, 14), 'resultat')
box(ax, 22, 3, 44, 10, 'resultat', label=r'$nr$ avec $n=7$, $r=3$', size='m')
text(ax, 44, 51, r'$r+\cdots+r$ ($n$ termes)', 'sujet', 'm')
save(fig, '51-052')
