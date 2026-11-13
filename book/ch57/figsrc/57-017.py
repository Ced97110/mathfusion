import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 35, 54, 'addition', 'varie', 's')
text(ax, 70, 54, 'multiplication', 'varie', 's')
rows = [(38, 'réels', '2 + 3 = 5', '2 × 3 = 6'), (23, 'entiers', '2 + 3 = 5', '2 × 3 = 6'),
        (8, 'en T', '(T + 1) + 2T = 3T + 1', '(T + 1) × 2T = 2T² + 2T')]
for y, a, b, c in rows:
    box(ax, 2, y, 14, 11, 'sujet', label=a, size='s')
    box(ax, 18, y, 34, 11, 'resultat', label=b, size='s')
    box(ax, 54, y, 32, 11, 'resultat', label=c, size='s')
save(fig, '57-017')
