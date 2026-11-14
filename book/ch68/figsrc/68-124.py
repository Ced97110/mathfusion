import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
EQ = {'A': (4, 5, 6, 7), 'B': (2, 3, 6, 7), 'C': (1, 3, 5, 7)}
count = {p: sum(p in v for v in EQ.values()) for p in range(1, 8)}
assert [p for p in count if count[p] == 1] == [1, 2, 4]
role = {p: ('resultat' if count[p] == 1 else 'sujet') for p in count}
X = {p: 22 + 9 * (p - 1) for p in range(1, 8)}
text(ax, 8, 66, 'position', 'fixe', 's')
for p in range(1, 8):
    box(ax, X[p] - 3.6, 62.5, 7.2, 7, role[p], label=str(p), r=0.5)
for k, (name, ps) in enumerate(EQ.items()):
    y = 52 - 10 * k
    text(ax, 8, y, f'ligne {name}', 'fixe', 's')
    line(ax, [(X[1] - 4, y), (X[7] + 4, y)], 'fixe', lw=0.4, dash=True)
    for p in ps:
        disc(ax, X[p], y, 2.4, role[p])
for p in range(1, 8):
    line(ax, [(X[p], 60.5), (X[p], 25.5)], role[p], lw=0.4, dash=True)
box(ax, 14, 12, 60, 8, 'resultat', label='contrôle : 1 seule équation')
box(ax, 14, 2, 60, 8, 'sujet', label='message : 2 ou 3 équations')
save(fig, '68-124')
