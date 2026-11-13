import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
H = 11
X, Wd = 3, 40
ys = [68, 38, 8]
# départ -> étape qui porte le poids -> arrivée
box(ax, X, ys[0], Wd, H, 'sujet', label=r'$0\,v=(0+0)\,v$', size='m')
box(ax, X, ys[1], Wd, H, 'varie', label=r'$0\,v=0\,v+0\,v$', size='m', lw=1.4)
box(ax, X, ys[2], Wd, H, 'resultat', label=r'$\mathbf{0}=0\,v$', size='m', lw=1.2)
text(ax, X + Wd + 4, ys[0] + H / 2, 'départ', 'sujet', 's', ha='left', weight='bold')
text(ax, X + Wd + 4, ys[2] + H / 2, 'arrivée', 'resultat', 's', ha='left', weight='bold')
# étape 1 : règle 2
xa = X + Wd / 2
arrow(ax, (xa, ys[0]), (xa, ys[1] + H), 'varie', lw=2.2)
text(ax, xa + 4, 59, 'règle 2', 'varie', 'm', ha='left', weight='bold')
text(ax, xa + 4, 55, r'$(0+0)\,v=0\,v+0\,v$', 'varie', 's', ha='left')
text(ax, xa + 4, 51, 'étape qui porte le poids', 'varie', 's', ha='left')
# étape 2 : ajouter -0v des deux côtés
arrow(ax, (xa, ys[1]), (xa, ys[2] + H), 'fixe', lw=1.0)
text(ax, xa + 4, 29, r'ajouter $-0\,v$', 'fixe', 'm', ha='left')
text(ax, xa + 4, 25, 'des deux côtés', 'fixe', 's', ha='left')
save(fig, '58-113')
