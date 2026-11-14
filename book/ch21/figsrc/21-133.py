import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cols = [(2, 'Noté avant', 'resultat', r'$a\neq 4$ noté', 'reconnu : refusé', 'resultat'),
        (46, 'Rien noté', 'fixe', 'rien écrit', 'gardé : faux', 'limite')]
for x, head, r0, t0, t3, r3 in cols:
    text(ax, x + 20, 73, head, 'encre', 'm', weight='bold')
    box(ax, x, 52, 40, 11, r0, label=t0)
    arrow(ax, (x + 20, 51), (x + 20, 43), 'varie')
    box(ax, x, 32, 40, 10, 'sujet', label=r'candidat $a=4$')
    arrow(ax, (x + 20, 31), (x + 20, 23), 'varie')
    box(ax, x, 8, 40, 14, r3, label=t3)
save(fig, '21-133')
