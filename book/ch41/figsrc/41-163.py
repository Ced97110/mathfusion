import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
k = 1.6  # mm par unité de produit
x0 = 6
def bar(y, a, b, role, label):
    box(ax, x0 + a * k, y, (b - a) * k, 9, role, label=label, size='s')
# somme : 10 + 8 = 18
text(ax, 44, 82, 'somme dans une variable', 'encre', 's', weight='bold')
bar(66, 0, 10, 'sujet', '10')
bar(66, 10, 18, 'varie', '8')
bar(52, 0, 18, 'resultat', '18')
text(ax, x0 + 18 * k + 4, 70.5, r'$u\cdot v$, $w\cdot v$', 'fixe', 's', ha='left')
text(ax, x0 + 18 * k + 4, 56.5, r'$(u+w)\cdot v$', 'resultat', 's', ha='left')
# on double u et v ensemble : 10 devient 40
text(ax, 44, 38, r'on double $u$ et $v$', 'encre', 's', weight='bold')
bar(22, 0, 10, 'sujet', '10')
bar(8, 0, 40, 'autre', '40')
text(ax, x0 + 40 * k + 4, 12.5, r'$\times 2\times 2$', 'autre', 's', ha='left')
save(fig, '41-163')
