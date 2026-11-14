import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 36, 59, r'$P\,(3,\,2)$', 'sujet', 'm')
text(ax, 71, 59, r'$(4,\,1)$', 'autre', 'm')
data = [(40, 'lundi', r'$3+2=5$', 'resultat', r'$4+1=5$', 'resultat'),
        (26, 'mardi', r'$2\times3+2=8$', 'resultat', r'$2\times4+1=9\neq8$', 'limite'),
        (12, 'somme', r'$3\times3+2\times2=13$', 'resultat', r'$3\times4+2\times1=14\neq13$', 'limite')]
for y, nom, a, ra, b, rb in data:
    text(ax, 9, y + 5.5, nom, 'fixe', 's')
    box(ax, 19, y, 33, 11, ra, fill=True, label=a, size='s')
    box(ax, 54, y, 33, 11, rb, fill=True, label=b, size='s')
text(ax, 36, 6, 'la somme est vraie', 'resultat', 's')
text(ax, 71, 6, 'la somme est fausse', 'limite', 's')
save(fig, '24-053')
