import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
w, gap, x0 = 26, 3, 2
cols = [('inconnue', r'$3y=2$', 'on la cherche', 'autre'),
        ('variable', r'$x\mapsto x^2$', 'valeurs variées', 'autre'),
        ('indéterminée', r'$(0,1,0,\ldots)$', 'objet fixé', 'sujet')]
for i, (t, ex, note, role) in enumerate(cols):
    x = x0 + i * (w + gap)
    box(ax, x, 6, w, 36, role)
    text(ax, x + w / 2, 36, t, role, 'm', weight='bold')
    text(ax, x + w / 2, 24, ex, 'encre', 's')
    text(ax, x + w / 2, 12, note, role, 's')
save(fig, '54-101')
