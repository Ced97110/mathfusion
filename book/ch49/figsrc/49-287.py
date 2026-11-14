import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Circle
fig, ax = canvas(92)
h = 7
corners = [(-h, h), (-h, -h), (h, -h), (h, h)]
def sq(cx, cy, k):
    poly(ax, [(cx-h,cy-h),(cx+h,cy-h),(cx+h,cy+h),(cx-h,cy+h)], 'fixe')
    disc(ax, cx+corners[k][0], cy+corners[k][1], 1.2, 'fixe')   # grey mark : shows the square turned
    ax.add_patch(Circle((cx, cy), 3.8, ec=COL['resultat'], fc='none', lw=0.9, ls='--', zorder=2))
    disc(ax, cx, cy, 2.2, 'sujet')                               # the pawn : never moves
text(ax, 18, 87, 'avant', 'fixe', 'm')
text(ax, 70, 87, 'après', 'fixe', 'm')
for k, lab in enumerate(['1', r'$r$', r'$r^2$', r'$r^3$']):
    y = 72 - k*17
    sq(18, y, 0); sq(70, y, k)
    arrow(ax, (30, y), (58, y), 'varie')
    text(ax, 44, y+3.5, lab, 'varie', 'm')
text(ax, 44, 10, 'chaque rotation : pion fixe', 'sujet', 'm')
text(ax, 44, 3.5, 'orbite = le pion seul', 'resultat', 'm')
save(fig, '49-287')
