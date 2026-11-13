import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig, ax = canvas(64)
def rect(x0, y0, x1, y1, role):
    ax.add_patch(Rectangle((x0,y0), x1-x0, y1-y0, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
def sq(x0, role, full):
    y0 = 22
    if full: rect(x0, y0, x0+15, y0+15, role); text(ax, x0+7.5, y0+7.5, '9', role, 'm')
    rect(x0+15, y0, x0+25, y0+15, role); text(ax, x0+20, y0+7.5, '6', role, 'm')
    rect(x0, y0+15, x0+15, y0+25, role); text(ax, x0+7.5, y0+20, '6', role, 'm')
    rect(x0+15, y0+15, x0+25, y0+25, role); text(ax, x0+20, y0+20, '4', role, 'm')
sq(8, 'resultat', True)
sq(54, 'fixe', False)
box(ax, 54, 22, 15, 15, 'limite', fill=False, dash=True, r=0.1)
text(ax, 61.5, 29.5, 'manque 9', 'limite', 's')
text(ax, 20.5, 55, r'$k$ = 0, 1, 2', 'resultat', 'm')
text(ax, 66.5, 55, r'$k$ = 1, 2 seulement', 'limite', 'm')
text(ax, 44, 35, r'(2 + 3)$^2$', 'encre', 'm')
text(ax, 20.5, 13, '9 + 12 + 4 = 25', 'resultat', 'm')
text(ax, 66.5, 13, '12 + 4 = 16', 'limite', 'm')
save(fig, '01-177')
