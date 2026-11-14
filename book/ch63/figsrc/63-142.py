import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, 'image de √2 + √3 par chaque élément', 'encre', 's')
rows = [(56, '1', '√2 + √3', 'fixé', 'resultat'),
        (43, 'σ', '−√2 + √3', 'change', 'varie'),
        (30, 'τ', '√2 − √3', 'change', 'varie'),
        (17, 'στ', '−√2 − √3', 'change', 'varie')]
for y, g, img, verdict, r in rows:
    box(ax, 2, y, 14, 10, role='sujet', label=g)
    arrow(ax, (16.8, y + 5), (26.2, y + 5), r)
    box(ax, 27, y, 34, 10, role=r, label=img)
    box(ax, 66, y, 20, 10, role=r, label=verdict)
text(ax, 44, 7, 'seul 1 fixe le nombre : Gal = {1}\nℚ(√2+√3) = Inv{1} = E', 'resultat', 's', weight='bold')
save(fig, '63-142')
