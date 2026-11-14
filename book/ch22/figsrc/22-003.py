import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 8, 44, 72, 16, 'fixe', label='le nombre qui, multiplié\npar lui-même, donne 16', size='m')
arrow(ax, (44, 43), (44, 31), 'varie')
text(ax, 62, 37, 'remplacé par', 'varie', 's')
box(ax, 8, 14, 72, 16, 'sujet', label='extraire la racine carrée\n' + r'$\sqrt{16}$', size='m')
arrow(ax, (44, 13), (44, 8.5), 'resultat')
text(ax, 44, 4.5, '4 : racine carrée de 16', 'resultat', 'm')
save(fig, '22-003')
