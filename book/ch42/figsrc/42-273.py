import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(96)
steps = [(r'1. $f$ : application ?', 'resultat', 'oui : une image\npar départ'),
         (r'2. $f$ injective ?', 'limite', 'non : 1 et 2\nvont sur a'),
         (r'3. $f$ surjective ?', 'resultat', 'oui : a et b\nsont atteints'),
         (r'4. mêmes tests pour $g$', 'fixe', 'injective ; y\nn\u2019est pas atteint'),
         (r'5. calculer $g\circ f$', 'resultat', r'$1\to z$, $2\to z$, $3\to x$')]
n = len(steps); bh = 11; gap = 7; top = 96 - 2
for i, (lab, role, res) in enumerate(steps):
    y = top - bh - i * (bh + gap)
    box(ax, 2, y, 44, bh, 'sujet', label=lab, size='m')
    box(ax, 52, y, 34, bh, role, label=res, size='s')
    arrow(ax, (46, y + bh / 2), (52, y + bh / 2), 'varie')
    if i < n - 1:
        arrow(ax, (24, y), (24, y - gap), 'varie')
save(fig, '42-273')
