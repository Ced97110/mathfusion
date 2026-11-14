import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)

def chain(y, head, gal, inv, verdict, vrole):
    text(ax, 44, y + 17, head, 'sujet', 'm')
    box(ax, 2, y, 20, 11, 'sujet', label=r'$F=\mathbb{Q}$', size='s')
    arrow(ax, (22, y + 5.5), (30, y + 5.5), 'varie')
    text(ax, 26, y + 9.5, 'Gal', 'varie', 's')
    box(ax, 30, y, 22, 11, 'fixe', label=gal, size='s')
    arrow(ax, (52, y + 5.5), (60, y + 5.5), 'varie')
    text(ax, 56, y + 9.5, 'Inv', 'varie', 's')
    box(ax, 60, y, 24, 11, vrole, label=inv, size='s')
    text(ax, 44, y - 5, verdict, vrole, 's')

chain(48, r'$\mathbb{Q}(\sqrt{2})/\mathbb{Q}$', r'$\{1,\sigma\}$', r'$\mathbb{Q}$', r'Inv = $F$ : galoisienne', 'resultat')
chain(12, r'$\mathbb{Q}(r)/\mathbb{Q}$', r'$\{1\}$', r'$\mathbb{Q}(r)$', r'Inv $\neq F$ : pas galoisienne', 'limite')
save(fig, '63-103')
