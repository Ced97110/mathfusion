import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
sq = [0, 1, 4]
sums = {a + b: (a, b) for a in sq for b in sq if a <= b}
assert [k for k in range(6) if k not in sums] == [3]
text(ax, 44, 55, r'sommes de deux carrés', 'encre', 'm', weight='bold')
text(ax, 44, 48, r'carrés possibles : $0$, $1$, $4$', 'fixe', 's')
for k in range(6):
    x = 2 + 14 * k
    ok = k in sums
    box(ax, x, 26, 13, 12, 'resultat' if ok else 'limite', label=str(k), size='l')
    if ok:
        a, b = sums[k]
        text(ax, x + 6.5, 20, rf'${a}+{b}$', 'resultat', 's')
text(ax, 44, 8, 'pour $3$ : aucune somme', 'limite', 'm', weight='bold')
arrow(ax, (2 + 14 * 3 + 6.5, 25), (2 + 14 * 3 + 6.5, 13), 'limite')
save(fig, '56-173')
