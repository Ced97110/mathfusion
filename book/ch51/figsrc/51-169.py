import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
brace(ax, 4, 83, 54, 'sujet', label='quaternion : 4 réels', down=False)
for i in range(4):
    box(ax, 4 + 20 * i, 38, 18, 12, 'sujet', label=rf'$\alpha_{i}$', size='l')
for i, s in enumerate(['seul', r'$i$', r'$j$', r'$k$']):
    text(ax, 13 + 20 * i, 33, s, 'varie' if i else 'fixe', 'm')
brace(ax, 4, 42, 29.5, 'autre', label='nombre complexe', size='s')
text(ax, 23, 22, r'$\alpha_2=\alpha_3=0$', 'autre', 's')
brace(ax, 24, 83, 16.5, 'fixe', label="point de l'espace", size='s')
text(ax, 53.5, 9, r'$\alpha_0=0$', 'fixe', 's')
save(fig, '51-169')
