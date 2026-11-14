import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
for x, s in ((4, r'$K=\mathbb{F}_2$'), (32, r'$F=\mathbb{F}_4$'), (60, r'$E=\mathbb{F}_{16}$')): box(ax, x, 68, 24, 10, 'fixe', label=s, size='s')
text(ax, 29, 73, r'$\subset$', 'fixe', 's'); text(ax, 57, 73, r'$\subset$', 'fixe', 's')
c = 14
for i in range(2):
    for j in range(2):
        box(ax, 12 + j * c, 22 + i * c, c, c, 'resultat', lw=0.8, r=0.3)
arrow(ax, (12, 54), (12 + 2 * c, 54), 'sujet', both=True)
text(ax, 12 + c, 58, r'$[F:K]=m=2$', 'sujet', 's')
arrow(ax, (44, 22), (44, 22 + 2 * c), 'varie', both=True)
text(ax, 47, 36, r'$[E:F]=2$', 'varie', 's', ha='left')
text(ax, 26, 12, r'$4$ cases : $[E:K]=n=4$', 'resultat', 's')
text(ax, 26, 3, r'$4=2\times2$, donc $m$ divise $n$', 'encre', 's')
save(fig, '67-110')
