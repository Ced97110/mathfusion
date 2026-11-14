import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
import math
s = 0.5; cx, cy = 8, 10
a53 = math.radians(53)
C = (cx, cy); B = (cx + 110 * s, cy); A = (cx + 120 * s * math.cos(a53), cy + 120 * s * math.sin(a53))
t = 110 * math.cos(a53) * s
F = (cx + t * math.cos(a53), cy + t * math.sin(a53))
poly(ax, [C, B, A], 'sujet')
from matplotlib.patches import Arc
ax.add_patch(Arc(C, 18, 18, theta1=0, theta2=53, ec=COL['varie'], lw=1.2, zorder=4))
line(ax, [B, F], 'varie', dash=True, lw=1.2)
d = 2.6; ux, uy = math.cos(a53), math.sin(a53); vx, vy = (B[0] - F[0]), (B[1] - F[1]); n = math.hypot(vx, vy); vx, vy = vx / n, vy / n
line(ax, [(F[0] + d * ux, F[1] + d * uy), (F[0] + d * (ux + vx), F[1] + d * (uy + vy)), (F[0] + d * vx, F[1] + d * vy)], 'varie', lw=0.8)
text(ax, (C[0] + B[0]) / 2, cy - 3.5, '110 m', 'sujet')
text(ax, 17, 38, '120 m', 'sujet', ha='center')
text(ax, 22.5, 13.5, '53°', 'varie', 's')
text(ax, 31, 25, r'$h \approx 87{,}8$ m', 'varie', 's')
text(ax, 71, 62, r'$\frac{1}{2}\times110\times120 = 6\,600$', 'sujet', 's')
text(ax, 71, 55, r'$\times\ \sin 53° \approx 0{,}7986$', 'sujet', 's')
box(ax, 57, 44, 28, 7, 'resultat', label=r'$\Delta \approx 5\,271$ m²', size='s')
save(fig, '37-108')
