import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
u = 3.6
text(ax, 77, 52, 'corrige une\nerreur isolée ?', 'encre', 's')
rows = [('répétition', 8, 'oui', 'resultat', 38), ('parité', 1, 'non', 'limite', 24), ('Hamming', 3, 'oui', 'resultat', 10)]
for name, add, verdict, vr, y in rows:
    text(ax, 2, y + 4.5, name, 'sujet' if name == 'Hamming' else 'encre', 's', ha='left', weight='bold' if name == 'Hamming' else 'normal')
    box(ax, 22, y, 4 * u, 9, 'fixe', label='4 utiles', size='s')
    box(ax, 22 + 4 * u, y, add * u, 9, 'varie', label=f'+{add}', size='s')
    text(ax, 77, y + 4.5, verdict, vr, 'm', weight='bold')
text(ax, 44, 3, 'total envoyé : 12, 5 et 7 bits', 'encre', 's')
save(fig, '68-011')
