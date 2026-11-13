import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 22, 62, 44, 11, 'sujet', label='$f = x^2-9$')
for x, d, v, rest, role, concl in [(2, '÷ ($x-3$)', 'f(3) = 9 − 9', 'reste 0', 'resultat', '$x-3$ divise $f$'),
                                   (47, '÷ ($x-2$)', 'f(2) = 4 − 9', 'reste −5', 'limite', '$x-2$ ne divise pas $f$')]:
    arrow(ax, (44, 61.5), (x + 19, 52), 'varie')
    text(ax, x + 19, 48, d, 'varie', 'm')
    box(ax, x, 30, 38, 10, 'fixe', label=v.replace('f(3)', '$f(3)$').replace('f(2)', '$f(2)$'), size='s')
    arrow(ax, (x + 19, 44.5 - 5), (x + 19, 40.5), 'fixe') if False else None
    arrow(ax, (x + 19, 29.5), (x + 19, 22.5), 'varie')
    box(ax, x, 12, 38, 10, role, label=rest)
    text(ax, x + 19, 7, concl, role, 's')
save(fig, '62-026')
