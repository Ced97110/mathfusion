import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for i in range(6):
    box(ax, 8 + 12 * i, 42, 12, 12, 'sujet'); box(ax, 8 + 12 * i, 22, 12, 12, 'autre')
text(ax, 8, 59, r'ℚ$(w)$ : degré 6', 'sujet', 's', ha='left')
text(ax, 8, 16, r'ℚ$(\sqrt[3]{5},\sqrt{5}\,i)$ : degré 6', 'autre', 's', ha='left')
text(ax, 44, 38, '=', 'resultat', 'xl')
text(ax, 44, 7, '6 ÷ 6 = 1 : même corps', 'resultat', 's')
save(fig, '61-230')
