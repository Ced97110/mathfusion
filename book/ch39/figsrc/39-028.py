import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
k = 0.45
text(ax, 44, 79, r'$y = r\sin\theta$', 'sujet', 'l')
rows = [(58, 40, 30, 'y = 40 × 0,5 = 20 km'),
        (33, 40, 60, 'y = 40 × 0,866 ≈ 34,64 km'),
        (8, 80, 30, 'y = 80 × 0,5 = 40 km')]
for base, r, th, res in rows:
    a = math.radians(th)
    O = (6, base)
    H = (6 + r * k * math.cos(a), base)
    P = (H[0], base + r * k * math.sin(a))
    line(ax, [O, P], 'fixe')
    line(ax, [O, H], 'fixe')
    line(ax, [H, P], 'sujet', lw=2.4)
    line(ax, [(H[0] - 2, base), (H[0] - 2, base + 2), (H[0], base + 2)], 'fixe', lw=0.6)
    pts = [(6 + 6 * math.cos(a * j / 20), base + 6 * math.sin(a * j / 20)) for j in range(21)]
    line(ax, pts, 'varie', lw=0.9)
    text(ax, 46, base + 8, f'r = {r} km ; θ = {th}°', 'varie', 's', ha='left')
    text(ax, 46, base + 2.5, res, 'sujet', 's', ha='left')
save(fig, '39-028')
