import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 3, 24, 82, 44, 'fixe', fill=False, dash=True)
text(ax, 44, 63, r'$\mathbb{Z}$ : une infinité d\'entiers'.replace("\\'", "’"), 'fixe', 'm')
n = 14
for i in range(n):
    x = 8 + i * 5.5
    if True: disc(ax, x, 53, 1.6, 'fixe')
text(ax, 45, 53, r'$\cdots$', 'fixe', 'm') if False else None
box(ax, 24, 32, 40, 13, 'sujet', label=r'$\{1,\,-1\}$', size='l')
text(ax, 44, 27.8, 'seules unités', 'sujet', 's')
text(ax, 44, 17, r'$1\times1=1$', 'resultat', 'm')
text(ax, 44, 10, r'$(-1)\times(-1)=1$', 'resultat', 'm')
text(ax, 44, 3.5, 'un groupe pour la multiplication', 'resultat', 's')
save(fig, '51-060')
