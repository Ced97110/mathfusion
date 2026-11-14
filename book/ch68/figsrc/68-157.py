import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
def chip(x, bits, role):
    for r, b in enumerate(bits):
        box(ax, x, 52 + (2 - r) * 5.5, 6, 5.5, role, label=b)
chip(4, '110', 'sujet')
chip(20, '111', 'sujet')
chip(36, '001', 'resultat')
chip(52, '001', 'sujet')
for x, s in ((13, '+'), (29, '='), (45, '=')):
    text(ax, x, 60, s, 'encre', 'm')
for x, s in ((7, 'colonne 6'), (23, 'colonne 7'), (39, 'syndrome'), (55, 'colonne 1')):
    text(ax, x, 74, s, 'encre', 's')
w, h, x0 = 5.5, 6, 46
def word(y, bits, roles):
    for i, b in enumerate(bits):
        box(ax, x0 + i * w, y, w, h, roles[i], label=b)
word(26, '0011010', ['fixe'] * 5 + ['varie', 'varie'])
text(ax, 2, 29, 'reçu', 'encre', 's', ha='left')
arrow(ax, (55, 51), (x0 + w / 2, 33), 'resultat')
text(ax, 2, 23, 'on inverse le bit 1', 'varie', 's', ha='left')
text(ax, 2, 40, 'syndrome = colonne 1 :\nil désigne le bit 1', 'resultat', 's', ha='left')
arrow(ax, (x0 + w / 2, 25), (x0 + w / 2, 21.5), 'varie')
word(14, '1011010', ['limite'] + ['fixe'] * 4 + ['limite', 'limite'])
text(ax, 2, 17, 'corrigé', 'encre', 's', ha='left')
brace(ax, x0, x0 + w, 14, 'limite', label='ajouté')
brace(ax, x0 + 5 * w, x0 + 7 * w, 14, 'varie', label='de départ')
text(ax, 44, 1.5, '3 bits faux : 2 de départ + 1 ajouté', 'limite', 's')
save(fig, '68-157')
