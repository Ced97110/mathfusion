import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 13, 70, r'$\mathbb{Z}$', 'fixe', 'l')
text(ax, 73, 70, r'$\mathbb{F}_4$', 'sujet', 'l')
text(ax, 43, 70, r'$\varphi(n)=n\cdot1$', 'varie', 's')
ly = [60, 48, 36, 24, 12]
for n, y in enumerate(ly):
    box(ax, 6, y, 14, 8, 'fixe', label=str(n))
ry = {0: 56, 1: 42, 2: 28, 3: 14}
rl = [('0', 'resultat', False), ('1', 'resultat', False), (r'$\alpha$ non atteint', 'fixe', True), (r'$\alpha+1$ non atteint', 'fixe', True)]
for (s, r, d), (k, y) in zip(rl, ry.items()):
    box(ax, 62, y, 22, 8, r, label=s, dash=d, size='s')
for n, y in enumerate(ly):
    t = ry[n % 2] + 4
    arrow(ax, (20, y + 4), (62, t), 'varie', lw=0.8)
text(ax, 44, 4, r'$\varphi(3)=1+1+1=1$', 'sujet', 'm')
save(fig, '67-040')
