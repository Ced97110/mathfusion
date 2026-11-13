import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, 'la partie : les entiers impairs', 'sujet', 's')
rows = [(3, 1, 2, 'fixe', 'pas équivalents : normal'), (5, 3, 2, 'fixe', 'pas équivalents : normal'), (1, 1, 0, 'limite', 'échec : 0 est absent')]
for i, (a, b, d, role, note) in enumerate(rows):
    y = 54 - 20 * i
    disc(ax, 8, y, 3.6, 'sujet', label=str(a), size='m'); disc(ax, 22, y, 3.6, 'sujet', label=str(b), size='m')
    text(ax, 40, y, r'$%d-%d=%d$' % (a, b, d), role, 'm')
    box(ax, 54, y - 7, 32, 14, role, label=note.replace(' : ', '\n'), size='s')
save(fig, '52-030')
