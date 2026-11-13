import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
names = ['ℂ  complexes', 'ℝ  réels', 'ℚ  fractions', 'ℤ  entiers']
for k, n in enumerate(names):
    x, y, w, h = 2 + 7 * k, 10 + 6 * k, 84 - 14 * k, 62 - 12 * k
    box(ax, x, y, w, h, 'sujet', fill=(k == 3))
    text(ax, x + 3, y + h - 3.5, n, 'sujet', 's', ha='left')
text(ax, 44, 30, r'$3 = \frac{3}{1}$', 'sujet', 'm')
text(ax, 44, 5, 'ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ', 'sujet', 'l')
save(fig, '51-085')
