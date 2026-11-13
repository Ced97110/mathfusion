import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

word = 'ALGEBRE'
cipher = ''.join(chr((ord(c) - 65 + 3) % 26 + 65) for c in word)
assert cipher == 'DOJHEUH'
assert {cipher[i] for i in range(7) if word[i] == 'E'} == {'H'}

fig, ax = canvas(58)
text(ax, 44, 54, 'clé 3 : E donne toujours H', 'encre', 'm')
w, pitch, x0 = 10.0, 11.7, 3.2
for i, (c, d) in enumerate(zip(word, cipher)):
    x = x0 + i * pitch
    rep = c == 'E'
    box(ax, x, 34, w, 11, 'autre' if rep else 'sujet', label=c)
    box(ax, x, 6, w, 11, 'autre' if rep else 'resultat', label=d)
    arrow(ax, (x + w / 2, 34), (x + w / 2, 17.5), 'autre' if rep else 'fixe', lw=1.2 if rep else 0.8)
save(fig, '53-063')
