import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def plane(ox, oy):
    arrow(ax, (ox - 17, oy), (ox + 17, oy), 'fixe', lw=0.6); arrow(ax, (ox, oy - 17), (ox, oy + 17), 'fixe', lw=0.6)
plane(22, 38); plane(66, 38)
text(ax, 22, 64, 'non dégénérée', 'resultat', 'm'); text(ax, 66, 64, 'dégénérée', 'limite', 'm')
disc(ax, 22, 38, 2.2, 'resultat')
text(ax, 22, 28, r'seul $z=0$', 'resultat', 's')
line(ax, [(66 - 11.2, 38 + 5.6), (66 + 11.2, 38 - 5.6)], 'limite', lw=1.8)
disc(ax, 66 + 11.2, 38 - 5.6, 1.3, 'limite')
text(ax, 66 + 4, 38 - 11.5, r'$z=(2,\,-1)$', 'limite', 's')
text(ax, 66 - 5, 38 + 11, 'toute la droite', 'limite', 's')
text(ax, 44, 9, r'$z$ orthogonal à tout : $B(x,z)=0$', 'encre', 's')
save(fig, '71-073')
