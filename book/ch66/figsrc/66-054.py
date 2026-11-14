import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 4, 54, r'$a+bi$', 'fixe', 'm', ha='left')
for k, l in enumerate([r'$a$', r'$b$']):
    box(ax, 28 + k * 14, 49, 12, 10, 'fixe', label=l)
text(ax, 60, 54, '2 rationnels', 'fixe', 'm', ha='left')
text(ax, 4, 28, r'$\mathbb{Q}(\zeta)$', 'sujet', 'm', ha='left')
for k in range(4):
    box(ax, 28 + k * 14, 23, 12, 10, 'sujet', label=rf'$a_{k + 1}$')
brace(ax, 28, 28 + 3 * 14 + 12, 21, 'sujet', label='4 rationnels')
text(ax, 60, 36, r'$\varphi(5)=4$', 'resultat', 'm', weight='bold')
text(ax, 44, 7, 'dimension = nombre de rationnels', 'encre', 's')
save(fig, '66-054')
