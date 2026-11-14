import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 6, 40, 18, 10, 'sujet', label='5', size='l')
box(ax, 64, 40, 18, 10, 'resultat', label='25', size='l')
arrow(ax, (25, 47), (63, 47), 'varie'); arrow(ax, (63, 43), (25, 43), 'resultat')
text(ax, 44, 49.8, 'au carré', 'varie', 's'); text(ax, 44, 40.2, 'racine carrée', 'resultat', 's')
text(ax, 44, 56, r'$5^2 = 25$ et $\sqrt{25} = 5$', 'encre', 'm')
f = numberline(ax, 8, 76, 20, 0, 5, arrow_right=False)
for v, lab, role in [(1, r'$1^2 = 1$', 'sujet'), (2, r'$\sqrt{2}$ ?', 'limite'), (4, r'$2^2 = 4$', 'sujet')]:
    disc(ax, f(v), 20, 1.7, role)
    text(ax, f(v), 25.5, lab, role, 's')
text(ax, 44, 7, r'2 n’est le carré d’aucun entier', 'limite', 's')
save(fig, '80-482')
