import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
X = lambda i: 12 + i*11
for i in range(6): box(ax, X(i), 50, 9, 9, 'sujet' if i % 2 == 0 else 'varie', label='a' if i % 2 == 0 else 'b')
for j in range(6): box(ax, X(j), 20, 9, 9, 'sujet' if j < 3 else 'varie', label='a' if j < 3 else 'b')
for i in range(6):
    j = i // 2 if i % 2 == 0 else 3 + i // 2
    arrow(ax, (X(i) + 4.5, 49.5), (X(j) + 4.5, 29.5), 'sujet' if i % 2 == 0 else 'varie')
brace(ax, X(0), X(2) + 9, 19, 'sujet'); brace(ax, X(3), X(5) + 9, 19, 'varie')
text(ax, 44, 64, 'commutativité', 'fixe', 'm', weight='bold')
text(ax, 44, 7, r'$a^3\, b^3$', 'resultat', 'xl')
save(fig, '14-045')
