import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Échelle : 1 mm = 5 km/h. Avion 180 -> 36 mm ; vent 100 -> 20 mm.
fig, ax = canvas(80)
K = 5.0
a, w = 180 / K, 100 / K            # 36 et 20 mm
x0 = 6
# Ligne 1 : vent vers l'est -> 280
y = 70
arrow(ax, (x0, y), (x0 + a, y), 'sujet')
arrow(ax, (x0 + a, y), (x0 + a + w, y), 'varie')
arrow(ax, (x0, y - 3), (x0 + (180 + 100) / K, y - 3), 'resultat')
text(ax, x0 + a / 2, y + 3.2, 'avion 180', 'sujet', 's')
text(ax, x0 + a + w / 2, y + 3.2, 'vent 100', 'varie', 's')
text(ax, 44, y - 8, 'vent vers l’est : 280 km/h', 'resultat', 's')
# Ligne 2 : vent vers l'ouest -> 80
y = 54
arrow(ax, (x0, y), (x0 + a, y), 'sujet')
arrow(ax, (x0 + a, y + 3), (x0 + a - w, y + 3), 'varie')
arrow(ax, (x0, y - 3), (x0 + (180 - 100) / K, y - 3), 'resultat')
text(ax, 44, y - 8, 'vent vers l’ouest : 80 km/h', 'resultat', 's')
# Ligne 3 : vent vers le nord -> sqrt(180^2+100^2) = 205,9 ~ 206
y = 22
arrow(ax, (x0, y), (x0 + a, y), 'sujet')
arrow(ax, (x0 + a, y), (x0 + a, y + w), 'varie')
arrow(ax, (x0, y), (x0 + a, y + w), 'resultat')
text(ax, x0 + a / 2, y - 3.5, 'avion 180', 'sujet', 's')
text(ax, x0 + a + 2, y + w / 2, 'vent 100', 'varie', 's', ha='left')
text(ax, 44, 10, 'vent vers le nord : 206 km/h', 'resultat', 's')
save(fig, '41-001')
