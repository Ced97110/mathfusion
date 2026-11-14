import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, 'Preuve 1 : à la main', 'autre', 's')
for x, s in zip((3, 24, 45, 66), ['1', r'$1+1$', r'$1+1+1$', r'$\ldots$']):
    box(ax, x, 60, 17, 10, 'autre', label=s, size='s')
for x in (20, 41, 62):
    arrow(ax, (x, 65), (x + 4, 65), 'autre')
text(ax, 30, 54, 'on constate : comme ' + r'$\mathbb{Z}/p\mathbb{Z}$', 'autre', 's')
text(ax, 35, 46, 'Preuve 2 : un théorème', 'sujet', 's')
box(ax, 4, 30, 62, 11, 'sujet', label='1er théorème d’isomorphisme', size='s')
text(ax, 35, 26, 'livré d’un coup, avec la raison', 'sujet', 's')
box(ax, 4, 4, 80, 11, 'resultat', label=r'même corps premier $\mathbb{F}_p$')
arrow(ax, (75, 59.5), (75, 15.5), 'autre')
arrow(ax, (35, 30), (35, 15.5), 'sujet')
save(fig, '67-045')
