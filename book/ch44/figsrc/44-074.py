import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, r'4 parties de $S=\{1,2\}$', 'fixe', 's')
parts = [('fixe', r'$\varnothing$'), ('sujet', r'$\{1\}$'), ('autre', r'$\{2\}$'), ('resultat', r'$S=\{1,2\}$')]
for i, (role, lab) in enumerate(parts):
    box(ax, 3 + i * 21.5, 50, 19, 10, role, label=lab, size='s' if i == 3 else 'm')
def eq(y, a, b, c, ra, rb, rc, rbox):
    items = [(a, ra, 4, 18), (r'$\cap$', None, 25, 6), (b, rb, 31, 18), ('=' if rbox != 'limite' else r'$\neq$', None, 52, 6), (c, rc, 58, 22)]
    for lab, r, x, wd in items:
        if r is None: text(ax, x + wd / 2, y + 5, lab, 'encre', 'l')
        else: box(ax, x, y, wd, 10, r, label=lab, size='m')
eq(30, r'$\{1\}$', r'$\{1,2\}$', r'$\{1\}$', 'sujet', 'resultat', 'sujet', 'ok')
eq(10, r'$\varnothing$', r'$\{1\}$', r'$\{1\}$', 'fixe', 'sujet', 'limite', 'limite')
text(ax, 84, 25, 'S ne change rien : neutre', 'resultat', 's', ha='right'); text(ax, 84, 5, 'le vide n’est pas neutre', 'limite', 's', ha='right')
save(fig, '44-074')
