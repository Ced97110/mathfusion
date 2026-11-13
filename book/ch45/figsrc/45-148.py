import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
bw, g, gg, x0 = 8, 1, 4, 4
xs = []
for k in range(3):
    gx = x0 + k * (2 * bw + g + gg)
    xs.append(gx)
    for j in range(2): box(ax, gx + j * (bw + g), 28, bw, 10, 'sujet', label=r'$a$', size='m')
    brace(ax, gx, gx + 2 * bw + g, 40, 'varie', label=r'$na$', down=False)
end = xs[2] + 2 * bw + g
brace(ax, xs[0], end, 26, 'resultat', label=r'$(mn)a=6a$', size='m')
arrow(ax, (end + 3, 33), (68, 33), 'encre')
box(ax, 70, 27, 14, 12, 'resultat', label='2', size='l')
text(ax, 77, 21, '6, reste 2', 'resultat', 's')
text(ax, 44, 6, r'$m=3$ paquets de $n=2$ fois $a$', 'encre', 's')
save(fig, '45-148')
