import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = (4, 33, 62)
text(ax, 44, 60, 'pour tout couple (x ; y)', 'encre', 'm')
gen = ('(x ; y)', '(y ; 0)', '(0 ; 0)')
con = ('(5 ; −2)', '(−2 ; 0)', '(0 ; 0)')
for row, (y, labs) in enumerate(((42, gen), (14, con))):
    for i, t in enumerate(labs):
        box(ax, xs[i], y, 22, 9, 'resultat' if i == 2 else 'sujet', label=t, size='s')
    for i in range(2):
        arrow(ax, (xs[i] + 23, y + 4.5), (xs[i + 1] - 1, y + 4.5), 'varie', lw=1.2)
        text(ax, xs[i] + 28.5, y + 12, r'$S-1$', 'varie', 's')
text(ax, 44, 32, 'avec x = 5 et y = −2 :', 'fixe', 's')
text(ax, 44, 5, r'$(S-1)^2$ envoie tout sur $(0\,;\,0)$', 'resultat', 's')
save(fig, '57-201')
