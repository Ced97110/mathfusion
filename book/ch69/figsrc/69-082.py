import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
Y0 = 26
n = 80
# panneau gauche : (x-1)^2 (x+2) sur [-2,2 ; 2]
xl = lambda v: 3 + (v + 2.2) * 40 / 4.2
gl = lambda x: (x - 1) ** 2 * (x + 2)
line(ax, [(3, Y0), (43, Y0)], 'fixe')
line(ax, [(xl(-2.2 + 4.2 * i / n), Y0 + 3.5 * gl(-2.2 + 4.2 * i / n)) for i in range(n + 1)], 'sujet', lw=1.2)
disc(ax, xl(-2), Y0, 1.1, 'resultat')
disc(ax, xl(1), Y0, 1.1, 'resultat')
# panneau droit : x^2 - 0,01 sur [-1,2 ; 1,2]
xr = lambda v: 46 + (v + 1.2) * 40 / 2.4
line(ax, [(46, Y0), (86, Y0)], 'fixe')
line(ax, [(xr(-1.2 + 2.4 * i / n), Y0 + 8 * ((-1.2 + 2.4 * i / n) ** 2 - 0.01)) for i in range(n + 1)], 'autre', lw=1.2)
disc(ax, xr(-0.1), Y0, 0.9, 'resultat')
disc(ax, xr(0.1), Y0, 0.9, 'resultat')
text(ax, 23, 48, r'$(x-1)^2(x+2)$', 'sujet', 'm')
text(ax, 66, 48, r'$x^2-0{,}01$', 'autre', 'm')
text(ax, 23, 11, 'racine double en 1 :\nun seul contact', 'sujet', 's')
text(ax, 66, 11, 'racines −0,1 et 0,1 :\nà peine séparées', 'autre', 's')
text(ax, 44, 56, 'une figure donne une idée, pas une preuve', 'encre', 'm')
save(fig, '69-082')
