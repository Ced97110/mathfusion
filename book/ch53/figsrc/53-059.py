import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

good = [a for a in range(1, 26) if math.gcd(a, 26) == 1]
assert good == [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] and len(good) == 12
assert len([a for a in range(1, 26) if a % 2 == 0]) == 12

fig, ax = canvas(52)
w, x0, y, h = 3.3, 2.75, 28, 8
for a in range(1, 26):
    ok = a in good
    box(ax, x0 + (a - 1) * w, y, w, h, 'resultat' if ok else 'limite', r=0.3, lw=0.5)
    if ok:
        text(ax, x0 + (a - 0.5) * w, y + h + 3, str(a), 'resultat', 's')
box(ax, 2, 3, 40, 14, 'resultat', label=r'12 restent :' + '\n' + r'$\varphi(26) = 12$', size='s')
box(ax, 46, 3, 40, 14, 'limite', label='retirés : les 12 pairs\net le nombre 13', size='s')
save(fig, '53-059')
