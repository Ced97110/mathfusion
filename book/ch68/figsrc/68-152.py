import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
w, h = 4.8, 6
xa, xb = 2, 52
def word(x, y, bits, roles):
    for i, b in enumerate(bits):
        box(ax, x + i * w, y, w, h, roles[i], label=b, r=0.5)
text(ax, 44, 66, 'code de Hamming', 'encre', 'm', weight='bold')
text(ax, xa + 3.5 * w, 58, 'mot reçu', 'encre', 's')
text(ax, xb + 3.5 * w, 58, 'mot du code proche', 'resultat', 's')
for y, r, c in ((42, '1111111', '1111111'), (18, '1000000', '0000000')):
    d = sum(p != q for p, q in zip(r, c))
    word(xa, y, r, ['varie' if p != q else 'sujet' for p, q in zip(r, c)])
    word(xb, y, c, ['resultat'] * 7)
    arrow(ax, (xa + 7 * w + 1.5, y + 3), (xb - 1.5, y + 3), 'varie')
    text(ax, 44.5, y + 7, rf'$d = {d}$', 'varie', 'm')
text(ax, 44, 8, 'tout mot reçu : $d \\leq 1$ d’un mot du code', 'resultat', 's', weight='bold')
text(ax, 44, 2.5, 'le décodeur a toujours un mot à proposer', 'resultat', 's')
save(fig, '68-152')
