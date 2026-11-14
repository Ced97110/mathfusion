import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 4, 66, 80, 11, 'sujet', label=r'un corps à $q$ éléments ($q=4,6,256$)', size='m')
names = ['existence', 'unicité', 'structure']
qs = ['Existe-t-il ?', 'Est-il unique ?', 'Comment est-il fait ?']
cx = [16, 44, 72]
for i in range(3):
    arrow(ax, (cx[i], 66), (cx[i], 49), 'fixe')
    box(ax, cx[i] - 12, 37, 24, 12, 'varie', label=names[i], size='m')
    text(ax, cx[i], 32, qs[i], 'encre', 's')
for i in range(2):
    arrow(ax, (cx[i] + 12, 43), (cx[i + 1] - 12, 43), 'varie')
box(ax, 10, 10, 12, 12, 'fixe', label='?', dash=True)
box(ax, 33, 10, 10, 12, 'fixe', label='?', dash=True)
box(ax, 45, 10, 10, 12, 'fixe', label='?', dash=True)
for i in range(2):
    for j in range(2):
        disc(ax, 68 + 8 * j, 12 + 8 * i, 2.8, 'sujet')
line(ax, [(68, 12), (76, 12)], 'sujet'); line(ax, [(68, 20), (76, 20)], 'sujet')
line(ax, [(68, 12), (68, 20)], 'sujet'); line(ax, [(76, 12), (76, 20)], 'sujet')
save(fig, '67-003')
