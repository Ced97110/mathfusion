import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(60)
cx, cy, R = 22, 34, 14
arc(ax, cx, cy, R, 0, 2 * math.pi, 'fixe', 0.8)
arc(ax, cx, cy, R, 0, 2.0, 'varie', 2.2)
rad(ax, cx, cy, R, 0, 'fixe'); rad(ax, cx, cy, R, 2.0, 'fixe')
text(ax, cx + R / 2, cy - 2.4, r'$r$', 'fixe', 'm')
p = pol(cx, cy, R + 4.5, 1.0)
text(ax, p[0], p[1], r'$s$', 'varie', 'm')
text(ax, cx, cy - R - 5, r'$s=6$ cm, $r=3$ cm', 'encre', 's')
text(ax, 64, 53, r'$\theta=s\,/\,r$', 'sujet', 'l')
box(ax, 44, 38, 20, 9, 'varie', label=r'$6\ \div\ 3$')
arrow(ax, (64, 42.5), (68, 42.5), 'encre')
box(ax, 68, 38, 16, 9, 'resultat', label=r'$\theta=2$')
box(ax, 44, 20, 20, 9, 'varie', label=r'$1{,}5\ \div\ 3$')
arrow(ax, (64, 24.5), (68, 24.5), 'encre')
box(ax, 68, 20, 16, 9, 'resultat', label=r'$\theta=0{,}5$')
text(ax, 64, 12, r'arc ÷ rayon', 'encre', 's')
save(fig, '29-033')
