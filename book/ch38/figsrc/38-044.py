import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
x0, x1 = 8.0, 78.0
# Droite 1 : l'angle β − α, de 3,2° à 3,4°
y1 = 46.0
f1 = numberline(ax, x0, x1, y1, 3.2, 3.4, step=0.05, labels=False, arrow_right=False)
disc(ax, f1(3.25), y1, 1.4, 'fixe'); disc(ax, f1(3.35), y1, 1.4, 'varie')
text(ax, f1(3.25), y1 + 4.5, '3,25°', 'fixe', 's', weight='bold')
text(ax, f1(3.35), y1 + 4.5, '3,35°', 'varie', 's', weight='bold')
text(ax, x0, y1 + 11, 'angle β − α', 'sujet', 's', ha='left', weight='bold')
# Droite 2 : la hauteur h, de 1 900 m à 2 000 m
y2 = 16.0
f2 = numberline(ax, x0, x1, y2, 1900, 2000, step=25, labels=False, arrow_right=False)
disc(ax, f2(1976), y2, 1.4, 'fixe'); disc(ax, f2(1925), y2, 1.4, 'varie')
text(ax, f2(1976), y2 + 4.5, '1 976 m', 'fixe', 's', weight='bold')
text(ax, f2(1925), y2 + 4.5, '1 925 m', 'varie', 's', weight='bold')
text(ax, x0, y2 + 11, 'hauteur h', 'sujet', 's', ha='left', weight='bold')
brace(ax, f2(1925), f2(1976), y2 - 3, 'varie', label='51 m d’écart', size='s')
# Le lien entre les deux
arrow(ax, (44, 39), (44, 30), 'varie')
text(ax, 47, 34.5, '0,1° de plus sur β', 'varie', 's', ha='left', weight='bold')
save(fig, '38-044')
