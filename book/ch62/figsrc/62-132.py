import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# Z/2Z has 2 elements, Z/7Z has 7, the field built from x^3 + x + 1 has 8 (not a prime)
rows = [(48, 'ℤ/2ℤ', 2, 'sujet', 'premier', 'resultat'), (32, 'ℤ/7ℤ', 7, 'sujet', 'premier', 'resultat'),
        (16, r'corps $K$', 8, 'autre', 'pas premier', 'limite')]
for y, lab, n, role, note, nrole in rows:
    text(ax, 3, y, lab, role, 'm', ha='left')
    for i in range(n): disc(ax, 24 + i * 5.2, y, 1.9, role)
    text(ax, 64, y, f'{n} : {note}', nrole, 's', ha='left')
text(ax, 44, 58, 'nombre d’éléments', 'encre', 'm')
save(fig, '62-132')
