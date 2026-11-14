import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx = [15, 44, 73]
for x, s in zip(cx, ['F', 'K', 'E']):
    text(ax, x, 50, f'${s}$', 'sujet', 'xl', weight='bold')
for x in (29.5, 58.5):
    text(ax, x, 50, r'$\subseteq$', 'varie', 'xl')
cont = ['fractions', r'$+\sqrt{2}$', r'$+\sqrt{2}$ et $\sqrt{3}$']
names = ['bas', 'milieu', 'haut']
for x, s, n in zip(cx, cont, names):
    box(ax, x - 13, 18, 26, 16, 'sujet', label=s, size='s')
    line(ax, [(x, 45), (x, 34)], 'sujet')
    text(ax, x, 13, n, 'fixe', 's')
text(ax, 44, 4, r'$\subseteq$ : « contenu dans »', 'varie', 's')
save(fig, '61-101')
