import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def at(c, a, r): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def sector(c, r, a0, a1, role):
    poly(ax, [c] + [at(c, a0 + (a1 - a0)*i/30, r) for i in range(31)], role)
def ray(c, a, r=24, dash=False): line(ax, [c, at(c, a, r)], 'fixe', dash=dash)
box(ax, 20, 46, 48, 9, 'sujet', label="formules d'addition")
cs = [(3, 12), (31, 12), (59, 12)]
for c in cs: arrow(ax, (44, 46), (c[0] + 12, 41), 'sujet', lw=0.8)
sector(cs[0], 24, 0, 30, 'sujet'); sector(cs[0], 24, 30, 60, 'varie'); [ray(cs[0], a) for a in (0, 30, 60)]
sector(cs[1], 24, 0, 60, 'resultat'); [ray(cs[1], a) for a in (0, 60)]; ray(cs[1], 30, dash=True)
sector(cs[2], 24, 0, 30, 'sujet'); sector(cs[2], 24, 30, 60, 'varie'); sector(cs[2], 24, 60, 90, 'sujet'); [ray(cs[2], a) for a in (0, 30, 60, 90)]
for c, t in zip(cs, ('double', 'demi', 'triple')): text(ax, c[0] + 12, 38, t, 'encre', 's')
text(ax, 15, 5, '30° + 30° = 60°', 'sujet', 's')
text(ax, 43, 5, '60° ÷ 2 = 30°', 'resultat', 's')
text(ax, 71, 5, '3 × 30° = 90°', 'sujet', 's')
save(fig, '34-011')
