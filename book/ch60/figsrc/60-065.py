import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, 'ℤ/12 : un seul morceau', 'fixe', 'm')
for h in range(12):
    hot = h % 3 == 0
    box(ax, 3 + 6.6 * h, 62, 6, 8, 'sujet' if hot else 'fixe', label=str(h) if hot else None, size='s', r=0.4)
text(ax, 44, 54, 'tuées par une puissance de 2', 'sujet', 's')
text(ax, 44, 42, 'ℤ/4 ⊕ ℤ/3 : deux morceaux', 'fixe', 'm')
for a in range(4):
    for b in range(3):
        hot = b == 0
        box(ax, 14 + 15 * a, 10 + 8 * b, 14, 7, 'sujet' if hot else 'fixe', label=str(next(n for n in range(12) if n % 4 == a and n % 3 == b)), size='s', r=0.4)
text(ax, 44, 3.5, 'reste mod 4 ; reste mod 3', 'fixe', 's')
save(fig, '60-065')
