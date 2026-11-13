import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
text(ax, 44, 79, r'$m^{\varphi(n)}\equiv 1$ si PGCD$(m,n)=1$', 'encre', 'm')
# horloge à 6 cases : 1 et 5 sont inversibles
for i in range(6):
    disc(ax, 9 + 14 * i, 64, 5, 'sujet' if i in (1, 5) else 'fixe', label=str(i))
text(ax, 44, 54, r'$\varphi(6)=2$ : cases 1 et 5', 'sujet', 's')
# cas qui marche
text(ax, 22, 45, r'$m=5$, PGCD$(5,6)=1$', 'resultat', 's')
box(ax, 2, 27, 40, 12, 'resultat', label=r'$5^2=25=4\times6+1$')
text(ax, 22, 21, 'reste 1', 'resultat', 's')
# cas sans l'hypothèse
text(ax, 66, 45, r'$m=2$, PGCD$(2,6)=2$', 'limite', 's')
box(ax, 46, 27, 40, 12, 'limite', label=r'$2^2=4=0\times6+4$')
text(ax, 66, 21, 'reste 4, pas 1', 'limite', 's')
save(fig, '53-122')
