import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
rows = [('1', r'diviseurs $d$ de $n$', '1, 2, 3, 6', 'sujet'),
        ('2', r'terme $q^d$', r'$q^1,q^2,q^3,q^6$', 'sujet'),
        ('3', r'signe $\mu(n/d)$', r'$+1$, $-1$ ou $0$', 'varie'),
        ('4', 'somme', 'on additionne', 'autre'),
        ('5', r'division par $n$', r'on divise par 6', 'resultat')]
for i, (k, a, b, r) in enumerate(rows):
    y = 86 - i * 15
    box(ax, 2, y - 6, 44, 11, r, label=a, size='s')
    box(ax, 50, y - 6, 36, 11, 'fixe', label=b, size='s')
    if i < 4: arrow(ax, (24, y - 7), (24, y - 9.4), 'fixe')
text(ax, 24, 97.5, 'étage de la formule', 'encre', 's'); text(ax, 68, 97.5, r'pour $n=6$', 'encre', 's')
text(ax, 44, 8, r'$N=\frac{1}{n}\sum\mu(n/d)\,q^d$', 'encre', 'm')
save(fig, '67-120')
