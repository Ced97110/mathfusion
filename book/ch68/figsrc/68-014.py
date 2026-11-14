import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(77)
S, dx, dy, x0, y0 = 28, 14, 11, 23, 19
words = [format(k, '03b') for k in range(8)]
P = lambda w: (x0 + int(w[0]) * S + int(w[2]) * dx, y0 + int(w[1]) * S + int(w[2]) * dy)
for a in words:
    for b in words:
        if a < b and sum(p != q for p, q in zip(a, b)) == 1:
            line(ax, [P(a), P(b)], 'fixe', lw=0.8, dash=(a[2] != b[2] or a[2] == '1'))
cx, cy = x0 + S / 2 + dx / 2, y0 + S / 2 + dy / 2
for w in words:
    x, y = P(w)
    blue = w.count('1') <= 1
    big = w in ('000', '111')
    r = 4.2 if big else 3
    disc(ax, x, y, r, 'sujet' if blue else 'varie')
    if big:
        ax.add_patch(Circle((x, y), r + 1.0, ec=COL['encre'], fc='none', lw=1.4, zorder=3))
    vx, vy = x - cx, y - cy
    n = math.hypot(vx, vy)
    text(ax, x + vx / n * 7.5, y + vy / n * 7.5, w, 'sujet' if blue else 'varie', 's')
text(ax, 44, 73, 'anneau noir = mot envoyé', 'encre', 's')
disc(ax, 6, 3, 1.8, 'sujet'); text(ax, 9.5, 3, 'à un pas de 000 au plus', 'sujet', 's', ha='left')
disc(ax, 50, 3, 1.8, 'varie'); text(ax, 53.5, 3, 'à un pas de 111 au plus', 'varie', 's', ha='left')
save(fig, '68-014')
