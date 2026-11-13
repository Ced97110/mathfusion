import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Fig. 39.2 : z (2, 30°), w (√2, 45°), zw (2√2, 75°)
fig, ax = canvas(68)
ox, oy, u = 8, 6, 18
def pol(r, a):
    return (ox + r * u * math.cos(math.radians(a)), oy + r * u * math.sin(math.radians(a)))
def arc(r, a0, a1, role):
    pts = [(ox + r * math.cos(math.radians(a0 + (a1 - a0) * k / 40)), oy + r * math.sin(math.radians(a0 + (a1 - a0) * k / 40))) for k in range(41)]
    line(ax, pts, role, lw=1.0)
arrow(ax, (ox - 3, oy), (ox + 54, oy), 'fixe', lw=0.8)
Z, W2, ZW = pol(2, 30), pol(math.sqrt(2), 45), pol(2 * math.sqrt(2), 75)
arrow(ax, (ox, oy), Z, 'sujet', lw=1.6)
arrow(ax, (ox, oy), W2, 'autre', lw=1.6)
arrow(ax, (ox, oy), ZW, 'resultat', lw=1.8)
arc(30, 0, 30, 'sujet')
arc(16, 0, 45, 'autre')
arc(44, 0, 75, 'resultat')
text(ax, ox + 34 * math.cos(math.radians(5)), oy + 34 * math.sin(math.radians(5)) + 0.5, '30°', 'sujet', 's')
text(ax, ox + 21.5 * math.cos(math.radians(24)), oy + 21.5 * math.sin(math.radians(24)), '45°', 'autre', 's')
text(ax, ox + 49 * math.cos(math.radians(37)), oy + 49 * math.sin(math.radians(37)), '75°', 'resultat', 's')
text(ax, Z[0] + 2.5, Z[1] + 0.5, 'z', 'sujet', 'm', ha='left', weight='bold')
text(ax, W2[0] - 1.5, W2[1] + 3.5, 'w', 'autre', 'm', weight='bold')
text(ax, ZW[0] + 3, ZW[1] + 1.5, 'zw', 'resultat', 'm', ha='left', weight='bold')
text(ax, 56, 45, '|z| = 2', 'sujet', 'm', ha='left')
text(ax, 56, 38, '|w| = √2', 'autre', 'm', ha='left')
text(ax, 56, 31, '|zw| = 2√2\n≈ 2,83', 'resultat', 'm', ha='left')
text(ax, 56, 20, '30° + 45° = 75°', 'resultat', 'm', ha='left')
text(ax, ox - 3, oy - 3, 'O', 'fixe', 's')
save(fig, '39-069')
