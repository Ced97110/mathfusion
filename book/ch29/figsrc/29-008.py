import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(64)
cy, r = 34, 14
for cx, ro, nom, tour, droit in ((22, 'sujet', 'degré', '360', '90'), (66, 'autre', 'grade', '400', '100')):
    disc(ax, cx, cy, r, ro, fill=False)
    poly(ax, [(cx, cy)] + arcpts(cx, cy, r, 0, 90), ro)
    line(ax, [(cx + 3, cy), (cx + 3, cy + 3), (cx, cy + 3)], ro, lw=0.7)
    text(ax, cx, cy + r + 6, nom, ro, 'l', weight='bold')
    text(ax, cx, cy - r - 5, f'tour : {tour} parts', ro, 's')
    text(ax, cx, cy - r - 11, f'angle droit : {droit}', ro, 's')
save(fig, '29-008')
