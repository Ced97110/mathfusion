import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
E = [(0, 0), (1, 0), (0, 1), (1, 1)]
N = ['0', '1', r'$\alpha$', r'$\alpha+1$']
def mul(p, q):
    a, b = p; c, d = q
    return ((a * c + b * d) % 2, (a * d + b * c + b * d) % 2)
x0, ytop, c = 6, 66, 10  # header row 66..76, body rows below
text(ax, x0 + 5, ytop + 5, '×', 'encre', 'm')
for j in range(4):
    text(ax, x0 + c + c * j + 5, ytop + 5, N[j], 'varie' if j == 3 else 'sujet', 's')
for i in range(4):
    yb = ytop - c * (i + 1)
    text(ax, x0 + 5, yb + 5, N[i], 'varie' if i == 2 else 'sujet', 's')
    for j in range(4):
        v = N[E.index(mul(E[i], E[j]))]
        role = 'resultat' if (i == 2 and j == 3) else ('varie' if (i == 2 or j == 3) else 'fixe')
        box(ax, x0 + c + c * j, yb, c, c, role, label=v, size='s', r=0.4, lw=0.5)
text(ax, 59, 60, r'ligne $a=\alpha$', 'varie', 's', ha='left')
text(ax, 59, 52, r'colonne $b=\alpha+1$', 'varie', 's', ha='left')
text(ax, 59, 40, 'croisement :', 'resultat', 's', ha='left')
text(ax, 59, 33, r'$a\times b=1$', 'resultat', 'm', ha='left')
text(ax, 44, 8, 'on lit la case au croisement', 'encre', 's')
save(fig, '67-012')
