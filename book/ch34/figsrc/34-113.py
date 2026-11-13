import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
rows = [('écrire', r'$\sin(A+B)=\sin A\cos B+\cos A\sin B$', 'sujet'),
        ('remplacer', r'0,7071 $\times$ 0,866 + 0,7071 $\times$ 0,5', 'sujet'),
        ('multiplier', r'0,6124 + 0,3536', 'sujet'),
        ('réunir', r'= 0,9659 = $\sin 75°$', 'resultat')]
text(ax, 44, 89, r'$A=45°,\ B=30°$ : calculer $\sin 75°$', 'encre', 'm')
h, gap = 13, 7
y = 70 - h
ys = []
for i, (nom, expr, role) in enumerate(rows):
    yy = 76 - i * (h + gap) - h + 4
    ys.append(yy)
    box(ax, 3, yy, 24, h, 'varie', label=nom)
    box(ax, 31, yy, 54, h, role, label=expr, size='s')
for i in range(3):
    arrow(ax, (15, ys[i]), (15, ys[i + 1] + h), 'varie')
save(fig, '34-113')
