import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 23, 78, 'corps infini : 3 sous-corps', 'limite', 's'); text(ax, 69, 78, 'diviseurs de 4 : 1 seul', 'resultat', 's')
top, mid, bot = (23, 60), [(9, 40), (23, 40), (37, 40)], (23, 20)
labs = [r'$\mathbb{Q}(\sqrt{2})$', r'$\mathbb{Q}(\sqrt{3})$', r'$\mathbb{Q}(\sqrt{6})$']
for m in mid:
    line(ax, [(bot[0], bot[1] + 4.5), (m[0], m[1] - 4.5)], 'fixe'); line(ax, [(m[0], m[1] + 4.5), (top[0], top[1] - 4.5)], 'fixe')
for m, s in zip(mid, labs): box(ax, m[0] - 7, m[1] - 4.5, 14, 9, 'limite', label=s, size='s')
box(ax, top[0] - 12, top[1] - 4.5, 24, 9, 'sujet', label=r'$\mathbb{Q}(\sqrt{2},\sqrt{3})$', size='s')
box(ax, bot[0] - 5, bot[1] - 4.5, 10, 9, 'sujet', label=r'$\mathbb{Q}$', size='s')
c = [(69, 60), (69, 40), (69, 20)]
line(ax, [(69, 54.8), (69, 45.2)]); line(ax, [(69, 34.8), (69, 25.2)])
for (x, y), s, r in zip(c, ('4', '2', '1'), ('sujet', 'resultat', 'sujet')): disc(ax, x, y, 5, r, label=s)
text(ax, 44, 6, r'deux niveaux : 3 contre 1 au niveau de degré 2', 'encre', 's')
save(fig, '67-108')
