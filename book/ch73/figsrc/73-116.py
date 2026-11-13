import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 8, 50, r'$Q(u_1)$', 'sujet', 's'); text(ax, 26, 50, r'$Q(u_2)$', 'sujet', 's'); text(ax, 45, 50, 'produit', 'encre', 's')
def row(y, a, b, c, rc):
    box(ax, 2, y, 12, 10, 'sujet', label=a); text(ax, 17, y + 5, r'$\times$', 'encre', 'm')
    box(ax, 20, y, 12, 10, 'sujet', label=b); arrow(ax, (33, y + 5), (38, y + 5), 'varie')
    box(ax, 39, y, 12, 10, rc, label=c)
row(33, '−1', '1', '−1', 'limite'); row(12, '4', '1', '4', 'resultat')
text(ax, 70, 38, 'autre classe', 'limite', 's')
text(ax, 70, 20, r'$4=1\times 2^2$', 'resultat', 's'); text(ax, 70, 14.5, '4 et 1 : même classe', 'resultat', 's')
save(fig, '73-116')
