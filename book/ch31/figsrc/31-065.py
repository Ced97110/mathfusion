import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [('identité : démontrée', 'sujet', 'vrai pour toutes les valeurs', ['−5 : vrai', '0 : vrai', '2 : vrai']),
        ('équation', 'autre', 'vraie pour certaines valeurs', ['2 : faux', '3 : vrai']),
        ('égalité essayée', 'fixe', '2 testées, sans preuve', ['35° : vrai', '60° : vrai'])]
for i, (title, role, cap, labs) in enumerate(rows):
    yt = 66 - 23 * i
    text(ax, 6, yt, title, role, 'l', ha='left', weight='bold')
    for k in range(5):
        if i == 0: r = 'resultat'
        elif i == 1: r = 'resultat' if k == 1 else 'limite'
        else: r = 'resultat' if k < 2 else 'fixe'
        box(ax, 5 + k * 16, yt - 12, 14, 8, r, label=labs[k] if k < len(labs) else None, size='s')
    text(ax, 6, yt - 15.5, cap, role, 's', ha='left')
save(fig, '31-065')
