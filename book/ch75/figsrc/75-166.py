import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(70)
ox, oy, R = 12, 8, 38
ax.add_patch(Circle((ox, oy), R, ec=COL['sujet'], fc='none', lw=1.0, zorder=1, ls='--'))
ax.set_xlim(0, W); ax.set_ylim(0, 70)
arrow(ax, (ox-4, oy), (ox+R+6, oy), 'fixe', lw=0.8)
px, py = ox + 0.6*R, oy + 0.8*R
poly(ax, [(ox, oy), (px, oy), (px, py)], 'sujet')
line(ax, [(ox, oy), (px, py)], 'varie', lw=1.4)
disc(ax, px, py, 1.4, 'varie')
text(ax, (ox+px)/2, oy-3.5, r'$a$ = 0,6', 'sujet', 'm')
text(ax, px+3, (oy+py)/2-8, r'$b$ = 0,8', 'sujet', 's', ha='left')
text(ax, ox+9, oy+17, 'distance 1', 'varie', 'm', rot=0, ha='right')
text(ax, 68, 62, r'$U(1)$ : cercle unité', 'sujet', 'm', weight='bold')
text(ax, 68, 53, r'$a^2+b^2=1$', 'resultat', 'l')
text(ax, 68, 46, '0,36 + 0,64 = 1', 'resultat', 's')
save(fig, '75-166')
