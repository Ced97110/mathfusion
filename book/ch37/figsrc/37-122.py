import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
k = 0.15
text(ax, 44, 64, 'côtés fixes : 110 et 120', 'fixe', 'm')
cases = [(30, '3 300'), (53, '5 271'), (90, '6 600'), (150, '3 300')]
for i, (ang, aire) in enumerate(cases):
    ox = (i % 2) * 44 + 16; oy = 40 - (i // 2) * 32
    t = math.radians(ang); tip = (ox + 110 * k * math.cos(t), oy + 110 * k * math.sin(t))
    role = 'resultat' if ang == 90 else 'sujet'
    poly(ax, [(ox, oy), (ox + 120 * k, oy), tip], role)
    line(ax, [tip, (tip[0], oy)], 'varie', dash=True)
    ax.add_patch(matplotlib.patches.Arc((ox, oy), 7, 7, theta1=0, theta2=ang, ec=COL['fixe'], lw=0.7, zorder=3))
    rr = 9 if ang > 100 else 7.5; bis = math.radians(ang / 2)
    text(ax, ox + rr * math.cos(bis), oy + rr * math.sin(bis), f'{ang}°', 'fixe', 's')
    text(ax, ox + 9, oy - 4, f'Δ = {aire}', role, 'm')
save(fig, '37-122')
