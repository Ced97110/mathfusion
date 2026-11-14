import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
H = 11
box(ax, 4, 58, 80, H, 'sujet', label=r'départ : $2\,v=(0,0)$', size='s')
arrow(ax, (44, 58), (44, 43), 'varie', lw=2.0)
text(ax, 47, 50.5, r'$\times\,\frac{1}{2}$ : inverse de 2', 'varie', 's', ha='left', weight='bold')
box(ax, 4, 32, 80, H, 'varie', label=r'$\frac{1}{2}\times2\,v=\frac{1}{2}\times(0,0)$', size='s', lw=1.4)
arrow(ax, (44, 32), (44, 17), 'fixe', lw=1.0)
text(ax, 47, 24.5, r'$\frac{1}{2}\times 2=1$', 'fixe', 's', ha='left')
box(ax, 4, 6, 80, H, 'resultat', label=r'arrivée : $v=(0,0)$', size='s', lw=1.2)
text(ax, 8, 50.5, 'étape décisive', 'varie', 's', ha='left')
save(fig, '58-114')
