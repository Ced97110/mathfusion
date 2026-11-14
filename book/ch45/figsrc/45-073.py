import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
X = [4 + i * 21 for i in range(4)]; bw = 15
top = ['0', '1', '2', '3']; bot = ['nulle', 'quart', 'demi', '3 quarts']
for i in range(4):
    box(ax, X[i], 48, bw, 9, 'limite' if i == 3 else 'sujet', label=top[i]); box(ax, X[i], 16, bw, 9, 'resultat', label=bot[i], size='s')
    arrow(ax, (X[i] + bw / 2, 48), (X[i] + bw / 2, 25.5), 'fixe', lw=0.8)
brace(ax, 4, 4 + 3 * 21 + bw, 61, 'resultat', 'avoir 4 éléments : conservé', down=False)
brace(ax, 4, 4 + 3 * 21 + bw, 14, 'resultat', 'avoir 4 éléments', down=True)
text(ax, 15, 36.5, r'$\eta$', 'varie', 'l')
text(ax, 44, 80, 'contenir le nombre 3 : pas conservé', 'limite', 's')
save(fig, '45-073')
