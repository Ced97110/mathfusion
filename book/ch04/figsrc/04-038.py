import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(60)

def cross(ax, cx, cy, h=0.57):
    """Croix × de deux traits gris de 1,6 mm centrés en (cx, cy)."""
    line(ax, [(cx - h, cy - h), (cx + h, cy + h)], 'fixe', lw=0.9)
    line(ax, [(cx - h, cy + h), (cx + h, cy - h)], 'fixe', lw=0.9)

text(ax, 22, 52, 'deux facteurs égaux', 'varie', 's')
text(ax, 66, 52, 'trois facteurs égaux', 'varie', 's')

# signe sans petit nombre : deux facteurs, creux vide
line(ax, [(8, 36), (10, 37.5), (13, 28), (16, 44), (32, 44)], 'sujet', lw=1.5)
text(ax, 24, 37, '64', 'encre', 'l')
text(ax, 38, 37, '= 8', 'resultat', 'l')
ax.add_patch(Circle((10.6, 41), 2.4, ec=COL['fixe'], fc='none', lw=0.8, ls='--', zorder=2))

# signe avec le petit 3 : trois facteurs
line(ax, [(52, 36), (54, 37.5), (57, 28), (60, 44), (76, 44)], 'sujet', lw=1.5)
text(ax, 68, 37, '64', 'encre', 'l')
text(ax, 82, 37, '= 4', 'resultat', 'l')
text(ax, 54.6, 41, '3', 'varie', 's', weight='bold')
disc(ax, 54.6, 41, 2.4, 'varie', fill=False)

# deux facteurs égaux : 8 × 8 = 64
for x in (6, 16):
    box(ax, x, 12, 7, 8, 'varie', fill=False, label='8', size='m')
cross(ax, 14.5, 16)
text(ax, 30, 16, '= 64', 'encre', 'm')

# trois facteurs égaux : 4 × 4 × 4 = 64
for x in (46, 56, 66):
    box(ax, x, 12, 7, 8, 'varie', fill=False, label='4', size='m')
cross(ax, 54.5, 16)
cross(ax, 64.5, 16)
text(ax, 80, 16, '= 64', 'encre', 'm')

save(fig, '04-038')
