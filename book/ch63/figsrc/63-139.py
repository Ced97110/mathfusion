import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'στ change les deux signes', 'encre', 's')
rows = [(40, '√2', '−√2', 'sujet', 'varie'),
        (26, '√3', '−√3', 'sujet', 'varie'),
        (12, '√6 = √2 × √3', '(−√2)(−√3) = √6', 'sujet', 'resultat')]
for y, a, b, r1, r2 in rows:
    box(ax, 2, y, 34, 10, role=r1, label=a)
    box(ax, 52, y, 34, 10, role=r2, label=b)
    arrow(ax, (36.8, y + 5), (51.2, y + 5), r2)
    text(ax, 44, y + 8.3, 'στ', r2, 's')
text(ax, 44, 5, 'moins × moins = plus : √6 reste', 'resultat', 's')
save(fig, '63-139')
