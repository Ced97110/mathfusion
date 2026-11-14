import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
px = {p: 24 + 16 * (p - 1) for p in range(1, 5)}
ys = [52 - 12.5 * s for s in range(4)]
pos = {c: c for c in range(1, 5)}
steps = [(1, 2), (1, 3), (1, 4)]
for c in range(1, 5):
    text(ax, px[c], 58, str(c), 'sujet', 'l')
for s, (a, b) in enumerate(steps):
    new = {c: (b if p == a else a if p == b else p) for c, p in pos.items()}
    for c in pos:
        moved = new[c] != pos[c]
        line(ax, [(px[pos[c]], ys[s]), (px[new[c]], ys[s + 1])], 'varie' if moved else 'fixe', lw=1.3 if moved else 0.9)
    text(ax, 2, (ys[s] + ys[s + 1]) / 2, f'({a} {b})', 'varie', 'm', ha='left')
    pos = new
inv = {p: c for c, p in pos.items()}
for p in range(1, 5):
    text(ax, px[p], 8, str(inv[p]), 'resultat', 'l')
save(fig, '46-195')
