import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
assert 1j * -1j == 1 and 6 % 4 == 2 and 4 % 2 == 0
text(ax, 2, 59, r'$\mathbb{Z}[i]$ : 1 étape', 'sujet', 'm', ha='left', weight='bold')
w, g = 26, 3
rows = [(36, 'sujet', ['$7+2i$ divisé\npar $2+i$ : reste $i$', '$i\\times(-i)=1$\n$i$ est une unité', 'PGCD :\nune unité'], ['sujet', 'sujet', 'resultat']),
        (6, 'autre', ['6 divisé par 4\nreste 2', '4 divisé par 2\nreste 0', 'PGCD $=2$\npas une unité'], ['autre', 'autre', 'fixe'])]
text(ax, 2, 29, r'$\mathbb{Z}$ : 2 étapes', 'autre', 'm', ha='left', weight='bold')
for y, _, labs, roles in rows:
    for i, (lab, role) in enumerate(zip(labs, roles)):
        x = 2 + i * (w + g)
        box(ax, x, y, w, 16, role, label=lab, size='s')
        if i < 2:
            arrow(ax, (x + w + 0.2, y + 8), (x + w + g - 0.2, y + 8), 'fixe')
save(fig, '56-179')
