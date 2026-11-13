import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 3, 24, 32, 24, 'sujet', fill=False, lw=1.2)
text(ax, 19, 44, 'alphabet', 'sujet', 's', weight='bold')
box(ax, 6, 27, 11, 11, 'sujet', label=r'$x$')
box(ax, 21, 27, 11, 11, 'sujet', label=r'$y$')
box(ax, 13.5, 6, 11, 11, 'fixe', fill=False, dash=True, label=r'$z$')
text(ax, 19, 2.5, 'non choisie', 'fixe', 's')
def word(y, letters, roles):
    for i, (l, r) in enumerate(zip(letters, roles)):
        box(ax, 44 + i * 8, y, 7.5, 9, r, label=l)
word(34, [r'$x$', r'$x$', r'$y$'], ['sujet', 'sujet', 'sujet'])
word(12, [r'$x$', r'$z$'], ['sujet', 'limite'])
text(ax, 70, 38.5, 'permis', 'resultat', 's', ha='left')
text(ax, 62, 16.5, 'interdit', 'limite', 's', ha='left')
text(ax, 58, 46, 'des suites de lettres', 'encre', 's')
save(fig, '49-019')
