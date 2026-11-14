import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cx, cy, u = 46, 35, 11
a0 = math.atan2(0.8, 2)
r = math.hypot(2, 0.8) * u
def pt(k, rad=r):
    a = a0 + k * math.pi / 2; return (cx + rad * math.cos(a), cy + rad * math.sin(a))
line(ax, [(cx - 26, cy), (cx + 26, cy)], 'fixe', lw=0.4)
line(ax, [(cx, cy - 26), (cx, cy + 26)], 'fixe', lw=0.4)
line(ax, [(cx + r * math.cos(t * 2 * math.pi / 120), cy + r * math.sin(t * 2 * math.pi / 120)) for t in range(121)], 'fixe', dash=True, lw=0.6)
for k, role in enumerate(('sujet', 'varie', 'autre', 'fixe')):
    arrow(ax, (cx, cy), pt(k), role, lw=1.5)
for k in range(4):
    a_s = a0 + k * math.pi / 2 + 0.3; a_e = a0 + (k + 1) * math.pi / 2 - 0.3
    pts = [(cx + 8 * math.cos(a_s + (a_e - a_s) * j / 20), cy + 8 * math.sin(a_s + (a_e - a_s) * j / 20)) for j in range(21)]
    line(ax, pts[:-3], 'varie', lw=1.0)
    arrow(ax, pts[-4], pts[-1], 'varie', lw=1.0)
x, y = pt(0.5, 14)
text(ax, x, y, '90°', 'varie', 's')
text(ax, 70, 45, '$v$ (2 ; 0,8)', 'sujet', 's', ha='left')
text(ax, 37, 64, '$Tv$ (−0,8 ; 2)', 'varie', 's')
text(ax, 22, 24, '$T^2v$ = −$v$\n(−2 ; −0,8)', 'autre', 's', ha='right')
text(ax, 57, 9, '$T^3v$ (0,8 ; −2)', 'fixe', 's', ha='left')
save(fig, '57-101')
