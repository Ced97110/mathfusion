import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# field with 4 elements : alpha^1 = alpha, alpha^2 = alpha + 1, alpha^3 = alpha (alpha + 1) = 1
P = [r'$\alpha^1$', r'$\alpha^2$', r'$\alpha^3$']
V = [r'$\alpha$', r'$\alpha+1$', '1']
for k in range(3):
    x = 4 + k * 29
    box(ax, x, 38, 22, 11, 'sujet', label=P[k])
    arrow(ax, (x + 11, 37), (x + 11, 30), 'fixe')
    box(ax, x, 18, 22, 11, 'resultat', label=V[k])
    if k < 2:
        arrow(ax, (x + 23, 23.5), (x + 28, 23.5), 'varie', lw=1.3)
        text(ax, x + 25.5, 28.5, r'$\times\alpha$', 'varie', 's')
brace(ax, 4, 82, 16, 'resultat', label=r'$q - 1 = 3$ éléments non nuls', size='s')
text(ax, 44, 57, 'corps à 4 éléments', 'sujet', 'm')
save(fig, '67-080')
