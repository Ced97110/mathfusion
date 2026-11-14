import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# i² = −1 : deux quarts de tour = un demi-tour
fig, ax = canvas(54)
ox, oy, u = 44, 12, 20
arrow(ax, (ox - 30, oy), (ox + 30, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 2), (ox, oy + 28), 'fixe', lw=0.8)
n = 40
def arc(a0, a1):
    return [(ox + u * math.cos(math.radians(a0 + (a1 - a0) * k / n)), oy + u * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]
for a0, a1 in ((0, 90), (90, 180)):
    p = arc(a0, a1)
    line(ax, p, 'varie', lw=1.6)
    arrow(ax, p[-3], p[-1], 'varie', lw=1.6)
disc(ax, ox + u, oy, 1.6, 'fixe')
disc(ax, ox, oy + u, 1.6, 'sujet')
disc(ax, ox - u, oy, 1.6, 'resultat')
text(ax, ox + u, oy - 3.5, '1', 'fixe', 'm')
text(ax, ox + 3, oy + u + 3, 'i', 'sujet', 'm', weight='bold', ha='left')
text(ax, ox - u, oy - 3.5, '−1', 'resultat', 'm', weight='bold')
text(ax, ox + 20, oy + 21, '× i : 90°', 'varie', 's', ha='left')
text(ax, ox - 20, oy + 21, '× i : 90°', 'varie', 's', ha='right')
text(ax, 44, 3.5, '90° + 90° = 180° : demi-tour', 'varie', 's')
text(ax, 44, 47, 'i × i = i² = −1', 'resultat', 'l', weight='bold')
save(fig, '39-072')
