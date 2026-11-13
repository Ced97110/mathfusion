import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(86)
ox, oy, R = 40, 43, 30
th = np.linspace(0, 2*math.pi, 200) if 'np' in globals() else [i*2*math.pi/200 for i in range(201)]
ax.add_patch(Circle((ox, oy), R, ec=COL['sujet'], fc=FILL['sujet'], lw=1.3, zorder=1))
arrow(ax, (ox-R-5, oy), (ox+R+6, oy), 'fixe', lw=0.8)
line(ax, [(ox, oy-R-4), (ox, oy+R+4)], 'fixe', lw=0.6)
zx, zy = ox + 0.6*R, oy + 0.8*R
cx, cy = zx, oy - 0.8*R
line(ax, [(ox, oy), (zx, zy)], 'varie'); line(ax, [(ox, oy), (cx, cy)], 'autre')
line(ax, [(zx, zy), (cx, cy)], 'fixe', dash=True)
disc(ax, zx, zy, 1.4, 'varie'); disc(ax, cx, cy, 1.4, 'autre')
text(ax, zx+4, zy+2, r'$z$', 'varie', 'l', weight='bold')
text(ax, cx+4, cy-2, r'$\bar z$', 'autre', 'l', weight='bold')
def arc(r, a0, a1, role):
    n = 30; line(ax, [(ox + r*math.cos(a0+(a1-a0)*k/n), oy + r*math.sin(a0+(a1-a0)*k/n)) for k in range(n+1)], role, lw=0.8)
a = math.atan2(0.8, 0.6)
arc(10, 0, a, 'varie'); arc(10, -a, 0, 'autre')
text(ax, ox+15, oy+4, r'$\theta$', 'varie', 's'); text(ax, ox+16, oy-4.5, r'$-\theta$', 'autre', 's')
text(ax, ox-14, oy+16, r'$U(1)$', 'sujet', 'l', weight='bold')
text(ax, ox-14, oy-14, r'$z\bar z=1$', 'sujet', 'm')
text(ax, ox+R+6, oy+3, 'axe réel', 'fixe', 's', ha='right')
save(fig, '75-165')
