import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
rows = [r"$a$", r"$=a\vee O$", r"$=a\vee(a\wedge a')$", r"$=(a\vee a)\wedge(a\vee a')$", r"$=(a\vee a)\wedge I$", r"$=a\vee a$"]
ys = [64 - 12 * i for i in range(6)]
for i, (y, r) in enumerate(zip(ys, rows)):
    role = 'sujet' if i == 0 else ('varie' if i == 3 else ('resultat' if i == 5 else 'fixe'))
    box(ax, 2, y, 50, 8, role, label=r, size='m')
    if i < 5:
        dec = (i == 2)
        arrow(ax, (27, y), (27, ys[i + 1] + 8), 'varie' if dec else 'fixe', lw=1.8 if dec else 0.9)
text(ax, 56, 38, "A3 : l'étape décisive", 'varie', 's', ha='left')
text(ax, 56, 68, 'départ', 'sujet', 's', ha='left')
text(ax, 56, 8, 'arrivée', 'resultat', 's', ha='left')
save(fig, '80-422')
