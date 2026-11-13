import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
def at(c, a, r): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def sector(c, r, a0, a1, role):
    poly(ax, [c] + [at(c, a0 + (a1 - a0)*i/30, r) for i in range(31)], role)
def ray(c, a, r=24): line(ax, [c, at(c, a, r)], 'fixe')
box(ax, 29, 3, 30, 44, 'sujet', fill=False, dash=True, lw=0.7)
cs = [(3, 14), (31, 14), (59, 14)]
sector(cs[0], 24, 0, 40, 'fixe'); [ray(cs[0], a) for a in (0, 40)]
sector(cs[1], 24, 0, 30, 'sujet'); sector(cs[1], 24, 30, 75, 'varie'); [ray(cs[1], a) for a in (0, 30, 75)]
sector(cs[2], 24, 0, 35, 'sujet'); sector(cs[2], 24, 35, 70, 'varie'); [ray(cs[2], a) for a in (0, 35, 70)]
for c, t, role in zip(cs, ('un angle', 'deux angles', 'angle double'), ('fixe', 'sujet', 'fixe')):
    text(ax, c[0] + 12, 43, t, role, 's')
text(ax, 15, 7, r'$\sin^2 A+\cos^2 A=1$', 'fixe', 's')
text(ax, 43, 7, r'$\sin(A+B)$', 'sujet', 's')
text(ax, 71, 7, r'$\sin(A+A)$', 'fixe', 's')
save(fig, '34-010')
