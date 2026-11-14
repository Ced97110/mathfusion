import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [('1. calculer R', r'$R=\sqrt{9+16}=5$', 'sujet'),
        ('2. chercher α', r'$\cos\alpha=\frac{3}{5}\ ;\ \sin\alpha=\frac{4}{5}$', 'sujet'),
        ('3. écrire', r'$3\sin x-4\cos x=5\sin(x-\alpha)$', 'varie'),
        ('4. vérifier', r'$x=0:\ 5\times(-0{,}8)=-4$', 'resultat')]
for i, (lab, expr, role) in enumerate(rows):
    y = 55 - 17 * i
    text(ax, 3, y + 14.5, lab, role, 's', ha='left', weight='bold')
    box(ax, 3, y + 1, 82, 11, role, label=expr, size='s')
    if i < 3: arrow(ax, (44, y + 1), (44, y - 3), 'fixe')
save(fig, '35-044')
