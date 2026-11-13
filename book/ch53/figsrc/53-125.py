import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(72)
# horloge à 7 cases : toutes les cases de 1 à 6 sont inversibles
for i in range(7):
    disc(ax, 8 + 12 * i, 62, 5, 'fixe' if i == 0 else 'sujet', label=str(i))
brace(ax, 15, 85, 56, 'sujet', label=r'$\varphi(7)=p-1=6$')
# m = 2 : p ne divise pas m
text(ax, 22, 42, r'$m=2$ : 7 ne divise pas 2', 'resultat', 's')
box(ax, 2, 24, 40, 12, 'resultat', label=r'$2^6=64=9\times7+1$')
text(ax, 22, 18, 'reste 1', 'resultat', 's')
# m = 7 : p divise m
text(ax, 66, 42, r'$m=7$ : 7 divise 7', 'limite', 's')
box(ax, 46, 24, 40, 12, 'limite', label=r'$7^6$ : multiple de 7')
text(ax, 66, 18, 'reste 0, pas 1', 'limite', 's')
save(fig, '53-125')
