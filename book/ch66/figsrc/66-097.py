import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, r'chaque case est un entier $n$, de 3 à 20', 'encre', 's')
f = numberline(ax, 6, 80, 15, 3, 20, 1, every=2, arrow_right=False)
green = {3, 4, 5, 6, 8, 10, 12, 15, 16, 17, 20}
for n in range(3, 21):
    r = 'resultat' if n in green else 'limite'
    poly(ax, [(f(n) - 2, 20.5), (f(n) + 2, 20.5), (f(n) + 2, 24.5), (f(n) - 2, 24.5)], r)
for n, t in [(7, r'$n=7$ : $\varphi(7)=6$'), (17, r'$n=17$ : $\varphi(17)=16$')]:
    text(ax, f(n) - (6 if n == 17 else 0), 36, t, 'encre', 's')
    arrow(ax, (f(n), 33.5), (f(n), 26), 'fixe', lw=0.8)
poly(ax, [(4, 4), (8, 4), (8, 8), (4, 8)], 'resultat')
text(ax, 10, 6, r'$n$ vert : $\varphi(n)$ puissance de 2', 'resultat', 's', ha='left')
poly(ax, [(4, 43), (8, 43), (8, 47), (4, 47)], 'limite')
text(ax, 10, 45, r'$n$ rouge : $\varphi(n)$ pas puissance de 2', 'limite', 's', ha='left')
save(fig, '66-097')
