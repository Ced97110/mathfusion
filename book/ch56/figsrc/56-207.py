import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 20, 61, r'$x^2+x+1$', 'sujet', 'l')
text(ax, 67, 61, r'$x^2+3x+3$', 'resultat', 'l')
for k, s in enumerate(['1', '1', '1']):
    box(ax, 3 + k * 12.5, 38, 11, 11, 'fixe', label=s, size='m')
for k, (s, role) in enumerate([('1', 'sujet'), ('3', 'resultat'), ('3', 'resultat')]):
    box(ax, 51 + k * 12.5, 38, 11, 11, role, label=s, size='m')
arrow(ax, (41, 52), (49, 52), 'varie')
text(ax, 45, 56, r'$x\to x+1$', 'varie', 's')
text(ax, 20, 31, r'constante $1$ : $3\nmid1$', 'fixe', 's')
text(ax, 67, 31, r'$3\mid3$ et $3\mid3$', 'resultat', 's')
text(ax, 67, 23, r'$3\nmid1$ et $9\nmid3$', 'resultat', 's')
box(ax, 8, 4, 72, 11, 'resultat', label=r'Eisenstein avec $p=3$', size='m')
save(fig, '56-207')
