import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(94)
text(ax, 44, 90, r'avec $a = 1$ et $b = 3$', 'varie', 'm')
text(ax, 44, 82, r'$-3a + 2b - 5a + a + 6b$', 'sujet', 'm')
for i, v in enumerate(['−3', '6', '−5', '1', '18']):
    box(ax, 3 + i * 17, 66, 14, 7, 'varie', label=v)
brace(ax, 3, 85, 65.4, 'resultat', r'somme $= 17$')
text(ax, 44, 55, '=', 'resultat', 'l')
text(ax, 44, 47, r'$-7a + 8b$', 'sujet', 'm')
for i, v in enumerate(['−7', '24']):
    box(ax, 18.5 + i * 27, 32, 24, 7, 'varie', label=v)
brace(ax, 18.5, 69.5, 31.4, 'resultat', r'somme $= 17$')
save(fig, '15-052')
