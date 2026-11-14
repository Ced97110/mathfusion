import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
u = 7.0; s = 4 * u
poly(ax, [(4, 40), (4 + s, 40), (4 + s, 40 + s), (4, 40 + s)], 'sujet')
poly(ax, [(4, 40), (4 + s, 40), (4 + s, 40 + s), (4, 40 + s)], 'varie', fill=False)
text(ax, 4 + s / 2, 40 + s / 2 + 3, r'$a = 4$', 'sujet', 'm')
text(ax, 4 + s / 2, 40 + s / 2 - 3, r'$b = 4$', 'varie', 'm')
text(ax, 4 + s / 2, 36, 'b recouvre a', 'varie', 's')
text(ax, 62, 62, r'$(4+4)(4-4)$', 'sujet', 's')
text(ax, 62, 56, r'$= 8 \times 0 = 0$', 'resultat', 's')
text(ax, 62, 48, r'$16 - 16 = 0$', 'resultat', 's')
x0, x1 = 4, 4 + 8 * u
line(ax, [(x0, 20), (x1, 20)], 'resultat', lw=1.6)
brace(ax, x0, x1, 23, 'sujet', 'largeur $a+b = 8$', down=False)
text(ax, 44, 13, r'hauteur $a-b = 0$ : pas d’aire', 'resultat', 's')
save(fig, '15-133')
