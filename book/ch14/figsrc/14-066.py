import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'Trois écritures, un nombre', 'fixe', 'm')
rows = [('248,0', r'$\times\,10$'), ('24,80', r'$\times\,10^{2}$'), ('2,480', r'$\times\,10^{3}$')]
for i, (num, pw) in enumerate(rows):
    y = 44 - i * 18
    box(ax, 4, y, 30, 12, 'sujet', label=num, size='l')
    text(ax, 46, y + 6, pw, 'varie', 'l')
    text(ax, 70, y + 6, '= 2 480', 'resultat', 'l')
save(fig, '14-066')
