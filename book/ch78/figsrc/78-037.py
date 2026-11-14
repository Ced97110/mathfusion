import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$[x,y,z]=(xy)z-x(yz)$', 'encre', 'l')
for cx, lab, role in [(18, r'$x=E$', 'sujet'), (44, r'$y=E$', 'sujet'), (70, r'$z=G$', 'autre')]:
    box(ax, cx - 9, 58, 18, 8, role, label=lab)
text(ax, 20, 49, 'groupement à gauche', 'fixe', 's')
text(ax, 68, 49, 'groupement à droite', 'fixe', 's')
box(ax, 3, 32, 36, 12, 'fixe', label=r'$(xy)z=0$')
box(ax, 49, 32, 36, 12, 'fixe', label=r'$x(yz)=-2E$')
text(ax, 44, 38, '−', 'varie', 'xl', weight='bold')
arrow(ax, (21, 31), (30, 20), 'resultat', lw=1.2)
arrow(ax, (67, 31), (58, 20), 'resultat', lw=1.2)
box(ax, 14, 5, 60, 14, 'resultat', label=r'$[E,E,G]=0-(-2E)=2E$', weight='bold')
save(fig, '78-037')
