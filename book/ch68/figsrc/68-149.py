import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
w, h, x0 = 8.5, 6, 20
rows = [
    (74, '0011001', ['fixe'] * 7, 'envoyé'),
    (50, '0011010', ['fixe'] * 5 + ['varie', 'varie'], 'reçu'),
    (22, '1011010', ['limite', 'fixe', 'fixe', 'fixe', 'fixe', 'limite', 'limite'], 'corrigé'),
]
for y, bits, roles, name in rows:
    for i, b in enumerate(bits):
        box(ax, x0 + i * w, y, w, h, roles[i], label=b)
    text(ax, 2, y + h / 2, name, 'encre', 's', ha='left')
text(ax, 50, 66, 'deux bits inversés : 6 et 7', 'varie', 's')
text(ax, 50, 42.5, 'A, B pairs, C impair : bit 1', 'encre', 's')
arrow(ax, (8, 72), (8, 59), 'varie')
arrow(ax, (8, 48), (8, 35), 'varie')
arrow(ax, (x0 + w / 2, 41), (x0 + w / 2, 29.5), 'varie')
text(ax, x0 + w / 2 + 3, 35, 'on inverse le bit 1', 'varie', 's', ha='left')
brace(ax, x0, x0 + w, 22, 'limite', label='ajoutée')
brace(ax, x0 + 5 * w, x0 + 7 * w, 22, 'varie', label='de départ')
text(ax, 50, 4, '3 erreurs : 2 de départ + 1 ajoutée', 'limite', 's', weight='bold')
save(fig, '68-149')
