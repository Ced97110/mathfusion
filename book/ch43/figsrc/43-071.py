import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 2, 6, 84, 38, 'fixe', fill=False, dash=True)
text(ax, 8, 48, r'$S$', 'fixe', 'l')
specs = [(5, 9, 24, 28, 'fixe', [(6, 7), (14, 7), (6, 20), (16, 20), (20, 13)]),
         (33, 9, 24, 28, 'sujet', [(7, 8), (14, 20), (18, 9)]),
         (61, 9, 24, 28, 'fixe', [(6, 7), (16, 8), (8, 20), (17, 20)])]
for x, y, w_, h, rl, pts in specs:
    box(ax, x, y, w_, h, rl, fill=(rl == 'sujet'))
    for dx, dy in pts: disc(ax, x + dx, y + dy, 1.3, 'fixe' if rl == 'fixe' else 'sujet')
disc(ax, 33 + 7, 9 + 8, 1.6, 'varie'); text(ax, 40 + 3, 17 - 0.5, r'$a$', 'varie', 'm', ha='left')
text(ax, 45, 41, r'$\bar{a}$', 'sujet', 'm')
text(ax, 44, 53, r'$a\,E\,a$ : $a$ est dans sa classe', 'varie', 'm')
save(fig, '43-071')
