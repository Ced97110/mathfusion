import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(80)
box(ax, 24, 64, 40, 11, 'fixe', label=r'$x^7 + 1$', size='l')
cols = [(3, '1 + x', 'parité', 'détecte 1 erreur'),
        (30.5, '1 + x + x³', 'Hamming', 'en corrige 1'),
        (58, '1 + x + … + x⁶', 'répétition', 'en corrige beaucoup')]
for x0, poly, name, what in cols:
    box(ax, x0, 34, 27, 13, 'sujet', label=poly, size='s')
    arrow(ax, (44, 63), (x0 + 13.5, 48.5), 'fixe')
    text(ax, x0 + 13.5, 28, name, 'sujet', 'm', weight='bold')
    text(ax, x0 + 13.5, 21, what, 'resultat', 's')
text(ax, 44, 8, 'un polynôme, trois diviseurs', 'encre', 's')
save(fig, '68-196')
