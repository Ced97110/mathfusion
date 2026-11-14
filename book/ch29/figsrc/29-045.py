import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(66)
cx, cy, R = 24, 44, 14
arc(ax, cx, cy, R, 0, 2 * math.pi, 'fixe', 0.8)
arc(ax, cx, cy, R, 0, 2.0, 'varie', 2.2)
rad(ax, cx, cy, R, 0, 'sujet'); rad(ax, cx, cy, R, 2.0, 'sujet')
text(ax, cx + R / 2, cy - 2.4, r'$r=1$', 'sujet', 's')
arrow(ax, (cx, cy - R - 1.5), (cx, 22), 'varie')
box(ax, 10, 10, 14, 8, 'sujet', label='1'); box(ax, 24, 10, 14, 8, 'sujet', label='1')
brace(ax, 10, 38, 10, 'varie', label='arc déroulé : 2')
text(ax, 66, 48, r'$\theta=2$', 'resultat', 'l')
text(ax, 66, 40, r'$\theta=s\,/\,1=s$', 'encre', 's')
text(ax, 66, 32, 'angle et arc :', 'encre', 's')
text(ax, 66, 27, 'même nombre', 'encre', 's')
save(fig, '29-045')
