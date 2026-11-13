import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))

fig, ax = canvas(84)
text(ax, 25, 78, 'dimension 4, Q = somme de 4 carrés', 'encre', 's', ha='left') if False else None
box(ax, 4, 14, 44, 58, 'sujet')
text(ax, 26, 65, r'$\Omega$', 'sujet', 'l')
box(ax, 9, 20, 34, 30, 'fixe')
text(ax, 26, 41, '{1, −1}', 'fixe', 'm')
text(ax, 26, 31, 'centre : −1 commute', 'fixe', 's')
text(ax, 26, 24, 'avec tout', 'fixe', 's')
arrow(ax, (50, 43), (60, 43), 'varie')
text(ax, 55, 49, 'diviser', 'varie', 's')
box(ax, 62, 28, 24, 30, 'resultat')
text(ax, 74, 50, r'$\Omega/(\Omega\cap\{1,-1\})$', 'resultat', 's') if False else None
text(ax, 74, 47, 'quotient', 'resultat', 's')
text(ax, 74, 38, 'simple', 'resultat', 'm', weight='bold')
text(ax, 26, 8, r'$\Omega$ seul : pas simple', 'limite', 's')
text(ax, 74, 20, r'$\Omega/(\Omega\cap\{1,-1\})$', 'resultat', 's')
save(fig, '73-200')
