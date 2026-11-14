import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
xs = (3, 25, 47, 69)
for x, d, n in zip(xs, (2, 3, 4, 5), (2, 6, 24, 120)):
    ok = d < 5
    text(ax, x + 8.5, 78, f'degré {d}', 'fixe', 's')
    box(ax, x, 50, 17, 20, 'resultat' if ok else 'limite', label=f'$S_{d}$\n{n}', size='s')
brace(ax, xs[0], xs[2] + 17, 47, 'resultat', label='résolubles : formule', down=True)
box(ax, 69, 24, 17, 14, 'limite', label='$A_5$\n60', size='s')
arrow(ax, (77.5, 49), (77.5, 39), 'limite')
text(ax, 77.5, 17, 'simple :\npas de formule', 'limite', 's')
save(fig, '64-190')
