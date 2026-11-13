import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
R = {'a': 'sujet', 'b': 'autre'}
def word(x, y, w, rl, s=5):
    for i, ch in enumerate(w): box(ax, x + i * s, y, s, s, rl, label=ch, size='m', r=0.5)
text(ax, 44, 63, 'mise bout à bout', 'varie', 'm')
word(4, 48, 'ab', 'sujet'); word(20, 48, 'bba', 'autre')
text(ax, 17, 50.5, '+', 'encre', 'm')
arrow(ax, (38, 50.5), (46, 50.5), 'varie')
word(50, 48, 'abbba', 'resultat')
text(ax, 52.5, 44, 'ab', 'sujet', 's', ha='left'); text(ax, 68, 44, 'bba', 'autre', 's', ha='left')
text(ax, 44, 34, '3 lettres b : toutes gardées', 'resultat', 's')
text(ax, 44, 23, 'réunion de deux ensembles', 'fixe', 's')
text(ax, 44, 13, r'$\{a,b\}\cup\{b\}=\{a,b\}$', 'fixe', 'm')
text(ax, 44, 5, 'un seul b : répétition perdue', 'limite', 's')
save(fig, '44-076')
