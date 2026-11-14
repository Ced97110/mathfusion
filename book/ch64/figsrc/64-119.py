import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 22, 46, r'$N$ normal : $N=A_5$', 'resultat', 's')
text(ax, 66, 46, r'$N$ non normal', 'limite', 's')
for r in range(6):
    for c in range(10):
        disc(ax, 22 + (c - 4.5) * 3.4, 38 - r * 3.4, 1.0, 'resultat')
        disc(ax, 66 + (c - 4.5) * 3.4, 38 - r * 3.4, 1.0, 'limite' if r * 10 + c < 3 else 'fixe')
text(ax, 22, 14, '60 sur 60', 'resultat', 's')
text(ax, 66, 14, r'3 sur 60 : $\langle(1\,2\,3)\rangle$', 'limite', 's')
save(fig, '64-119')
