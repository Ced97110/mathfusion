import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
items = [(r'$2$', ['2'], r'$2^1$'), (r'$4$', ['2', '2'], r'$2\times2=2^2$'), (r'$3$', ['3'], r'$3^1$')]
bw, gap, x0, y0, bh = 24, 4, 4, 14, 30
for i, (head, ps, expo) in enumerate(items):
    x = x0 + i * (bw + gap); cx = x + bw / 2
    box(ax, x, y0, bw, bh, 'resultat')
    text(ax, cx, y0 + bh - 5, head, 'encre', 'l', weight='bold')
    n = len(ps)
    for j, p in enumerate(ps):
        dx = (j - (n - 1) / 2) * 9
        disc(ax, cx + dx, y0 + 14, 4, 'sujet' if p == '2' else 'autre', label=p)
    text(ax, cx, y0 + 4, expo, 'encre', 's')
brace(ax, x0, x0 + 3 * bw + 2 * gap, 12, 'resultat', label='un seul premier, répété')
save(fig, '50-018')
