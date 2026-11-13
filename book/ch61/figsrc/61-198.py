import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cx, cy, r = 22, 44, 17
pts = [(cx + r * math.cos(math.radians(90 + 360 * k / 17)), cy + r * math.sin(math.radians(90 + 360 * k / 17))) for k in range(17)]
poly(ax, pts, 'resultat')
for p in pts: disc(ax, p[0], p[1], 0.8, 'resultat')
text(ax, 22, 20, '17 côtés', 'resultat', 's')
box(ax, 48, 56, 38, 11, 'sujet', label='degré du polynôme : 16', size='s')
text(ax, 67, 51.5, 'quatre facteurs égaux à 2', 'fixe', 's')
for i in range(4):
    box(ax, 48 + 10 * i, 38, 6, 9, 'varie', label='2')
    if i < 3: text(ax, 56 + 10 * i, 42.5, '×', 'varie')
arrow(ax, (67, 38), (67, 31.5), 'fixe')
box(ax, 48, 20, 38, 11, 'resultat', label=r'$16=2^4$ : case verte', size='s')
arrow(ax, (67, 20), (67, 14.5), 'fixe')
box(ax, 48, 4, 38, 10, 'resultat', label="Gauss l'a construit", size='s', weight='bold')
save(fig, '61-198')
