import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# gauche : plan par l'origine ; droite : plan décalé
def plan(x0, role, dash):
    pts = [(x0, 20), (x0 + 28, 20), (x0 + 36, 40), (x0 + 8, 40)]
    poly(ax, pts, role)
    if dash: line(ax, pts + [pts[0]], role, lw=1.0, dash=True)
    return pts
plan(5, 'resultat', False)
plan(48, 'limite', True)
disc(ax, 5 + 18, 30, 1.2, 'encre')
text(ax, 5 + 18 + 4, 27.5, r'$O$', 'encre', 'm')
disc(ax, 48 + 18, 14, 1.2, 'encre')
text(ax, 48 + 18 + 4, 11.5, r'$O$', 'encre', 'm')
text(ax, 23, 58, 'passe par O', 'resultat', 'm')
text(ax, 66, 58, 'ne passe pas par O', 'limite', 'm')
text(ax, 23, 50, 'sous-espace', 'resultat', 'm', weight='bold')
text(ax, 66, 50, 'pas un sous-espace', 'limite', 'm', weight='bold')
text(ax, 23, 8, r'$-3x+y+z=0$', 'resultat', 'm')
text(ax, 66, 5, r'$-3x+y+z=1$', 'limite', 'm')
save(fig, '58-133')
