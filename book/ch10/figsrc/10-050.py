import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
n = 10; bw = 6.4; gap = 2.0; x0 = (W - (n * bw + (n - 1) * gap)) / 2
for i in range(n):
    x = x0 + i * (bw + gap)
    box(ax, x, 40, bw, 8, 'sujet', label='50', size='s')
    if i < n - 1:
        cx = x + bw + gap / 2
        line(ax, [(cx - 0.7, 44), (cx + 0.7, 44)], 'varie', lw=0.9); line(ax, [(cx, 43.3), (cx, 44.7)], 'varie', lw=0.9)
brace(ax, x0, x0 + n * bw + (n - 1) * gap, 40, 'varie', label='9 additions')
box(ax, x0, 8, n * bw + (n - 1) * gap, 9, 'resultat', label=r'$10 \times 50 = 500$', size='l')
text(ax, 44, 22, '1 multiplication', 'resultat', 's')
text(ax, 44, 56, 'dix fois le même 50', 'fixe', 's')
save(fig, '10-050')
