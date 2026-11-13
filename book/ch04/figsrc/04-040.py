import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(76)

def cross(ax, cx, cy, h=0.57):
    """Croix × de deux traits gris de 1,6 mm centrés en (cx, cy)."""
    line(ax, [(cx - h, cy - h), (cx + h, cy + h)], 'fixe', lw=0.9)
    line(ax, [(cx - h, cy + h), (cx + h, cy - h)], 'fixe', lw=0.9)

# ligne du haut : l'exposant 3 de 2³
text(ax, 12, 66, '2', 'encre', 'l')
text(ax, 15.5, 69.5, '3', 'autre', 's')
text(ax, 14, 58.5, 'exposant', 'autre', 's')
arrow(ax, (25, 66), (35.5, 66), 'fixe', lw=0.9)
for x in (36, 46, 56):
    box(ax, x, 62.5, 7, 7, 'autre', fill=False, label='2', size='m')
cross(ax, 44.5, 66)
cross(ax, 54.5, 66)
text(ax, 70, 66, '= 8', 'encre', 'm')

# ligne du milieu : l'indice 3 de ∛8, boîtes vides
line(ax, [(6, 42), (8, 43.5), (11, 35), (14, 50), (26, 50)], 'encre', lw=1.4)
text(ax, 20, 43, '8', 'encre', 'l')
text(ax, 8.6, 47, '3', 'sujet', 's', weight='bold')
text(ax, 10, 30, 'indice', 'sujet', 's')
arrow(ax, (28, 42), (35.5, 42), 'fixe', lw=0.9)
for x in (36, 46, 56):
    box(ax, x, 38.5, 7, 7, 'sujet', fill=False, dash=True)
cross(ax, 44.5, 42)
cross(ax, 54.5, 42)
text(ax, 70, 42, '= 8', 'encre', 'm')

# ligne du bas : pour √16, l'indice 2 n'est pas écrit
line(ax, [(6, 18), (8, 19.5), (11, 11), (14, 26), (26, 26)], 'encre', lw=1.4)
text(ax, 20, 19, '16', 'encre', 'l')
ax.add_patch(Circle((8.6, 23), 2.2, ec=COL['sujet'], fc='none', lw=0.8, ls='--', zorder=2))
text(ax, 16, 6, 'indice 2, non écrit', 'sujet', 's')
arrow(ax, (28, 18), (35.5, 18), 'fixe', lw=0.9)
for x in (36, 46):
    box(ax, x, 14.5, 7, 7, 'sujet', fill=False, dash=True)
cross(ax, 44.5, 18)
text(ax, 60, 18, '= 16', 'encre', 'm')

save(fig, '04-040')
