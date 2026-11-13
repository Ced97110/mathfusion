import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, cy, kx, ky = 44, 38, 0.2, 7.0
X = lambda d: x0 + d * kx
T = lambda d: math.tan(math.radians(d))
line(ax, [(8, cy), (82, cy)], 'fixe', lw=0.7)
ax.add_patch(Rectangle((X(-90), cy - 0.9), X(90) - X(-90), 1.8, fc=FILL['resultat'], ec=COL['resultat'], lw=0.6, zorder=1))
for d in (-90, 90): line(ax, [(X(d), cy - 26), (X(d), cy + 26)], 'fixe', lw=0.6, dash=True)
for m, role, lw in ((-1, 'fixe', 1.2), (0, 'sujet', 2.0), (1, 'fixe', 1.2)):
    pts = [(X(d), cy + T(d) * ky) for d in range(max(-180, -90 + 180 * m + 1), min(180, 90 + 180 * m - 1) + 1) if abs(T(d)) <= 3.6]
    line(ax, pts, role, lw=lw)
yy = cy + T(108) * ky
line(ax, [(X(-72), yy), (X(108), yy)], 'fixe', lw=0.7, dash=True)
disc(ax, X(-72), yy, 1.7, 'resultat'); disc(ax, X(108), yy, 1.7, 'sujet')
text(ax, X(-72) - 3, yy + 4.5, '−72°', 'resultat', 's'); text(ax, X(108) + 6, yy + 4.5, '108°', 'sujet', 's')
brace(ax, X(-72), X(108), yy - 4, 'varie', label='180°')
text(ax, X(-90), cy + 4, '−90°', 'resultat', 's'); text(ax, X(90), cy - 4, '90°', 'resultat', 's')
text(ax, 70, 62, r'$\tan x$', 'sujet', 's')
save(fig, '33-109')
