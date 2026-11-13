import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(60)
text(ax, 44, 54, 'le signe ° décide', 'encre', 'm')
box(ax, 6, 32, 20, 10, 'sujet', label='30°')
arrow(ax, (26, 37), (36, 37), 'encre')
box(ax, 36, 32, 28, 10, 'sujet', label='en degrés')
box(ax, 6, 12, 20, 10, 'varie', label='30')
arrow(ax, (26, 17), (36, 17), 'encre')
box(ax, 36, 12, 28, 10, 'varie', label='en radians')
text(ax, 75, 17, 'règle du livre', 'varie', 's')
save(fig, '29-042')
