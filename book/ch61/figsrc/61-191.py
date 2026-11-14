import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
box(ax, 4, 82, 80, 11, 'fixe', label=r'$\cos 3\theta = 4\cos^3\theta - 3\cos\theta$', size='m', weight='bold')
steps = [('sujet', 'cosinus de 30° ≈ 0,866', r'$\cos\theta$'), ('varie', 'au cube : ≈ 0,65', r'$\cos^3\theta$'),
         ('varie', 'fois 4 : ≈ 2,6', r'$4\cos^3\theta$'), ('varie', 'moins 3 × 0,866 : ≈ 2,6', r'$-\,3\cos\theta$'),
         ('resultat', 'reste 0 = cos 90°', r'$\cos 3\theta$')]
for i, (r, t, tag) in enumerate(steps):
    y = 64 - 15 * i
    box(ax, 4, y, 56, 10, r, label=t, size='s')
    text(ax, 64, y + 5, tag, r, 'm', ha='left')
    arrow(ax, (32, y + 15 if i else 81), (32, y + 10), 'fixe')
save(fig, '61-191')
