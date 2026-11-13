import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 16, 60, r'$n^{+}+m$', 'sujet', 'l', weight='bold')
text(ax, 46, 60, r'= $(n+m)^{+}$', 'sujet', 'l', weight='bold')
A = ['4 + 2', '11 + 2', '4 + 7']
B = ['= (3 + 2)⁺', '= (10 + 2)⁺', '= (3 + 7)⁺']
C = ['= 6', '= 13', '= 11']
for a, b, c, y in zip(A, B, C, (44, 34, 24)):
    text(ax, 16, y, a, 'sujet', 'm')
    text(ax, 46, y, b, 'varie', 'm')
    text(ax, 74, y, c, 'resultat', 'm', weight='bold')
arrow(ax, (24, 49), (36, 49), 'varie')
text(ax, 31, 52.5, 'un pas de moins', 'varie', 's')
arrow(ax, (58, 49), (69, 49), 'resultat')
text(ax, 64, 52.5, 'le suivant', 'resultat', 's')
line(ax, [(6, 17), (82, 17)], 'fixe', lw=0.6)
text(ax, 44, 12, '2 reste 2, 7 reste 7', 'fixe', 's')
save(fig, '01-044')
