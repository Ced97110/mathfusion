import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
c = (26, 34); R = 20
for k in range(6):
    t = math.radians(60 * k)
    e = (c[0] + R * math.cos(t), c[1] + R * math.sin(t))
    line(ax, [c, e], 'sujet', lw=1.4)
    for s in (-1, 1):
        m = (c[0] + 12 * math.cos(t), c[1] + 12 * math.sin(t)); t2 = t + s * math.radians(40)
        line(ax, [m, (m[0] + 5 * math.cos(t2), m[1] + 5 * math.sin(t2))], 'sujet', lw=1.0)
for k in range(3):
    t = math.radians(30 + 60 * k); d = 24
    line(ax, [(c[0] - d * math.cos(t), c[1] - d * math.sin(t)), (c[0] + d * math.cos(t), c[1] + d * math.sin(t))], 'varie', dash=True)
text(ax, c[0], 5, 'flocon à 6 branches', 'sujet', 's')
text(ax, 70, 58, r'$D_n$', 'sujet', 'xl')
box(ax, 54, 38, 32, 11, 'sujet', label='6 rotations', size='s')
box(ax, 54, 24, 32, 11, 'varie', label='6 réflexions', size='s')
box(ax, 54, 8, 32, 12, 'resultat', label=r'$2n=12$', size='l')
save(fig, '74-100')
