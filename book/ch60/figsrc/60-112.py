import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 20, 60, 'Judson', 'autre', 'm')
text(ax, 68, 60, 'ce chapitre', 'sujet', 'm')
rows = [(r'$g^m=e$', r'$mg=0$'), (r'$\mathbb{Z}_n$', r'$\mathbb{Z}/n$'), (r'$\times$', r'$\oplus$')]
for r, (a, b) in enumerate(rows):
    y = 42 - r * 17
    box(ax, 4, y, 32, 10, 'autre', label=a, size='l')
    text(ax, 44, y + 5, '=', 'encre', 'l')
    box(ax, 52, y, 32, 10, 'sujet', label=b, size='l')
save(fig, '60-112')
