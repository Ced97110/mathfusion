import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 48, 'Ferrari, degré 4', 'sujet', 'l', weight='bold')
chips = [('racine carrée', 'sujet', "d'abord"), ('racine cubique', 'varie', 'puis'), ('racine carrée', 'sujet', 'encore')]
for i, (lab, role, when) in enumerate(chips):
    x = 3 + i * 29.5
    box(ax, x, 24, 24, 12, role, label=lab, size='s')
    text(ax, x + 12, 19, when, 'fixe', 's')
    if i > 0: arrow(ax, (x - 5.2, 30), (x - 0.5, 30), 'fixe')
brace(ax, 2, 86, 14, 'resultat', label='trois extractions à la suite')
save(fig, '64-004')
