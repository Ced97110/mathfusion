import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, 'un nombre multiplié par lui-même', 'encre', 's')
data = [(r'$1{,}4\cdot1{,}4$', r'$1{,}96$', 'limite'), (r'$1{,}41\cdot1{,}41$', r'$1{,}9881$', 'limite'),
        (r'$1{,}42\cdot1{,}42$', r'$2{,}0164$', 'limite')]
for i, (a, b, r) in enumerate(data):
    y = 52 - i * 14
    box(ax, 4, y, 40, 11, 'fixe', label=a, size='m')
    arrow(ax, (45, y + 5.5), (53, y + 5.5), 'varie')
    box(ax, 54, y, 30, 11, r, label=b + r'$\neq2$', size='m')
y = 10
box(ax, 4, y, 40, 11, 'sujet', label=r'$\sqrt{2}\cdot\sqrt{2}$', size='m')
arrow(ax, (45, y + 5.5), (53, y + 5.5), 'varie')
box(ax, 54, y, 30, 11, 'resultat', label=r'$2$ exact', size='m')
text(ax, 44, 3.5, r'$\sqrt{2}$ est positif ($-\sqrt{2}$ écarté)', 'sujet', 's')
save(fig, '12-125')
