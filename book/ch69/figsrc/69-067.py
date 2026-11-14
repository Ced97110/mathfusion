import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
Y0 = 30
f = numberline(ax, 14, 74, Y0, 1, 2, step=1, arrow_right=False)
n = 60
pts = [(f(1 + i / n), Y0 + 14 * ((1 + i / n) ** 2 - 2)) for i in range(n + 1)]
line(ax, pts, 'sujet', lw=1.2)
disc(ax, f(1), Y0 - 14, 1.5, 'varie')
disc(ax, f(2), Y0 + 28, 1.5, 'varie')
text(ax, 24, 10, r'$f(1)=-1$', 'encre', 'm')
text(ax, 64, 63, r'$f(2)=2$', 'encre', 'm')
r = 2 ** 0.5
disc(ax, f(r), Y0, 1.5, 'resultat')
text(ax, 28, 40, 'racine ≈ 1,414', 'resultat', 'm')
text(ax, 30, 53, r'$f=x^2-2$', 'sujet', 'm')
text(ax, 44, 70, r'$f(1)\,f(2)=-2<0$', 'resultat', 'l')
save(fig, '69-067')
