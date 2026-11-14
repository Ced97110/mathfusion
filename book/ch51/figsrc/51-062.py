import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
s, g = 7.0, 1.5
groups = [(4, 'sujet', '1 · addition', '4 règles'), (2, 'autre', '2 · multiplication', '2 règles'), (2, 'varie', '3 · le pont', '2 règles')]
gap = 6
total = sum(n * s + (n - 1) * g for n, *_ in groups) + gap * 2
x = (88 - total) / 2
prev = None
for n, role, name, cnt in groups:
    w_ = n * s + (n - 1) * g
    for i in range(n): box(ax, x + i * (s + g), 26, s, s, role)
    text(ax, x + w_ / 2, 40, name, role, 's')
    brace(ax, x, x + w_, 26, role, label=cnt, down=True)
    if prev is not None: arrow(ax, (prev + 0.8, 29.5), (x - 0.8, 29.5), 'fixe')
    prev = x + w_; x += w_ + gap
text(ax, 44, 8, '8 règles, lues en trois temps', 'encre', 'm')
save(fig, '51-062')
