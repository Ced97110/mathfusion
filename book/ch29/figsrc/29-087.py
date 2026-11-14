import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

cx, cy, R = 8, 56, 50
h = math.degrees(0.3)
poly(ax, [(cx, cy)] + arcp(cx, cy, R, -h, h, 20), 'fixe')
line(ax, arcp(cx, cy, R, -h, h, 20), 'varie', lw=1.8)
for a in (-h, h):
    line(ax, [(cx, cy), (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))], 'sujet', lw=1.2)
text(ax, 33, 43, 'r = 500 m', 'sujet', 's')
text(ax, 62, 56, 's = 300 m', 'varie', 's', ha='left')
text(ax, 21, 56, r'$\theta$', 'resultat', 'm')
box(ax, 14, 20, 60, 10, 'resultat', label='θ = 300 ÷ 500 = 0,6 rad', size='m')
arrow(ax, (44, 19.5), (44, 12.5), 'varie')
text(ax, 48, 16, r'$\times\,180/\pi$', 'varie', 's', ha='left')
box(ax, 29, 2.5, 30, 9.5, 'resultat', label='≈ 34,38°', size='m')
save(fig, '29-087')
