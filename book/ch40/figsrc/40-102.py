import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 26                      # a = 1 -> 26 mm
cx, cy = 31, 33
arrow(ax, (cx - 29, cy), (cx + 30, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - 29), (cx, cy + 30), 'fixe', lw=0.6)
T = [2 * math.pi * i / 400 for i in range(401)]
line(ax, [(cx + s * math.cos(t), cy + s * math.sin(t)) for t in T], 'autre', lw=1.2)
line(ax, [(cx + s * math.cos(t) ** 3, cy + s * math.sin(t) ** 3) for t in T], 'sujet', lw=1.5)
# 45 degrés
c45 = math.cos(math.pi / 4)
P1 = (cx + s * c45, cy + s * c45)           # cercle : 0,707 ; 0,707
P2 = (cx + s * c45 ** 3, cy + s * c45 ** 3)  # astroïde : 0,354 ; 0,354
line(ax, [(cx, cy), P1], 'fixe', lw=0.8, dash=True)
disc(ax, P1[0], P1[1], 1.2, 'autre')
disc(ax, P2[0], P2[1], 1.2, 'sujet')
for p in [(cx + s, cy), (cx, cy + s), (cx - s, cy), (cx, cy - s)]:
    disc(ax, p[0], p[1], 0.9, 'resultat')
arrow(ax, (P1[0] + 1.5, P1[1] + 0.5), (63, 52), 'autre', lw=0.6)
text(ax, 74, 56, 'cercle', 'autre', 'm')
text(ax, 74, 51, 'distance 1', 'autre', 's')
text(ax, 74, 45.5, '(0,707 ; 0,707)', 'autre', 's')
arrow(ax, (P2[0] + 1.5, P2[1] - 0.5), (62, 38.5), 'sujet', lw=0.6)
text(ax, 74, 37, 'astroïde', 'sujet', 'm')
text(ax, 74, 31.5, 'distance 0,5', 'sujet', 's')
text(ax, 74, 26, '(0,354 ; 0,354)', 'sujet', 's')
text(ax, 74, 8, 'ils se touchent', 'resultat', 's')
text(ax, 74, 3.5, 'en (a ; 0), (0 ; a)…', 'resultat', 's')
save(fig, '40-102')
