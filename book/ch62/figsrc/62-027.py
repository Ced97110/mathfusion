import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(46, '$x^2-1$ dans ℚ', '$(x-1)(x+1)$', 'resultat'),
        (26, '$x^2-2$ dans ℚ', 'pas ce produit', 'limite'),
        (6, '$x^2-2$ dans ℝ', '$(x-\\sqrt{2})(x+\\sqrt{2})$', 'resultat')]
for y, l, r, role in rows:
    box(ax, 2, y, 34, 12, 'sujet', label=l, size='s')
    arrow(ax, (37.5, y + 6), (43.5, y + 6), 'varie')
    box(ax, 45, y, 41, 12, role, label=r, size='s')
text(ax, 44, 61, 'produit de facteurs de degré 1 ?', 'encre', 'm')
save(fig, '62-027')
