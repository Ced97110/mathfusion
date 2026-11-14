import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
disc(ax, 44, 26, 9, 'sujet', label=r'$\alpha^{0}=1$')
arrow(ax, (37.6, 32.4), (50.4, 32.4), 'varie', curve=-1.0)
text(ax, 44, 43.5, 'carré : 0 × 2 = 0', 'varie', 'm')
text(ax, 44, 12, 'paquet d’un seul élément', 'sujet', 'm')
text(ax, 44, 5.5, r'racine de $x+1$', 'sujet', 'm')
save(fig, '67-188')
