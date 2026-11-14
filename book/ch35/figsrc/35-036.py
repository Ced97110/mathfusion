import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [('départ', 'fixe', r'$R\cos\alpha=3\ ;\ R\sin\alpha=4$', 'sujet'),
        ('1. carrés', 'fixe', r'$R^2\cos^2\alpha=9\ ;\ R^2\sin^2\alpha=16$', 'sujet'),
        ('2. additionner', 'fixe', r'$R^2\cos^2\alpha+R^2\sin^2\alpha=25$', 'sujet'),
        ('3. facteur commun', 'fixe', r'$R^2(\cos^2\alpha+\sin^2\alpha)=25$', 'sujet'),
        (r'4. $\cos^2+\sin^2=1$', 'varie', r'$R^2\times1=25$', 'resultat')]
for i, (lab, lr, expr, role) in enumerate(rows):
    y = 61 - 13 * i
    text(ax, 2, y + 4.5, lab, lr, 's', ha='left', weight='bold' if lr == 'varie' else 'normal')
    box(ax, 33, y, 53, 9, role, label=expr, size='s')
    if i < 4: arrow(ax, (59.5, y), (59.5, y - 4), 'varie' if i == 3 else 'fixe')
save(fig, '35-036')
