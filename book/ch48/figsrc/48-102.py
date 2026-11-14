import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 4, 18, 48, 26, 'sujet', dash=False)
text(ax, 28, 50, r'$H=\{0,4,8\}$', 'sujet', 'm')
for x, s in [(42, '0'), (14, '4'), (28, '8')]:
    disc(ax, x, 31, 4.5, 'sujet', label=s)
disc(ax, 72, 31, 4.5, 'limite', label='6')
arrow(ax, (46.6, 31), (67.4, 31), 'varie', both=True)
text(ax, 72, 40, r'$6\notin H$', 'limite', 's')
text(ax, 60, 25, r'paquet $0K$', 'varie', 's')
text(ax, 44, 8, r'$H$ ne contient pas $K$', 'limite', 'm')
save(fig, '48-102')
