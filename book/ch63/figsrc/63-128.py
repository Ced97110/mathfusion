import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Ellipse
fig, ax = canvas(80)
text(ax, 22, 74, r'$H=\{1,\tau\}$ fixe $r$', 'sujet', 's')
box(ax, 2, 24, 44, 40, 'fixe')
names = ['1', r'$\sigma$', r'$\sigma^2$', r'$\tau$', r'$\sigma\tau$', r'$\sigma^2\tau$']
for k, l in enumerate(names):
    x = 10 + (k % 3) * 14
    y = 54 if k < 3 else 34
    disc(ax, x, y, 4.5, 'encre', label=l, size='s')
box(ax, 4.5, 28, 11, 31, 'varie', fill=False, lw=1.5)
text(ax, 22, 15, 'non normal', 'limite', 'm')
text(ax, 55, 44, r'$\Leftrightarrow$', 'encre', 'xl')
cx, cy, R = 68, 44, 9
text(ax, 68, 74, r'$\mathrm{Inv}\,H=\mathbb{Q}(r)$', 'autre', 's')
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=1))
ax.add_patch(Ellipse((cx + R, cy), 9, 7, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=1.2))
for k, l in enumerate([r'$r$', r'$jr$', r'$j^2r$']):
    a = math.radians(120 * k)
    role = 'resultat' if k == 0 else 'limite'
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2, role)
    text(ax, cx + (R + 7) * math.cos(a), cy + (R + 5) * math.sin(a), l, role, 's')
text(ax, 68, 15, 'non galoisienne', 'limite', 'm')
save(fig, '63-128')
