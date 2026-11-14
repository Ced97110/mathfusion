import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(108)
X = [4 + i * 21 for i in range(4)]; bw = 15
top = ['0', '1', '2', '3']; bot = ['nulle', 'quart', 'demi', '3 quarts']
# Panel A: bijective eta, the order is kept
text(ax, 44, 103, r'$\eta$ bijective', 'varie', 'm', weight='bold')
for i in range(4):
    box(ax, X[i], 72, bw, 9, 'sujet', label=top[i]); box(ax, X[i], 46, bw, 9, 'resultat', label=bot[i], size='s')
    arrow(ax, (X[i] + bw / 2, 72), (X[i] + bw / 2, 55.5), 'varie')
    if i < 3:
        arrow(ax, (X[i] + bw + 0.5, 76.5), (X[i + 1] - 0.5, 76.5), 'fixe', lw=0.8)
        arrow(ax, (X[i] + bw + 0.5, 50.5), (X[i + 1] - 0.5, 50.5), 'fixe', lw=0.8)
arrow(ax, (X[3] + bw / 2, 81.5), (X[0] + bw / 2, 81.5), 'fixe', lw=0.8, curve=0.18)
text(ax, 44, 92, r'$o(1)=4$ pas', 'sujet', 'm')
text(ax, 44, 40, r'$o(\eta(1))=4$ pas', 'resultat', 'm')
# Panel B: fiche counterexample, every number sent to the null rotation (not bijective)
line(ax, [(4, 34), (84, 34)], 'fixe', lw=0.6, dash=True)
text(ax, 44, 29, r'$\eta$ constante : tout vers nulle', 'limite', 'm', weight='bold')
for i in range(4):
    box(ax, X[i], 15, bw, 6, 'sujet')
    arrow(ax, (X[i] + bw / 2, 15), (44, 8.6), 'limite', lw=0.8)
box(ax, 34, 2, 20, 6, 'limite', label='nulle', size='s')
text(ax, 72, 5, r'$o(\eta(1))=1$ pas', 'limite', 's')
save(fig, '45-065')
