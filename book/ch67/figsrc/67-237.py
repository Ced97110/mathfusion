import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
disc(ax, 44, 42, 28, 'sujet')
disc(ax, 34, 42, 15, 'resultat', label=r'vu modulo $p$', size='s')
text(ax, 44, 66, r'$G_f$', 'sujet', 'm')
disc(ax, 63, 42, 3, 'fixe')
text(ax, 63, 35, '4-cycle ?', 'fixe', 's')
text(ax, 44, 8, 'vu : présent ; non vu : inconnu', 'encre', 's')
save(fig, '67-237')
