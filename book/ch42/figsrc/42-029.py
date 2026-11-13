import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
for x, t, r in [(8, r'$\{$', 'sujet'), (24, r'$a$', 'varie'), (34, ',', 'fixe'), (44, r'$b$', 'varie'), (54, ',', 'fixe'), (64, r'$c$', 'varie'), (80, r'$\}$', 'sujet')]:
    text(ax, x, 38, t, r, 22)
for x, t in [(24, 'gourde'), (44, 'carte'), (64, 'lampe')]: text(ax, x, 28, t, 'varie', 's')
for x in (34, 54): text(ax, x, 28, 'virgule', 'fixe', 's')
brace(ax, 4, 84, 46, 'sujet', label='accolades', down=False)
brace(ax, 18, 70, 23, 'varie', label='3 éléments')
save(fig, '42-029')
