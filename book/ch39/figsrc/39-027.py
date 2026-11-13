import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
s = 1.5
O = (8, 32)
H = (O[0] + 34.64 * s, 32)
P = (H[0], 32 + 20 * s)
line(ax, [O, P], 'fixe')
line(ax, [H, P], 'fixe', dash=True)
line(ax, [O, H], 'sujet', lw=2.4)
m = 2.2
line(ax, [(H[0] - m, 32), (H[0] - m, 32 + m), (H[0], 32 + m)], 'fixe', lw=0.6)
pts = [(O[0] + 9 * math.cos(math.radians(30 * k / 20)), 32 + 9 * math.sin(math.radians(30 * k / 20))) for k in range(21)]
line(ax, pts, 'varie', lw=1.0)
text(ax, 22, 36, r'$\theta$', 'varie', 's')
text(ax, O[0] - 1, 32 + 3, r'$O$', 'fixe', 'm', ha='right')
text(ax, H[0], 27.5, r'$H$', 'fixe', 'm')
text(ax, P[0], P[1] + 4.5, r'$P$', 'fixe', 'm')
text(ax, 31, 27.5, r'$x$', 'sujet', 'm')
text(ax, 28, 52, r'$r = 40$ km', 'fixe', 's', rot=29.98)
text(ax, 6, 19, r'1. $\cos\theta = x / r$', 'encre', 's', ha='left')
text(ax, 6, 11.5, r'2. $x = r\cos\theta$', 'encre', 's', ha='left')
text(ax, 6, 4, r'3. $x = 40 \times 0{,}866 \approx 34{,}64$', 'resultat', 's', ha='left')
save(fig, '39-027')
