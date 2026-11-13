import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ox, oy, kx, ky = 44, 32, 4.4, 14.0; q = math.pi / 2
xt = [-8 + 16 * i / 160 for i in range(161)]
line(ax, [(ox - 38, oy), (ox + 38, oy)], 'fixe', lw=0.5); line(ax, [(ox, oy - 25), (ox, oy + 25)], 'fixe', lw=0.5)
for s in (1, -1): line(ax, [(ox - 38, oy + s * q * ky), (ox + 38, oy + s * q * ky)], 'fixe', lw=0.9, dash=True)
line(ax, [(ox + x * kx, oy + math.atan(x) * ky) for x in xt], 'resultat', lw=1.9)
disc(ax, ox + kx, oy + math.pi / 4 * ky, 1.3, 'resultat')
text(ax, ox + kx + 2, oy + math.pi / 4 * ky - 5, 'pente 1 : 45°', 'resultat', 's', ha='left')
text(ax, ox - 37, oy + q * ky + 3, r'$\pi/2$ = 90°', 'fixe', 's', ha='left'); text(ax, ox - 37, oy - q * ky - 3, r'$-\pi/2$ = −90°', 'fixe', 's', ha='left')
xe = ox + 8 * kx; ye = oy + math.atan(8) * ky
arrow(ax, (xe, ye + 0.3), (xe, oy + q * ky - 0.3), 'varie', lw=1.0)
text(ax, ox + 30, oy + q * ky + 8, 'jamais atteint', 'varie', 's')
arrow(ax, (ox + 30, oy + q * ky + 5.5), (xe - 1, oy + q * ky + 0.8), 'varie', lw=0.8)
text(ax, ox - 22, oy - 6.5, 'la courbe monte', 'resultat', 's') if False else None
save(fig, '33-078')
