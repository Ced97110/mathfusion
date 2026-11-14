import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(52)
text(ax, 44, 48, r'$OH=\|u\|\cos\theta$', 'resultat', 'l')
L = 5 * math.sqrt(10)      # 5 mm par unité, ‖u‖ = √10
panels = [(2, 0, r'$\theta=0^\circ$', r'$OH=\|u\|$'),
          (31, 45, r'$\theta=45^\circ$', r'$OH\approx2{,}236$'),
          (60, 90, r'$\theta=90^\circ$', r'$OH=0$')]
for x0, ang, head, val in panels:
    ox, oy = x0 + 3, 20
    ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    arrow(ax, (ox, oy), (ox + 22, oy), 'autre', lw=1.0)
    tip = (ox + L * ca, oy + L * sa)
    if ang == 0:
        arrow(ax, (ox, oy + 0.0), tip, 'sujet', lw=1.8)
    else:
        arrow(ax, (ox, oy), tip, 'sujet', lw=1.8)
    line(ax, [tip, (tip[0], oy)], 'fixe', lw=0.8, dash=True)
    ax.plot([ox, tip[0]], [oy - 3.5, oy - 3.5], color=COL['resultat'], lw=3.0, zorder=4, solid_capstyle='butt')
    ax.plot([ox, ox], [oy - 3.5, oy], color=COL['fixe'], lw=0.6, ls='--', zorder=1)
    if ang == 90: ax.plot([ox], [oy - 3.5], marker='o', ms=4, color=COL['resultat'], zorder=5)
    text(ax, ox + 12, oy + 21, head, 'encre', 's')
    text(ax, ox + 12, oy - 9, val, 'resultat', 's')
text(ax, 14, 23.5, r'$u$', 'sujet', 'm')
text(ax, 25, 16.5, r'$v$', 'autre', 'm')
save(fig, '41-095')
