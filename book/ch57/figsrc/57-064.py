import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 13, 62, 'R = ℤ', 'fixe', 's')
text(ax, 73, 62, 'End M  (M = ℤ²)', 'fixe', 's')
text(ax, 42, 62, r'$\eta$', 'sujet', 'l', weight='bold')
rows = [(48, '3', 'tripler', None), (34, '1', 'ne rien changer', 'respecte le un'),
        (20, r'$3+2$', 'tripler + doubler', 'respecte +'), (6, r'$3\times 2$', 'tripler ∘ doubler', 'respecte ×')]
for y, left, right, note in rows:
    box(ax, 2, y, 22, 9, 'varie', label=left)
    arrow(ax, (25, y + 4.5), (59, y + 4.5), 'sujet', lw=1.3)
    box(ax, 60, y, 26, 9, 'sujet', label=right, size='s')
    if note: text(ax, 42, y + 8, note, 'fixe', 's')
save(fig, '57-064')
