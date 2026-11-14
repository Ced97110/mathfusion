import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
R = 3.8
y = 40
x1, x2, x3, xr = 12, 30, 48, 78
text(ax, 44, 68, r'$\sigma$ : un cycle de longueur $r\geq 4$', 'sujet', 'm')
disc(ax, x1, y, R, 'resultat', label=r'$a_1$')
disc(ax, x2, y, R, 'fixe', label=r'$a_2$')
disc(ax, x3, y, R, 'resultat', label=r'$a_3$')
text(ax, 63, y, r'$\cdots$', 'fixe', 'l')
disc(ax, xr, y, R, 'resultat', label=r'$a_r$')
arrow(ax, (x1, y + R), (x3, y + R), 'resultat', curve=-0.4)
arrow(ax, (x3, y + R), (xr, y + R), 'resultat', curve=-0.35)
arrow(ax, (xr, y - R), (x1, y - R), 'resultat', curve=-0.25)
text(ax, 46, 58, r'résultat : $(a_1\,a_3\,a_r)$', 'resultat', 'm')
text(ax, 44, 21, r'avec $\rho=(a_1\,a_2\,a_3)$', 'varie', 'm')
text(ax, 44, 9, r'exemple : $(12345)$ donne $(135)$', 'encre', 's')
save(fig, '64-130')
