import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
rows = [(36, '27', '11011', 4, 3, 5), (8, '3', '11', 1, 1, 2)]
for y, e, bits, nsq, npr, k in rows:
    assert len(bits) == k and nsq == k - 1 and npr == bits.count('1') - 1
    text(ax, 3, y + 27, f'e = {e} : k = {k} bits', 'sujet', 's', ha='left')
    for i, b in enumerate(bits):
        box(ax, 3 + i * 9, y + 8, 8, 9, 'sujet', label=b, size='m', r=0.4)
    text(ax, 52, y + 25, f'{nsq} carré' + ('s' if nsq > 1 else ''), 'varie', 's', ha='left')
    for j in range(nsq):
        box(ax, 52 + j * 8, y + 17, 6, 6, 'varie', r=0.3)
    text(ax, 52, y + 13, f'{npr} produit' + ('s' if npr > 1 else ''), 'resultat', 's', ha='left')
    for j in range(npr):
        box(ax, 52 + j * 8, y + 5, 6, 6, 'resultat', r=0.3)
text(ax, 44, 2.5, r'$k-1$ carrés, au plus $k-1$ produits', 'encre', 's')
save(fig, '53-120')
