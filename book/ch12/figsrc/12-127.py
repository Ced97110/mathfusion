import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x = 52
rows = [(r'$99/70$', '1,4142', '857…', 44), (r'$\sqrt{2}$', '1,4142', '135…', 26)]
for lab, a, b, y in rows:
    text(ax, 4, y, lab, 'sujet' if 'sqrt' in lab else 'autre', 'l', ha='left')
    text(ax, x, y, a, 'fixe', 'l', ha='right', weight='bold')
    text(ax, x, y, b, 'limite', 'l', ha='left', weight='bold')
brace(ax, 17.5, x, 20, 'fixe', label='mêmes chiffres', down=True)
brace(ax, x, x + 20, 20, 'limite', label='différents', down=True)
text(ax, 44, 53, 'proche n’est pas égal', 'varie', 'm')
text(ax, 44, 35, r'$=$ ?', 'varie', 'm')
save(fig, '12-127')
