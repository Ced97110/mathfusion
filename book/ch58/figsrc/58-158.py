import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 76, 'départ : un vecteur écrit avec les autres', 'fixe', 's')
box(ax, 14, 62, 60, 10, 'resultat', label=r'$w=-u+2v$', weight='bold')
# étape : passer w de l'autre côté
arrow(ax, (44, 61), (44, 53), 'varie', lw=1.5)
text(ax, 48, 57, r'on passe $w$ de l’autre côté', 'varie', 's', ha='left')
box(ax, 14, 41, 60, 11, 'varie')
text(ax, 44, 46.5, r'$-u+2v\ \mathbf{-1}\cdot w=(0,\,0)$', 'varie', 'm')
arrow(ax, (44, 40), (44, 32), 'resultat', lw=1.5)
# arrivée : un nombre devant w est non nul
text(ax, 44, 27, 'nombres devant u, v, w', 'fixe', 's')
vals = [r'$-1$', r'$2$', r'$-1$']
roles = ['sujet', 'varie', 'autre']
xs = [16, 38, 60]
for x, v, r in zip(xs, vals, roles):
    box(ax, x, 11, 14, 11, r, label=v)
text(ax, 67, 6, r'$-1\neq 0$ : famille liée', 'resultat', 's')
text(ax, 23, 6, 'pas de division', 'fixe', 's')
save(fig, '58-158')
