import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, r'4 parties de $S=\{1,2\}$', 'fixe', 's')
parts = [('fixe', r'$\varnothing$'), ('sujet', r'$\{1\}$'), ('autre', r'$\{2\}$'), ('resultat', r'$\{1,2\}$')]
for i, (role, lab) in enumerate(parts):
    box(ax, 3 + i * 21.5, 50, 19, 10, role, label=lab, size='m')
def eq(y, a, op, b, c, ra, rb, rc):
    items = [(a, ra), (None, op), (b, rb), (None, '='), (c, rc)]
    xs = [4, 25, 31, 52, 58]; ws = [18, 6, 18, 6, 22]
    for (lab, r), x, wd in zip(items, xs, ws):
        if lab is None: text(ax, x + wd / 2, y + 5, r, 'encre', 'l')
        else: box(ax, x, y, wd, 10, r, label=lab, size='m')
eq(30, r'$\{1\}$', r'$\cup$', r'$\{2\}$', r'$\{1,2\}$', 'sujet', 'autre', 'resultat')
eq(10, r'$\varnothing$', r'$\cup$', r'$\{1\}$', r'$\{1\}$', 'fixe', 'sujet', 'sujet')
text(ax, 84, 25, 'réunion', 'varie', 's', ha='right'); text(ax, 84, 5, 'le vide ne change rien', 'fixe', 's', ha='right')
save(fig, '44-073')
