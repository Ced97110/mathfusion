import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
Y0 = 36
xv = lambda v: 14 + (v + 4) * 10
yv = lambda v: Y0 + 3.5 * v
text(ax, 44, 78, 'irréductibles : degré 1 ou 2', 'resultat', 'm')
text(ax, 44, 72, r'$x^2+ax+b$ irréductible $\Leftrightarrow a^2<4b$', 'resultat', 'm')
numberline(ax, 14, 74, Y0, -4, 2, step=1)
n = 60
pts1 = [(xv(-3 + 4 * i / n), yv((-3 + 4 * i / n) ** 2 + 2 * (-3 + 4 * i / n) + 5)) for i in range(n + 1)]
pts2 = [(xv(-4 + 6 * i / n), yv((-4 + 6 * i / n) ** 2 + 2 * (-4 + 6 * i / n) - 3)) for i in range(n + 1)]
line(ax, pts1, 'sujet', lw=1.1)
line(ax, pts2, 'autre', lw=1.1)
disc(ax, xv(-1), yv(4), 1.3, 'sujet')
text(ax, xv(-1), yv(4) + 5, 'minimum 4', 'sujet', 's')
disc(ax, xv(-3), Y0, 1.3, 'resultat')
disc(ax, xv(1), Y0, 1.3, 'resultat')
text(ax, 44, 12, r'$x^2+2x+5$ : $a^2=4$, $4b=20$ : $4<20$', 'sujet', 's')
text(ax, 44, 6, r'$x^2+2x-3$ : $a^2=4$, $4b=-12$ : $4<-12$ faux', 'autre', 's')
save(fig, '69-066')
