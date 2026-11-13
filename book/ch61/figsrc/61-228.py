import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'ℚ$(\sqrt[3]{5},\sqrt{5}\,i)$', 'encre', 'm')
for r in range(2):
    for c in range(3):
        box(ax, 14 + 16 * c, 24 + 14 * r, 16, 14, 'sujet' if r == 0 else 'varie')
brace(ax, 14, 62, 52, 'sujet', r'ℚ$(\sqrt[3]{5})$ : degré 3', down=False)
text(ax, 65, 38, 'degré 2', 'varie', 's', ha='left')
text(ax, 44, 14, 'degré total : 3 × 2 = 6', 'resultat', 's')
text(ax, 44, 6, r'$x^3-5$ : Eisenstein, $p=5$', 'sujet', 's')
save(fig, '61-228')
