import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

cx, cy, R = 21, 36, 15
a0, a1 = 90 - 57.3, 90 + 57.3
P = (cx + R * math.cos(math.radians(a1)), cy + R * math.sin(math.radians(a1)))
Q = (cx + R * math.cos(math.radians(a0)), cy + R * math.sin(math.radians(a0)))
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
poly(ax, arcp(cx, cy, R, a0, a1), 'sujet')
line(ax, [P, Q], 'resultat', lw=1.8)
line(ax, arcp(cx, cy, R, a0, a1), 'varie', lw=1.8)
line(ax, [(cx, cy), P], 'fixe')
line(ax, [(cx, cy), Q], 'fixe')
text(ax, P[0] - 3.5, P[1] + 1, r'$P$', 'encre', 'm')
text(ax, Q[0] + 3.5, Q[1] + 1, r'$Q$', 'encre', 'm')
text(ax, cx, cy - 4, r'$O$', 'encre', 'm')
text(ax, cx, 13, 'r = 3 cm, angle 2', 'encre', 's')
labs = ['1. arc\ns = rθ = 6 cm', '2. corde\n2r sin(θ/2) ≈ 5,05 cm', '3. périmètre\narc + corde ≈ 11,05 cm', '4. aire du segment\n½ r²(θ − sin θ)']
roles = ['varie', 'resultat', 'sujet', 'autre']
h, gap = 13, 4
for i in range(4):
    y = 69 - i * (h + gap) - h
    box(ax, 43, y, 44, h, roles[i], label=labs[i], size='s')
    if i < 3:
        arrow(ax, (65, y - 0.2), (65, y - gap + 0.2), 'encre')
save(fig, '29-089')
