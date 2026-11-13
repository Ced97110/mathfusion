import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
from matplotlib.patches import Circle

fig, ax = canvas(64)

XS_DIVISEUR = [16, 20.5, 25, 29.5]   # centres des 4 carrés du diviseur d = 4
X_FIN = 31.75                        # bout de la rangée du diviseur

def point(x, y, r, role):
    ax.add_patch(Circle((x, y), r, fc=COL[role], ec='none', zorder=3))

def diviseur(cy):
    text(ax, 7, cy, r'$d = 4$', 'fixe', 'm')
    for cx in XS_DIVISEUR:
        box(ax, cx - 1.5, cy - 1.5, 3, 3, 'fixe', r=0.3)

def reste(n, cy):
    for i in range(n):
        point(16 + 4.5 * i, cy, 1.3, 'varie')

# Test
text(ax, 44, 59, r'$r < d$ ?', 'sujet', 'l')

# Premier reste : r = 7, au-dessus du diviseur
diviseur(42)
reste(7, 48)
text(ax, 7, 48, r'$r = 7$', 'varie', 'm')
line(ax, [(X_FIN, 16), (X_FIN, 52)], 'fixe', dash=True)
text(ax, 50, 48, r'$7 < 4$ : faux', 'limite', 'm', ha='left')
text(ax, 50, 42, 'on enlève 4', 'varie', 's', ha='left')

# On enlève un paquet de 4
arrow(ax, (22, 37.5), (22, 30.5), 'varie')
text(ax, 24.5, 34, '− 4', 'varie', 'm', ha='left')

# Second reste : r = 3, au-dessous du diviseur
diviseur(20)
reste(3, 26)
text(ax, 7, 26, r'$r = 3$', 'varie', 'm')
text(ax, 50, 26, r'$3 < 4$ : vrai', 'resultat', 'm', ha='left')
text(ax, 50, 20, 'on s’arrête', 'resultat', 's', ha='left')

save(fig, '03-060')
