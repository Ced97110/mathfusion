import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 21, 54, 'avant : ouvertes', 'fixe', 'm')
text(ax, 67, 54, 'après : fermées', 'resultat', 'm')
L = ['polygones réguliers', 'quadrature du cercle', 'troisième question']
R = ['Gauss-Wantzel', 'Lindemann', 'non nommée ici']
for i in range(3):
    y = 36 - i * 16
    d = (i == 2)
    box(ax, 2, y, 38, 11, 'fixe', label=L[i], dash=d, size='s')
    arrow(ax, (40, y + 5.5), (48, y + 5.5), 'resultat')
    box(ax, 48, y, 38, 11, 'resultat', label=R[i], dash=d, size='s')
save(fig, '66-139')
