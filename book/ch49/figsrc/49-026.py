import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def blocks(y, first, second):
    x = 8
    for (n, role, lab) in (first, second):
        for i in range(n): box(ax, x + i * 9, y, 8.5, 9, role)
        text(ax, x + (n * 9 - 0.5) / 2, y + 13, lab, role, 'm')
        x += n * 9 + 2
        if x > 40: pass
blocks(32, (2, 'sujet', r'$a$'), (1, 'autre', r'$b$'))
text(ax, 62, 36.5, r'$ab$', 'encre', 'xl', weight='bold')
blocks(8, (1, 'autre', r'$b$'), (2, 'sujet', r'$a$'))
text(ax, 62, 12.5, r'$ba$', 'encre', 'xl', weight='bold')
brace(ax, 8, 8 + 27 + 2, 30, 'fixe', label='3 lettres')
text(ax, 62, 24, 'l’ordre compte', 'fixe', 's') if False else None
save(fig, '49-026')
