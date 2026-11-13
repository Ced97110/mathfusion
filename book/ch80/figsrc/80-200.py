import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [('entiers', r'$2^{2}=4\neq2$', 'faux', 'limite'),
        ('cadran à 4 h', r'$2^{2}=0\neq2$', 'faux', 'limite'),
        (r'$\mathbb{Z}/2$', r'$0^{2}=0$ ; $1^{2}=1$', 'vrai', 'resultat')]
text(ax, 44, 58, r'la règle $x^{2}=x$ est-elle vraie ?', 'sujet', 'm')
for k, (n, c, v, role) in enumerate(rows):
    y = 38 - k * 15
    box(ax, 2, y, 26, 11, 'fixe', label=n, size='s')
    box(ax, 30, y, 38, 11, role, label=c, size='s')
    box(ax, 70, y, 16, 11, role, label=v, size='s', weight='bold')
    arrow(ax, (28, y + 5.5), (30, y + 5.5), 'fixe') if False else None
save(fig, '80-200')
