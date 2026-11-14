import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'$\mathbb{F}_2^n$ : l’ensemble des mots de $n$ bits, $2^n$ mots', 'sujet', 'm')
p = 5.3
def row(y, n, roles):
    for k in range(n):
        poly(ax, [(2 + k * p, y), (2 + k * p + 4.5, y), (2 + k * p + 4.5, y + 4.5), (2 + k * p, y + 4.5)], roles(k))
text(ax, 2, 38, r'$n=3$ : $2\times2\times2=8$ mots', 'encre', 'm', ha='left')
row(31, 8, lambda k: 'sujet')
text(ax, 2, 20, r'$n=4$ : $2\times2\times2\times2=16$ mots', 'encre', 'm', ha='left')
row(13, 16, lambda k: 'sujet' if k < 8 else 'varie')
text(ax, 44, 6, 'un bit de plus : deux fois plus de mots', 'varie', 's')
save(fig, '68-025')
