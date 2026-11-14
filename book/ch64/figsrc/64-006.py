import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(40, r'$x^2=5$', r'$x=\sqrt{5}$', 'resultat', '1 étape'),
        (26, r'$x^3=8$', r'$x=\sqrt[3]{8}=2$', 'resultat', '1 étape'),
        (12, 'troisième équation', 'décimales seulement', 'fixe', 'inexacte')]
for y, eq, sol, role, note in rows:
    box(ax, 2, y, 24, 11, 'sujet', label=eq, size='s')
    arrow(ax, (27, y + 5.5), (38, y + 5.5), role if role != 'fixe' else 'fixe')
    box(ax, 39, y, 32, 11, role, label=sol, size='s', dash=(role == 'fixe'))
    if note: text(ax, 73, y + 5.5, note, role, 's', ha='left')
text(ax, 44, 4, 'approchée ≠ écriture exacte', 'fixe', 's')
text(ax, 44, 57, 'racines et opérations, en un nombre fini d’étapes', 'sujet', 's')
save(fig, '64-006')
