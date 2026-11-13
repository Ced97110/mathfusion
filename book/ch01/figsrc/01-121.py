import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 86, r'$1+2+\cdots+n=n(n+1)/2$', 'sujet', 'l')
f = numberline(ax, 10, 80, 16, 0, 10, step=1, every=5)
text(ax, 85, 12.5, r'$n$', 'fixe', 's')
for n in range(1, 11):
    S = n * (n + 1) // 2
    box(ax, f(n) - 2, 16, 4, S, 'sujet', r=0.3)
for n in range(1, 11):
    disc(ax, f(n), 16 + n * (n + 1) / 2, 1.1, 'resultat')
text(ax, 30, 29, r'$6=3\times4/2$', 'resultat', 's')
text(ax, 72, 75, r'$55=10\times11/2$', 'resultat', 's')
text(ax, 28, 62, r'$n=100$ : 5 050 = 5 050', 'resultat', 's')
text(ax, 26, 5, r'$3\times4=12$ : 4 est pair', 'encre', 's')
text(ax, 66, 5, r'$10\times11=110$ : 10 pair', 'encre', 's')
save(fig, '01-121')
