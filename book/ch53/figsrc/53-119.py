import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
assert 17 * 14 * 26 * 16 % 55 == 8 and 1 + 2 + 8 + 16 == 27 and 1 + 2 + 4 + 8 + 16 == 31
vals, bits = [17, 14, 31, 26, 16], '11011'
for i, (v, b) in enumerate(zip(vals, bits)):
    x = 3 + i * 17
    box(ax, x, 36, 12, 12, 'resultat' if b == '1' else 'limite', label=str(v), size='l', dash=b == '0')
    text(ax, x + 6, 30, 'bit ' + b, 'resultat' if b == '1' else 'limite', 's')
text(ax, 44, 58, 'lignes de 17 modulo 55', 'encre', 's')
text(ax, 44, 20, 'bits 1 : 1 + 2 + 8 + 16 = 27', 'resultat', 's')
text(ax, 44, 12, 'avec 31 aussi : 31, donc faux', 'limite', 's')
text(ax, 44, 4, r'$17 \times 14 \times 26 \times 16 \equiv 8$', 'resultat', 's')
save(fig, '53-119')
