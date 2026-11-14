import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(78)
w, h, x0, ytop = 9, 6, 9, 40
cols = [1, 2, 3, 4, 5, 6, 7, 1]  # the 8th column repeats column 1
for j, v in enumerate(cols):
    bits = [(v >> 2) & 1, (v >> 1) & 1, v & 1]
    role = 'limite' if j in (0, 7) else 'sujet'
    for r, b in enumerate(bits):
        box(ax, x0 + j * w, ytop + (2 - r) * h, w, h, role, label=str(b))
for r, name in enumerate('ABC'):
    text(ax, 4, ytop + (2 - r) * h + h / 2, name, 'encre', 's')
brace(ax, x0 + 1, x0 + 7 * w - 1, ytop - 1, 'fixe', label='les 7 colonnes possibles')
text(ax, x0 + 7.5 * w, ytop - 5, '8e', 'limite', 's')
xa, xb = x0 + w / 2, x0 + 7.5 * w
line(ax, [(xa, ytop + 3 * h + 1), (xa, ytop + 3 * h + 4), (xb, ytop + 3 * h + 4), (xb, ytop + 3 * h + 1)], 'limite')
text(ax, 48, ytop + 3 * h + 8, 'deux colonnes égales', 'limite', 's')
text(ax, 48, 72, r'$m = 3$ : 3 lignes, 8 colonnes', 'encre', 'm')
text(ax, 48, 20, 'somme des deux colonnes = 0', 'encre', 's')
text(ax, 48, 12, r'$d \leq 2$ : erreur non corrigée', 'limite', 's')
save(fig, '68-153')
