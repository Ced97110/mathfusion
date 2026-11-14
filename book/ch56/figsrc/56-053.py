import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# Deux lettres, même rôle
box(ax, 2, 56, 38, 16, 'sujet', label=r'$N(r)$' + '\n' + r'pour $a+b\sqrt{-5}$', size='s')
box(ax, 48, 56, 38, 16, 'autre', label=r'$\nu(z)$' + '\n' + r'pour $a+b\sqrt{3}\,i$', size='s')
text(ax, 44, 64, '=', 'encre', 'l')
text(ax, 44, 50, 'même rôle : carré de la distance à 0', 'encre', 's')
# La règle écrite avec ν
box(ax, 2, 22, 28, 12, 'resultat', label='ν(zw)', size='m')
text(ax, 34, 28, '=', 'encre', 'm')
box(ax, 38, 22, 20, 12, 'autre', label='ν(z)', size='m')
box(ax, 62, 22, 20, 12, 'autre', label='ν(w)', size='m')
text(ax, 16, 15, 'norme du produit', 'resultat', 's')
text(ax, 48, 15, 'norme de z', 'autre', 's')
text(ax, 72, 15, 'norme de w', 'autre', 's')
save(fig, '56-053')
