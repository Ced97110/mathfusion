import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 20, 70, 'exemples', 'fixe', 's')
text(ax, 69, 70, 'règle annoncée', 'autre', 's')
for y, lab in [(50, r'ℚ$(\sqrt{2},\sqrt{3})=$ℚ$(s)$'), (34, r'ℚ$(\sqrt{3},\sqrt{5})=$ℚ$(t)$'), (18, r'ℚ$(\sqrt[3]{5},\sqrt{5}\,i)=$ℚ$(w)$')]:
    box(ax, 3, y, 34, 12, 'fixe', label=lab, size='s')
    arrow(ax, (37, y + 6), (52, 42), 'varie')
box(ax, 52, 24, 34, 36, 'autre', dash=True)
for y, t in [(48, 'toute extension'), (42, 'finie est simple'), (36, '(caractéristique 0)')]:
    text(ax, 69, y, t, 'autre', 's')
text(ax, 69, 14, 'démontrée au chapitre 63', 'autre', 's')
save(fig, '61-231')
