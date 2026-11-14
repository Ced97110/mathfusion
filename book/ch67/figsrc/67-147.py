import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
box(ax, 4, 80, 80, 10, 'limite', label=r'conjugués : $u$ seul, pas dans $\mathbb{Q}$')
text(ax, 44, 72,r'$m_u$ pour $u=\sqrt[3]{2}$' + '\n' + r'dans la base $1,u,u^2$', 'encre', 's')
M = [[0, 0, 2], [1, 0, 0], [0, 1, 0]]
for i in range(3):
    for j in range(3):
        role = 'sujet' if i == j else ('autre' if M[i][j] != 0 else 'fixe')
        box(ax, 29 + 10 * j, 56 - 10 * i, 9, 9, role, label=str(M[i][j]))
box(ax, 4, 10, 38, 11, 'sujet', label=r'diagonale : $T=0$', size='s')
box(ax, 46, 10, 38, 11, 'autre', label=r'$N=\det=2$', size='s')
text(ax, 44, 29, 'dans $\\mathbb{Q}$ : la définition par la matrice marche', 'resultat', 's')
save(fig, '67-147')
