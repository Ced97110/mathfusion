import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# cas 1 : clé 5, L(11) -> Q(16) ; cas 2 : clé 3, X(23) -> A(0)
cases = [(58, 'L : 11', 'Q : 16', '+5', '−5', '16 − 5 = 11', 'resultat'),
         (14, 'X : 23', 'A : 0', '+3', '−3', '0 − 3 = −3, puis −3 + 26 = 23', 'resultat')]
for y, a, b, fw, bk, cap, role in cases:
    box(ax, 2, y, 20, 10, 'fixe', label=a)
    box(ax, 66, y, 20, 10, 'varie', label=b)
    arrow(ax, (24, y + 7.5), (64, y + 7.5), 'fixe')
    text(ax, 44, y + 11, fw, 'fixe', 'm')
    arrow(ax, (64, y + 2.5), (24, y + 2.5), 'sujet')
    text(ax, 44, y - 1, bk, 'sujet', 'm', weight='bold')
    text(ax, 44, y - 7, cap, role, 's', weight='bold')
text(ax, 13, 72, 'clé 5', 'varie', 's')
text(ax, 13, 28, 'clé 3', 'varie', 's')
save(fig, '53-035')
