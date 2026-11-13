import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# r = 2a cos θ, a = 1 : à 120°, r = -1 : on recule de 1 et on arrive sur la demi-droite de 300°. Le cercle est tracé deux fois sur un tour.
fig, ax = canvas(96)
u = 22; o = (14, 62)
def pt(r, deg): return (o[0] + u * r * math.cos(math.radians(deg)), o[1] + u * r * math.sin(math.radians(deg)))
def circ(a0, a1, role, lw):
    line(ax, [pt(2 * math.cos(math.radians(t)), t) for t in range(a0, a1 + 1, 2)], role, lw=lw)
circ(0, 90, 'sujet', 1.8)        # r > 0 : demi-cercle du haut
circ(90, 180, 'varie', 1.8)      # r < 0 : demi-cercle du bas
cc = (o[0] + u, o[1]); rr = 1.16 * u
ring = [(cc[0] + rr * math.cos(math.radians(p)), cc[1] + rr * math.sin(math.radians(p))) for p in range(-170, 171, 4)]
line(ax, ring[:-2], 'fixe', lw=0.8, dash=True)
arrow(ax, ring[-3], ring[-1], 'fixe', lw=0.8)
arrow(ax, (o[0] - 5, o[1]),(o[0] + 2 * u + 6, o[1]), 'fixe', lw=0.8)
line(ax, [o, pt(1.1, 120)], 'fixe', lw=0.7, dash=True)
Q = pt(-1, 120)
arrow(ax, (o[0] + 0.3, o[1] - 0.5), (Q[0] - 0.3, Q[1] + 0.5), 'varie', lw=1.5)
disc(ax, Q[0], Q[1], 1.5, 'varie'); disc(ax, o[0], o[1], 1.0, 'encre')
text(ax, pt(1.1, 120)[0] + 8, pt(1.1, 120)[1] + 1, '120°', 'fixe', 's')
text(ax, Q[0] + 15, Q[1] + 8,'$r = -1$ : 300°', 'varie', 's')
text(ax, 44, 92, r'$r = 2a\cos\theta$, $a = 1$', 'sujet', 'm')
text(ax, 44, 26, '0° à 90° : $r > 0$, demi-cercle du haut', 'sujet', 's')
text(ax, 44, 20, '90° à 180° : $r < 0$, demi-cercle du bas', 'varie', 's')
text(ax, 44, 12, '180° à 360° : le même cercle encore', 'fixe', 's')
text(ax, 44, 6, 'deux passages sur un tour', 'encre', 's')
save(fig, '40-051')
