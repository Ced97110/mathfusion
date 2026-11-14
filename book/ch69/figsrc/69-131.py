import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
xs = [30, 46, 62, 78]
rows = [(52, ['−', '+', '−', '+'], 'en −μ = −5\n3 changements'),
        (32, ['+', '+', '+', '+'], 'en μ = 5\n0 changement')]
for y, sg, lab in rows:
    text(ax, 2, y, lab, 'encre', 's', ha='left')
    for x, s in zip(xs, sg):
        disc(ax, x, y, 3.5, 'sujet', label=s)
    for i in range(3):
        if sg[i] != sg[i + 1]:
            arrow(ax, (xs[i] + 4.2, y), (xs[i + 1] - 4.2, y), 'varie')
brace(ax, 26, 82, 58, 'sujet', label=r'suite écrite en $p$ et $q$', down=False)
text(ax, 62, 42, 'chaque signe : −, 0 ou +', 'fixe', 's')
box(ax, 3, 6, 36, 12, 'fixe', label=r'$V(-\mu)>V(\mu)$')
arrow(ax, (40, 12), (49, 12), 'varie')
box(ax, 50, 6, 36, 12, 'resultat', label='conditions de signe\nen $p$ et $q$', size='s')
save(fig, '69-131')
