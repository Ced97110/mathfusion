import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

M = [[3, 3], [2, 5]]
v = [4, 18]
raw = [M[i][0] * v[0] + M[i][1] * v[1] for i in range(2)]
res = [r % 26 for r in raw]
assert raw == [66, 98] and res == [14, 20]
assert chr(65 + 14) + chr(65 + 20) == 'OU' and chr(65 + 4) + chr(65 + 18) == 'ES'

fig, ax = canvas(38)
text(ax, 44, 34,'la paire ES devient OU', 'encre', 'm')
cw, chh = 9, 9
for i in range(2):
    for j in range(2):
        box(ax, 2 + j * (cw + 0.8), 10 - i * (chh + 0.8) + 9.8, cw, chh, 'sujet', label=str(M[i][j]))
text(ax, 23.5, 15, r'$\times$', 'encre', 'm')
for i in range(2):
    box(ax, 27, 10 - i * (chh + 0.8) + 9.8, 11, chh, 'varie', label=f'{"ES"[i]}={v[i]}', size='s')
text(ax, 41, 15, '=', 'encre', 'm')
for i in range(2):
    y = 10 - i * (chh + 0.8) + 9.8
    box(ax, 44, y, 12, chh, 'resultat', label=f'{"OU"[i]}={res[i]}', size='s')
calc = [r'$3\times4+3\times18=66$', r'$2\times4+5\times18=98$']
for i in range(2):
    y = 10 - i * (chh + 0.8) + 9.8 + chh / 2
    text(ax, 58, y + 2.2, calc[i], 'fixe', 's', ha='left')
    text(ax, 58, y - 2.2, f'reste {res[i]}', 'resultat', 's', ha='left')
save(fig, '53-069')
