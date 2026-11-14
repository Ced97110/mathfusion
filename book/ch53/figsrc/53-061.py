import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def shift(word, k):
    return ''.join(chr((ord(ch) - 65 - k) % 26 + 65) for ch in word)

assert shift('DOJHEUH', 3) == 'ALGEBRE'
assert sum(1 for k in range(26) if shift('DOJHEUH', k) == 'ALGEBRE') == 1

fig, ax = canvas(72)
box(ax, 22, 56, 44, 11, 'limite', fill=False, label='message intercepté : DOJHEUH', size='s')
w, x0, y, h = 3.2, 2.4, 34, 7
for k in range(26):
    box(ax, x0 + k * w, y, w, h, 'resultat' if k == 3 else 'fixe', r=0.3, lw=0.5)
brace(ax, x0, x0 + 26 * w, y + h + 1, 'fixe', label='26 essais, un par décalage', down=False)
arrow(ax, (44, 56), (44, y + h + 8), 'fixe', lw=0.8)
text(ax, x0 + 0.5 * w, y - 3, '0', 'fixe', 's')
text(ax, x0 + 25.5 * w, y - 3, '25', 'fixe', 's')
xk = x0 + 3.5 * w
arrow(ax, (xk, y - 0.5), (xk + 10, 20), 'resultat', curve=-0.15)
box(ax, 22, 8, 50, 12, 'resultat', label='décalage 3 : ALGEBRE', size='m', weight='bold')
text(ax, 44, 2, 'chiffre affine : 312 essais', 'fixe', 's')
save(fig, '53-061')
