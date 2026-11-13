import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
a = 0.35
s = 50                      # 1 m = 50 mm ; R = 17,5 mm
ox, oy = 6, 22
R = s * a
t = math.pi / 2
Cx = ox + s * a * t         # 0,55 m -> 33 mm
Cy = oy + R
Mx, My = Cx - R, Cy          # valve : a sin t = 0,35 à gauche, a cos t = 0 dessous
line(ax, [(2, oy), (60, oy)], 'fixe', lw=1.0)
line(ax, [(Cx + R * math.cos(u), Cy + R * math.sin(u)) for u in [2 * math.pi * i / 200 for i in range(201)]], 'fixe', lw=1.0)
line(ax, [(Cx, Cy), (Mx, My)], 'sujet', lw=1.2)
disc(ax, Cx, Cy, 0.9, 'fixe')
disc(ax, Cx, oy, 0.9, 'fixe')
disc(ax, Mx, My, 1.3, 'varie')
text(ax, Cx + 3.2, Cy + 2.4, 'C', 'fixe', 's')
text(ax, Mx - 3, My + 3, 'M', 'varie', 's')
text(ax, Cx, oy + 3.2, 't = π/2', 'encre', 's') if False else None
# abscisse : a t (orange) puis − a sin t (vert)
yb = oy - 6
arrow(ax, (ox, yb), (Cx, yb), 'varie', lw=1.2)
arrow(ax, (Cx, yb - 4), (Mx, yb - 4), 'resultat', lw=1.2)
line(ax, [(Cx, oy), (Cx, yb - 4)], 'fixe', lw=0.6, dash=True)
line(ax, [(Mx, My), (Mx, yb - 4)], 'resultat', lw=0.6, dash=True)
text(ax, ox + 4, yb + 3.2, 'at ≈ 0,55', 'varie', 's', ha='left')
text(ax, Cx + 3, yb - 4, '− a sin t = − 0,35', 'resultat', 's', ha='left')
text(ax, Mx, 1.5, 'x ≈ 0,20', 'resultat', 's')
# hauteur : a − a cos t
line(ax, [(Cx + R + 4, oy), (Cx + R + 4, My)], 'resultat', lw=1.2)
text(ax, 74, My - 3, 'y = 0,35 − 0', 'resultat', 's')
text(ax, 74, My - 8.5, '= 0,35', 'resultat', 's')
text(ax, 56, 58, 'x = a t − a sin t', 'sujet', 'm', ha='left')
text(ax, 56, 52, 'y = a − a cos t', 'sujet', 'm', ha='left')
text(ax, 74, 57, 't = π/2', 'varie', 'm') if False else None
text(ax, 62, 57, 'a = 0,35 ; t = π/2', 'encre', 's', ha='left') if False else None
save(fig, '40-099')
