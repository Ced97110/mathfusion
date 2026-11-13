import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
rows = [(r'$x^2-3x-1=0$','sujet'), (r'$x^2-3x=1$','fixe'), (r'$(x-\frac{3}{2})^2=\frac{13}{4}$','fixe'), (r'$x=\frac{3\pm\sqrt{13}}{2}$','resultat')]
labs = ['on met 1 à droite', 'on ajoute 9/4 des deux côtés', 'on prend la racine']
ys = [80, 56, 32, 8]
for (t, r), y in zip(rows, ys): box(ax, 8, y, 72, 14, r, label=t, size='l')
for i, l in enumerate(labs):
    arrow(ax, (44, ys[i]-0.5), (44, ys[i+1]+14.5), 'varie')
    text(ax, 48, (ys[i]+ys[i+1]+14)/2, l, 'varie', 's', ha='left')
save(fig, '23-049')
