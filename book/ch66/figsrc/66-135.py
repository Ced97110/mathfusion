import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
labels = [('sujet', r'$\sqrt{\pi}$ est constructible'), ('fixe', r'$\sqrt{\pi}$ est algébrique'),
          ('varie', r'$\pi=(\sqrt{\pi})^{2}$ est algébrique'), ('limite', r'$\pi$ transcendant : faux')]
ys = [68, 50, 32, 14]
for (role, s), y in zip(labels, ys):
    box(ax, 2, y, 56, 11, role, label=s)
for y, s in zip(ys[:3], ['chapitre 61', 'A est un corps', 'Lindemann']):
    arrow(ax, (30, y), (30, y - 7), 'fixe')
    text(ax, 34, y - 3.5, s, 'fixe', 's', ha='left')
text(ax, 74, 73.5, r'$\approx1{,}7725$', 'sujet', 's')
text(ax, 74, 37.5, r'$\approx3{,}1416$', 'varie', 's')
save(fig, '66-135')
