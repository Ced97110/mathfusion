import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 12, 42, 64, 14, 'sujet', label=r'$\sin(x+\pi/2)=\cos x$', size='l')
box(ax, 2, 16, 40, 18, 'fixe', label='Preuve par la figure\n(rotation du triangle)', size='s')
box(ax, 46, 16, 40, 18, 'autre', label="Preuve par le calcul\n(formules d'addition)", size='s')
arrow(ax, (22, 34), (30, 42), 'fixe')
arrow(ax, (66, 34), (58, 42), 'autre')
text(ax, 44, 8, r'$x=1$ : les deux donnent 0,5403', 'resultat', 's')
save(fig, '30-176')
