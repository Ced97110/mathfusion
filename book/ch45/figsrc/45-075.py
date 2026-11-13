import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
X = [4 + i * 21 for i in range(4)]; bw = 15
for i in range(4):
    box(ax, X[i], 50, bw, 9, 'sujet', label=str(i)); box(ax, X[i], 12, bw, 9, 'resultat', label=str(i))
for i in range(4):
    j = (i + 1) % 4
    arrow(ax, (X[i] + bw / 2, 49.5), (X[j] + bw / 2, 21.5), 'varie' if i == 3 else 'sujet', lw=1.4 if i == 3 else 0.9)
text(ax, 44, 65, r'$x$ : départ', 'sujet', 'm'); text(ax, 44, 5, r'$a_L(x)$ : arrivée, ligne de 1', 'resultat', 'm')
save(fig, '45-075')
