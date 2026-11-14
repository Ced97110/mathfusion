import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 7.5; oy = 32.0
def grid(ox, union):
    P = lambda x, y: (ox + x * u, oy + y * u)
    for i in range(-2, 3):
        for j in range(-2, 3):
            if not union: role = 'resultat'
            elif j == 0: role = 'sujet'
            elif i == 0: role = 'autre'
            else: role = 'fixe'
            disc(ax, *P(i, j), 1.0 if role != 'fixe' else 0.5, role)
    return P
P1 = grid(22, True)
q = P1(1, 1)
disc(ax, *q, 1.5, 'limite', fill=False)
P2 = grid(66, False)
a, b, c = P2(1, 0), P2(0, 1), P2(1, 1)
arrow(ax, (a[0], a[1] + 1.6), (c[0], c[1] - 1.8), 'varie', lw=0.9)
arrow(ax, (b[0] + 1.6, b[1]), (c[0] - 1.8, c[1]), 'varie', lw=0.9)
text(ax, 22, 56, r'$N_1\cup N_2$ : réunion', 'encre', 's')
text(ax, 66, 56, r'$N_1+N_2$ : somme', 'encre', 's')
text(ax, 22, 8, r'$(1\,;\,1)$ n’y est pas', 'limite', 's')
text(ax, 66, 8, r'$(1\,;\,1)=y_1+y_2$ y est', 'resultat', 's')
text(ax, 41.5, 32, r'$N_1$', 'sujet', 's')
text(ax, 28, 52.5, r'$N_2$', 'autre', 's')
save(fig, '57-135')
