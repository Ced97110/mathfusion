import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(58)
cy, r = 30, 11
for cx, ro, tour, quart in ((14, 'autre', '100', '25'), (44, 'sujet', '360', '90'), (74, 'autre', '400', '100')):
    disc(ax, cx, cy, r, ro, fill=False)
    poly(ax, [(cx, cy)] + arcpts(cx, cy, r, 0, 90), ro)
    text(ax, cx, cy + r + 5, f'tour : {tour}', ro, 's')
    text(ax, cx, cy - r - 5, f'quart : {quart}', ro, 's')
text(ax, 44, 6, 'un choix parmi d’autres', 'varie', 's')
save(fig, '29-007')
