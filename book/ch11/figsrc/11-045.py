import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
for j, b in enumerate(['mètre', 'gramme', 'litre']):
    text(ax, 40 + j * 16, 62, b, 'fixe', 's')
data = [('kilo 1 000', ['km', 'kg', 'kL']), ('milli 0,001', ['mm', 'mg', 'mL'])]
for i, (r, cells) in enumerate(data):
    y = 38 - i * 16
    text(ax, 2, y + 5, r, 'sujet', 's', ha='left')
    for j, c in enumerate(cells):
        box(ax, 32 + j * 16, y, 16 - 1.5, 10, 'resultat', label=r'$%s$' % c)
text(ax, 44, 17, '', 'encre', 's')
text(ax, 44, 12, '6 préfixes × 3 bases = 18 unités', 'encre', 's')
text(ax, 44, 5, 'mais seulement 6 nombres à apprendre', 'sujet', 's')
save(fig, '11-045')
