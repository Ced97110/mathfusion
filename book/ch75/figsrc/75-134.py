import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
S = 11
for i in range(3):
    for j in range(3):
        role = 'resultat' if (i, j) == (0, 0) else ('sujet' if i == 0 else ('varie' if j == 0 else 'fixe'))
        box(ax, 12 + S * i, 12 + S * j, S, S, role)
    text(ax, 12 + S * i + S / 2, 7, str(i), 'fixe', 's'); text(ax, 7, 12 + S * i + S / 2, str(i), 'fixe', 's')
text(ax, 28.5, 3, r'$u$ : colonnes', 'fixe', 's'); text(ax, 28.5, 49, r'$v$ : lignes', 'fixe', 's')
for k, (role, s) in enumerate([('sujet', r'$u=0$ : 3 couples'), ('varie', r'$v=0$ : 3 couples'), ('resultat', r'$(0,0)$ : deux fois')]):
    box(ax, 51, 38 - 9 * k - 2.5, 5, 5, role); text(ax, 58, 38 - 9 * k, s, role, 's', ha='left')
text(ax, 67, 8, r'$3+3-1=5$', 'resultat', 'm')
save(fig, '75-134')
