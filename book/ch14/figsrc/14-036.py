import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 4, 6, 38, 44, 'resultat'); box(ax, 46, 6, 38, 44, 'limite')
text(ax, 23, 43, r'$a = 2$', 'resultat', 'l'); text(ax, 65, 43, r'$a = 0$', 'limite', 'l')
text(ax, 23, 33, r'$2^5\ /\ 2^2$', 'encre'); text(ax, 65, 33, r'$0^5\ /\ 0^2$', 'encre')
text(ax, 23, 23, r'$32\ /\ 4$', 'encre'); text(ax, 65, 23, r'$0\ /\ 0$', 'encre')
text(ax, 23, 13, r'$= 8$', 'resultat', 'l', weight='bold'); text(ax, 65, 13, 'aucun sens', 'limite', 'l', weight='bold')
save(fig, '14-036')
