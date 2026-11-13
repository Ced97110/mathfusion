import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
from matplotlib.patches import Rectangle

fig, ax = canvas(64)

def carres(cx, cy, n):
    """n carrés bleus pleins de 2 mm, pas de 2,4 mm, groupe centré sur cx ; cy = centre vertical."""
    x_premier = cx - (2.4 * n - 0.4) / 2
    for i in range(n):
        ax.add_patch(Rectangle((x_premier + 2.4 * i, cy - 1), 2, 2, fc=COL['sujet'], ec='none', zorder=3))

# Première division : 1 706 ÷ 4 (quotient 426, sans zéro)
text(ax, 4, 59, '1 706 ÷ 4', 'encre', 'm', ha='left')
for x0, nombre, n in ((4, '17', 4), (22, '10', 2), (40, '26', 6)):
    box(ax, x0, 40, 17, 14, 'fixe')
    cx = x0 + 8.5
    text(ax, cx, 50.5, nombre, 'encre', 'm')
    carres(cx, 44.5, n)
box(ax, 62, 40, 24, 14, 'resultat', label='quotient 426', size='s')

# Séparation des deux cas
line(ax, [(2, 35), (86, 35)], 'fixe', lw=0.9)

# Seconde division : 1 204 ÷ 4 (le 0 apparaît au quotient)
text(ax, 4, 30, '1 204 ÷ 4', 'encre', 'm', ha='left')
box(ax, 4, 12, 17, 14, 'fixe')
text(ax, 12.5, 22.5, '12', 'encre', 'm')
carres(12.5, 16.5, 3)
box(ax, 22, 12, 17, 14, 'limite')
text(ax, 30.5, 22.5, '0', 'limite', 'm')
box(ax, 29.5, 15.5, 2, 2, 'limite', fill=False, dash=True, r=0.2)
text(ax, 30.5, 6.5, '4 ne tient pas', 'limite', 's')
box(ax, 40, 12, 17, 14, 'fixe')
text(ax, 48.5, 22.5, '4', 'encre', 'm')
carres(48.5, 16.5, 1)
box(ax, 62, 12, 24, 14, 'resultat', label='quotient 301', size='s')

# Légende : ce que compte un carré bleu
ax.add_patch(Rectangle((44, 5.5), 2, 2, fc=COL['sujet'], ec='none', zorder=3))
text(ax, 47, 6.5, '= un 4 qui tient', 'encre', 's', ha='left')

save(fig, '03-085')
