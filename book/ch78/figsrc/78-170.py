import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, 'centre de 2 éléments : q = 2', 'fixe', 's')
f = numberline(ax, 6, 72, 30, 0, 4, labels=False)
for v in range(1, 5):
    disc(ax, f(v), 40, 3.6, 'resultat' if v == 1 else 'limite', label=str(v))
text(ax, f(3), 49, r'$\Phi_6(2)=3$', 'limite', 's')
line(ax, [(f(1), 22), (f(1), 36)], 'sujet', lw=1.2, dash=True)
text(ax, f(1), 19, r'$q-1=1$', 'sujet', 's')
line(ax, [(f(1) + 2, 30), (f(4) + 4, 30)], 'limite', lw=2.4)
text(ax, f(3), 22, 'plus grands que 1', 'limite', 's')
text(ax, 44, 8, r'contradiction sauf $n=1$', 'resultat', 'm')
save(fig, '78-170')
