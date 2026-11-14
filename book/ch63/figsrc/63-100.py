import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Ellipse
fig, ax = canvas(66)

def plane(cx, cy, R, inside, region, title, cap, crole):
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=1))
    ax.add_patch(region)
    names = [r'$r$', r'$jr$', r'$j^2r$']
    for k in range(3):
        a = math.radians(120 * k)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        role = 'resultat' if k < inside else 'limite'
        disc(ax, x, y, 2, role)
        text(ax, cx + (R + 5.5) * math.cos(a), cy + (R + 4) * math.sin(a), names[k], role, 's')
    text(ax, cx, 56, title, 'sujet', 'm')
    text(ax, cx, 6, cap, crole, 's')

plane(22, 30, 9, 1, Ellipse((31, 30), 9, 7, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=1.2),
      r'$\mathbb{Q}(r)$', '1 racine sur 3 : échoue', 'limite')
plane(66, 30, 9, 3, Ellipse((66, 30), 34, 30, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=0.5),
      r'$\mathbb{Q}(r,\,j)$', '3 racines sur 3 : réussit', 'resultat')
save(fig, '63-100')
