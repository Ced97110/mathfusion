import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
items = [('2', ['2']), ('3', ['3']), ('4', ['2', '2']), ('6', ['2', '3'])]
bw, gap, x0, y0, bh = 18, 3.3, 3, 18, 28
for i, (head, ps) in enumerate(items):
    x = x0 + i * (bw + gap); cx = x + bw / 2
    bad = head == '6'
    box(ax, x, y0, bw, bh, 'limite' if bad else 'resultat', lw=1.6 if bad else 0.8)
    text(ax, cx, y0 + bh - 5, head, 'encre', 'l', weight='bold')
    n = len(ps)
    for j, p in enumerate(ps):
        dx = (j - (n - 1) / 2) * 8
        disc(ax, cx + dx, y0 + 11, 3.4, 'sujet' if p == '2' else 'autre', label=p)
brace(ax, x0, x0 + 2 * (bw + gap) + bw, 17, 'resultat', label='un seul premier')
text(ax, 85, 13.3, 'deux premiers différents', 'limite', 's', ha='right')
save(fig, '50-019')
