import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ys = [48, 36, 24, 12]
G = [24, 12, 4, 1]          # tailles des groupes S4, A4, V, {e}
F = [1, 2, 6, 24]           # 24 / taille du groupe
names = [r'$S_4\ \leftrightarrow\ F_1$', r'$A_4\ \leftrightarrow\ F_2$', r'$V\ \leftrightarrow\ F_3$', r'$\{e\}\ \leftrightarrow\ K$']
text(ax, 18, 61, "groupes : nombre d'éléments", 'autre', 's')
text(ax, 68, 61, 'corps de la tour', 'sujet', 's')
for y, g, f, nm in zip(ys, G, F, names):
    wg = max(g * 0.95, 2.0); wf = max(f * 0.95, 2.0)
    box(ax, 34 - wg, y - 3, wg, 6, 'autre')
    text(ax, 34 - wg - 1.2, y, str(g), 'autre', 's', ha='right')
    box(ax, 54, y - 3, wf, 6, 'sujet')
    text(ax, 44, y, nm, 'encre', 's')
for k, lab in enumerate([r'$24\div12=2$', r'$12\div4=3$', r'$4\div1=4$']):
    text(ax, 44, (ys[k] + ys[k + 1]) / 2, lab, 'varie', 's')
save(fig, '64-096')
