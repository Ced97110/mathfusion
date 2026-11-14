import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
s, p = 5.5, 6.3
def grid(x0, y0, cols, rows, role):
    for i in range(cols):
        for j in range(rows):
            box(ax, x0 + i * p, y0 + j * p, s, s, role, r=0.3, lw=0.6)
# n = 9 : 3 x 2 = 6
text(ax, 22, 62, r'$n=9=3^2$', 'encre', 'm')
grid(6, 28, 3, 2, 'limite')
text(ax, 22, 22, r'$3\times 2=6$', 'limite', 'm')
text(ax, 22, 14, r'3 est impair, plus grand que 1', 'limite', 's')
text(ax, 22, 8, r'6 n’est pas $2^m$', 'limite', 's')
# n = 15 : 2 x 4 = 8
text(ax, 66, 62, r'$n=15=3\times 5$', 'encre', 'm')
grid(50, 28, 4, 2, 'resultat')
text(ax, 66, 22, r'$2\times 4=8$', 'resultat', 'm')
text(ax, 66, 14, r'2 et 4 sont des', 'resultat', 's')
text(ax, 66, 8, r'puissances de 2', 'resultat', 's')
text(ax, 22, 50, r'$p-1$ : 3 × 2 cases'.replace('$p-1$ : ', ''), 'fixe', 's')
text(ax, 66, 50, r'4 colonnes × 2 lignes', 'fixe', 's')
save(fig, '66-065')
