import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'exposants $k$ de $\omega^k$, avec $n=8$', 'encre', 's')
bw, gap = 10, 1.0
x0 = (W - (7 * bw + 6 * gap)) / 2
pos = {k: x0 + (k - 1) * (bw + gap) for k in range(1, 8)}
for k in range(1, 8):
    role = 'resultat' if k % 2 else 'fixe'
    box(ax, pos[k], 26, bw, 9, role, label=str(k), size='l')
good = [1, 3, 5, 7]; bad = [2, 4, 6]
for k in good:
    arrow(ax, (pos[k] + bw / 2, 25), (pos[k] + bw / 2, 20), 'resultat', lw=0.8)
for k in bad:
    arrow(ax, (pos[k] + bw / 2, 25), (pos[k] + bw / 2, 20), 'fixe', lw=0.8)
box(ax, 2, 8, 50, 11, 'resultat', label='seul diviseur\ncommun avec 8 : 1', size='s')
box(ax, 54, 8, 32, 11, 'fixe', label='un diviseur commun\nautre que 1', size='s')
text(ax, 27, 3, r'$\omega,\omega^3,\omega^5,\omega^7$ primitives', 'resultat', 's')
text(ax, 70, 3, 'pas primitives', 'fixe', 's')
save(fig, '39-128')
