import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
box(ax, 20, 70, 48, 10, 'sujet', label=r'$(x-1)(x^2-2)$', size='l')
text(ax, 44, 63, r'$d = 8$ : pas un carré dans ℚ', 'fixe', 's')
labs = ['1', '(23)', '(12)', '(13)', '(123)', '(132)']
for i, s in enumerate(labs):
    box(ax, 3 + i * 14, 38, 12, 9, 'sujet' if i < 2 else 'fixe', label=s, size='s')
brace(ax, 3, 27, 48, 'sujet', r'groupe de $f$ : 2 éléments', down=False)
brace(ax, 3, 85, 37, 'limite', r'$S_3$ : 6 éléments (faux ici)', down=True)
box(ax, 8, 16, 72, 12, 'varie', label=r'$x-1$ est un facteur : $f$ réductible', size='s')
save(fig, '65-069')
