import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$5\div 2$ : $q=5/2$ et $r=0$, il faut $\delta(0)<\delta(2)$', 'encre', 's')
# gauche : taille = degré
text(ax, 22, 56, 'taille = degré', 'autre', 'm', weight='bold')
f = numberline(ax, 10, 34, 38, 0, 2, step=1, arrow_right=False)
disc(ax, f(0), 38, 1.6, 'sujet')
text(ax, f(0) + 2, 43, r'$\delta(2)=0$', 'sujet', 's', ha='left')
arrow(ax, (f(0) - 1, 38), (f(0) - 6.5, 38), 'limite', lw=1.2)
text(ax, 22, 24, r'$\delta(0)<0$ : rien', 'limite', 's')
text(ax, 22, 19.5, 'dans les entiers naturels', 'limite', 's')
# droite : taille = 2^degré
text(ax, 66, 56, r'taille = $2^{\mathrm{deg}}$', 'resultat', 'm', weight='bold')
g = numberline(ax, 54, 78, 38, 0, 2, step=1, arrow_right=False)
disc(ax, g(0), 38, 1.6, 'resultat')
disc(ax, g(1), 38, 1.6, 'sujet')
text(ax, g(0) - 2, 43, r'$\delta(0)=0$', 'resultat', 's', ha='left')
text(ax, g(1) + 1, 33.5 - 6, r'$\delta(2)=2^0=1$', 'sujet', 's', ha='left') if False else None
text(ax, 66, 24, r'$\delta(2)=2^0=1$', 'sujet', 's')
text(ax, 66, 19.5, r'$0<1$ : possible', 'resultat', 's')
line(ax, [(44, 14), (44, 52)], 'fixe', dash=True)
save(fig, '56-136')
