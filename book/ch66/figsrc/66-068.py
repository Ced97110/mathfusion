import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'$F_k=2^{2^k}+1$, ici $k=3$', 'sujet', 'm')
labs = [(r'$k=3$', 'sujet'), (r'$2^3=8$', 'varie'), (r'$2^8=256$', 'varie'), (r'$F_3=257$', 'resultat')]
w, g = 17, 5.5
for i, (s, role) in enumerate(labs):
    x = 2 + i * (w + g)
    box(ax, x, 36, w, 10, role, label=s, size='s')
    if i < 3:
        arrow(ax, (x + w, 41), (x + w + g, 41), 'varie')
text(ax, 44, 29, r'$2^k$, puis $2^{2^k}$, puis $+1$', 'varie', 's')
for i, (k, v, e) in enumerate([(0, 3, 1), (1, 5, 2), (2, 17, 4)]):
    box(ax, 2 + i * 29, 6, 27, 10, 'fixe', label=rf'$F_{k}=2^{{{e}}}+1={v}$', size='s')
save(fig, '66-068')
