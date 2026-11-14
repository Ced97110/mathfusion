import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# écriture 1 : 2 est un facteur de 6, donc 2 divise 6
yA = 63
text(ax, 6, yA + 6, '6 =', 'encre', 'm')
box(ax, 14, yA, 14, 12, 'sujet', label='2')
text(ax, 33, yA + 6, '×', 'encre', 'm')
box(ax, 38, yA, 14, 12, 'fixe', label='3')
text(ax, 72, yA + 6, '2 ∣ 6 : oui', 'resultat', 'm')
# écriture 2 : 2 ne divise aucun des deux facteurs
yB = 44
text(ax, 6, yB + 6, '6 =', 'encre', 'm')
box(ax, 12, yB, 32, 12, 'fixe', label=r'$1+\sqrt{-5}$')
text(ax, 48, yB + 6, '×', 'encre', 'm')
box(ax, 52, yB, 32, 12, 'fixe', label=r'$1-\sqrt{-5}$')
for x in (12, 52):
    arrow(ax, (x + 16, yB - 0.5), (x + 16, yB - 5), 'fixe')
box(ax, 12, yB - 17, 32, 11, 'limite', label='2 ∣ 1 + √−5 ? non', size='s')
box(ax, 52, yB - 17, 32, 11, 'limite', label='2 ∣ 1 − √−5 ? non', size='s')
text(ax, 44, yB - 24, 'car (1 + √−5) ÷ 2 = ½ + ½√−5\ncoefficients non entiers', 'limite', 's')
box(ax, 2, 3, 84, 12, 'resultat', label='2 divise 6 sans diviser un facteur\ndonc 2 n’est pas premier', size='s')
save(fig, '56-049')
