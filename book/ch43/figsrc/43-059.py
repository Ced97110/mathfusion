import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
import math
def panel(ox, oy, th, role):
    for a in (th, th + 90):
        r = math.radians(a)
        arrow(ax, (ox, oy), (ox + 17 * math.cos(r), oy + 17 * math.sin(r)), role, lw=0.9)
    r = math.radians(65)
    arrow(ax, (ox, oy), (ox + 20 * math.cos(r), oy + 20 * math.sin(r)), 'sujet', lw=1.6)
panel(20, 20, 0, 'fixe')
panel(66, 20, 20, 'autre')
text(ax, 20, 5, 'repère 1\nmatrice $A$', 'fixe', 'm')
text(ax, 66, 5, 'repère 2\nmatrice $B$', 'autre', 'm')
text(ax, 33, 42, 'flèche', 'sujet', 'm', ha='left')
text(ax, 44, 59, 'la même flèche, deux repères', 'encre', 'm')
save(fig, '43-059')
