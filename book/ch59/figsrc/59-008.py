import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
s, ox, oy = 6.5, 8, 10
P = lambda x, y: (ox + x * s, oy + y * s)
inK = lambda x, y: any(4 * a + 6 * b == x and 6 * a + 4 * b == y for a in range(-12, 13) for b in range(-12, 13))
# repr. : points entiers du parallélogramme demi-ouvert (0,0),(4,6),(6,4),(10,10)
reps = []
for i in range(0, 11):
    for j in range(0, 11):
        # x = a f1 + b f2 avec 0 <= a < 1, 0 <= b < 1 ; det = -20
        a = (4 * j - 6 * i) / -20.0 * -1  # placeholder remplacé ci-dessous
        a = (i * 4 - j * 6) / (4 * 4 - 6 * 6)
        b = (4 * j - 6 * i) / (4 * 4 - 6 * 6)
        if 0 <= a < 1 - 1e-12 and 0 <= b < 1 - 1e-12: reps.append((i, j))
assert len(reps) == 20, len(reps)
poly(ax, [P(0, 0), P(4, 6), P(10, 10), P(6, 4)], 'varie')
for i in range(11):
    for j in range(11):
        c = 'fixe'
        if (i, j) in reps: continue
        ax.plot([P(i, j)[0]], [P(i, j)[1]], '.', color=COL['fixe'], ms=2.4, zorder=3)
for (i, j) in reps:
    ax.plot([P(i, j)[0]], [P(i, j)[1]], 'o', color=COL['varie'], ms=3.0, zorder=4)
for (i, j) in [(0, 0), (4, 6), (6, 4), (10, 10)]:
    ax.plot([P(i, j)[0]], [P(i, j)[1]], 'o', color=COL['sujet'], ms=3.6, zorder=5)
text(ax, 4, 84, '20 paquets', 'varie', 'm', ha='left')
text(ax, 4, 78, 'un point orange par paquet', 'varie', 's', ha='left')
text(ax, 84, 4, r'points de $K$ en bleu', 'sujet', 's', ha='right')
save(fig, '59-008')
