import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(52)
f = numberline(ax, 6, 76, 18, -1, 1, step=0.5)
disc(ax, f(-0.988), 18, 1.6, 'varie'); disc(ax, f(0.5), 18, 1.6, 'sujet')
line(ax, [(f(-0.988), 21), (f(-0.988), 31)], 'varie', 0.8, dash=True)
line(ax, [(f(0.5), 21), (f(0.5), 31)], 'sujet', 0.8, dash=True)
text(ax, f(-0.988) - 1, 34, r'$\sin 30\approx-0{,}988$', 'varie', 's', ha='left')
text(ax, f(0.5), 34, r'$\sin 30^\circ=0{,}5$', 'sujet', 's')
text(ax, f(-0.988) - 1, 41, '30 radians', 'varie', 's', ha='left')
text(ax, f(0.5), 41, '30 degrés', 'sujet', 's')
text(ax, 44, 4, 'un petit ° change le résultat', 'encre', 's')
save(fig, '29-043')
