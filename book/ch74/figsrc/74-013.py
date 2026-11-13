import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def star(cx, cy, R, r, role):
    pts = []
    for i in range(10):
        a = math.radians(90 + i * 36); rr = R if i % 2 == 0 else r
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    poly(ax, pts, role)
fig, ax = canvas(78)
box(ax, 4, 46, 34, 26, 'resultat'); star(21, 59, 10, 4.2, 'resultat')
text(ax, 21, 42, 'étoile seule', 'resultat', 's')
box(ax, 50, 46, 34, 26, 'limite')
for a in range(3):
    for b in range(2): star(58 + a * 9, 52.5 + b * 12, 4, 1.7, 'limite')
text(ax, 67, 42, 'étoile répétée', 'limite', 's')
text(ax, 44, 35, 'tours possibles', 'resultat', 's')
for i, s in enumerate(['1/2', '1/3', '1/4', '1/6']): box(ax, 4 + i * 15, 18, 13, 11, 'resultat', label=s)
box(ax, 70, 18, 14, 11, 'limite', label='1/5', weight='bold')
text(ax, 77, 12, 'refusé', 'limite', 's')
text(ax, 32, 12, 'demi, tiers, quart, sixième', 'resultat', 's')
save(fig, '74-013')
