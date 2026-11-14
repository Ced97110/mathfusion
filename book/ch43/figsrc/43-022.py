import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'le couple $(14\ ;\ 2)$', 'sujet', 'm')
rows = [('plus grand que', r'$14>2$', 'oui', 'resultat'),
        ('égaux', r'$14=2$', 'non', 'limite'),
        ('multiple de 12', r'$14-2=12$', 'oui', 'resultat')]
for i, (name, form, ans, role) in enumerate(rows):
    y = 40 - i*16
    text(ax, 3, y + 8.5, name, 'fixe', 's', ha='left')
    box(ax, 3, y - 5, 34, 10, 'sujet', label=form, size='m')
    arrow(ax, (38, y), (52, y), 'fixe')
    box(ax, 54, y - 5, 30, 10, role, label=ans, size='m')
save(fig, '43-022')
