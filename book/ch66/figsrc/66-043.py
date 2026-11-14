import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [
    (48, '1 côté', None, None, r'$\Phi_1=x-1$'),
    (30, '2 côtés', r'$x^2-1$', r'$\div\ (x-1)$', r'$\Phi_2=x+1$'),
    (12, '4 côtés', r'$x^4-1$', r'$\div\ (x-1)(x+1)$', r'$\Phi_4=x^2+1$'),
]
text(ax, 20, 61, 'on divise', 'fixe', 's')
text(ax, 47, 61, 'par les précédents', 'varie', 's')
text(ax, 76, 61, 'il reste', 'sujet', 's')
for y, lab, a, b, c in rows:
    text(ax, 1.5, y + 5, lab, 'encre', 's', ha='left')
    if a: box(ax, 15, y, 20, 10, 'fixe', label=a)
    if b: box(ax, 37, y, 26, 10, 'varie', label=b)
    box(ax, 65, y, 22, 10, 'sujet', label=c)
    if a: arrow(ax, (35, y + 5), (37, y + 5), 'fixe', lw=0.6)
arrow(ax, (76, 29), (76, 23), 'sujet')
arrow(ax, (76, 47), (76, 41), 'sujet')
save(fig, '66-043')
