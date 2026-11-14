import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(94)
text(ax, 44, 88, r'coefficients $a_i$ dans $\mathbb{F}_p$', 'varie', 'm')
A = [r'$a_1$', r'$a_2$', '⋯', r'$a_n$']
U = [r'$u_1$', r'$u_2$', '⋯', r'$u_n$']
cx = []
for i in range(4):
    x = 4 + i * 21; cx.append(x + 8)
    box(ax, x, 68, 16, 12, 'fixe' if i == 2 else 'varie', label=A[i])
    text(ax, x + 8, 62, '×', 'encre', 'm')
    box(ax, x, 44, 16, 12, 'fixe' if i == 2 else 'sujet', label=U[i])
text(ax, 44, 38, r'base de $F$', 'sujet', 's')
for c in cx:
    arrow(ax, (c, 44), (44 + (c - 44) * 0.35, 27), 'resultat')
box(ax, 8, 14, 72, 13, 'resultat', label=r'$x=a_1u_1+\cdots+a_nu_n$', size='m')
text(ax, 44, 6, 'une seule écriture pour chaque $x$', 'resultat', 's')
save(fig, '67-026')
