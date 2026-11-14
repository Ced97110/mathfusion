import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(85)
text(ax, 44, 79, '⟨3⟩ dans l’horloge à 12', 'sujet', 's'); text(ax, 44, 8, 'horloge à 4', 'autre', 's')
top = [0, 3, 6, 9]
for i, v in enumerate(top):
    x = 14 + i * 20
    hl = v in (3, 6, 9)
    box(ax, x - 6, 58, 12, 10, 'sujet', label=str(v), lw=1.4 if hl else 0.8)
    box(ax, x - 6, 22, 12, 10, 'autre', label=str(i), lw=1.4 if hl else 0.8)
    arrow(ax, (x, 57), (x, 33), 'resultat', both=True)
text(ax, 44, 45, 'n ↔ 3 × n', 'resultat', 's', ha='left') if False else None
text(ax, 44, 45, '3 × n ↔ n', 'resultat', 's')
text(ax, 34, 72.5, '3 + 6 = 9', 'sujet', 's'); text(ax, 34, 15, '1 + 2 = 3', 'autre', 's')
save(fig, '48-189')
