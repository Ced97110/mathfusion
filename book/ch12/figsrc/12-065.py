import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
rings = [('fixe', 'ℝ  réels', r'$\pi$'), ('autre', 'ℚ  rationnels', '1/2'), ('varie', 'ℤ  relatifs', '−2'), ('resultat', 'entiers', '0')]
for k, (role, name, num) in enumerate(rings):
    x = 2 + 7 * k; w = 84 - 14 * k; y = 2 + 4 * k; top = 98 - 14 * k
    box(ax, x, y, w, top - y, role, r=1.2)
    text(ax, x + 2.5, top - 5, name, role, 's', ha='left')
    text(ax, x + w - 2.5, top - 5, num, role, 'm', ha='right')
box(ax, 30, 18, 28, 24, 'sujet', r=1.2)
text(ax, 32.5, 37.5, 'ℕ  naturels', 'sujet', 's', ha='left')
text(ax, 44, 26, '1, 2, 3', 'sujet', 'm')
save(fig, '12-065')
