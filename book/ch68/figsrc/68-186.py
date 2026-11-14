import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(76)
text(ax, 44, 70, r'$R_7$ : on compte avec $x^7 = 1$', 'sujet', 'm')
text(ax, 2, 56, r'$x^7 \to 1$', 'varie', 'm', ha='left')
xs, p = brow(fig, ax, 58, 56, '1000000', role='resultat')
text(ax, 2, 42, r'$x^8 \to x$', 'varie', 'm', ha='left')
brow(fig, ax, 58, 42, '0100000', role='resultat')
brace(ax, xs[0] - p / 2, xs[-1] + p / 2, 37, 'resultat', 'degré < 7 : mot de 7 bits')
text(ax, 44, 17, 'tout polynôme se ramène à 7 bits', 'sujet', 's')
save(fig, '68-186')
