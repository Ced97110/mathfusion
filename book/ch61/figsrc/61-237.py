import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, 'tout non nul a un inverse', 'resultat', 'm')
for x, lab, role in [(14, '0', 'fixe'), (34, '1', 'resultat'), (54, r'$u$', 'sujet'), (74, r'$1+u$', 'sujet')]:
    disc(ax, x, 22, 6, role, label=lab)
arrow(ax, (54, 29), (74, 29), 'resultat', both=True, curve=-0.6)
text(ax, 64, 42, 'produit = 1', 'resultat', 's')
text(ax, 14, 10, '0 : exclu', 'fixe', 's'); text(ax, 34, 10, r'$1\times 1=1$', 'resultat', 's')
text(ax, 64, 10, r'$u\times(1+u)=1$', 'resultat', 's')
save(fig, '61-237')
