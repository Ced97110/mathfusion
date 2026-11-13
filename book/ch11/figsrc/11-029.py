import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, '1 h = 60 min', 'sujet', 'l', weight='bold')
f = numberline(ax, 24, 78, 28, 0, 3, labels=False, role='sujet', arrow_right=False)
for v in range(4):
    text(ax, f(v), 35, f'{v} h', 'sujet', 's'); text(ax, f(v), 21, f'{60 * v} min', 'varie', 's')
brace(ax, f(0), f(1), 17, 'resultat', label='60 min', size='s')
text(ax, 3, 28, 'durée', 'fixe', 's', ha='left')
text(ax, 44, 4, r'$2 \times 60 = 120$ ; $3 \times 60 = 180$', 'varie', 's')
save(fig, '11-029')
