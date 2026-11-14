import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$f=xy-1$,  $q=x^2-y^2$,  $h=x^4-1$', 'encre', 's')
cols = [(2, 'resultat', r'$P=(1,\ 1)$', r'sur $f=0$ et $q=0$', r'$h(1)=0$', 'racine de $h$'),
        (46, 'limite', r'$(2,\ 0{,}5)$', r'sur $f=0$, pas sur $q=0$', r'$h(2)=15$', 'pas racine de $h$')]
for x, role, p, cap, hv, concl in cols:
    c = x + 20
    box(ax, x, 48, 40, 10, role, label=p)
    text(ax, c, 43, cap, role, 's')
    arrow(ax, (c, 39), (c, 31.5), 'varie')
    box(ax, x, 21, 40, 10, role, label=hv)
    text(ax, c, 15, concl, role, 's')
save(fig, '70-088')
