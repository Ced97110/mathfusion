import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
parts = [(r'$f$', 'varie', 22), (':', 'fixe', 32), (r'$G$', 'sujet', 43), (r'$\to$', 'fixe', 55), (r"$G'$", 'autre', 67)]
for s, r, x in parts: text(ax, x, 66, s, r, 15)
rows = [(r'$f$', 'varie', "nom de l'application"), (r'$G$', 'sujet', 'groupe de départ'),
        (r'$\to$', 'fixe', 'envoie vers'), (r"$G'$", 'autre', "groupe d'arrivée")]
for i, (s, r, lab) in enumerate(rows):
    y = 46 - i * 12
    box(ax, 6, y - 4.5, 16, 9, r, label=s)
    text(ax, 28, y, lab, r, 'm', ha='left')
save(fig, '48-027')
