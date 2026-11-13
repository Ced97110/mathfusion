import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'énoncé : multiple de 4 $\Rightarrow$ pair', 'sujet', 'm')
y = 30
f = numberline(ax, 10, 66, y, -8, 8, step=4)
brace(ax, f(-8), f(8), y + 5, 'resultat', 'l’énoncé couvre tous ces nombres', down=False)
disc(ax, f(-8), y, 2.2, 'varie')
text(ax, f(-8) + 2, y + 9.5 if False else y - 12, r'$-8 = 4 \times (-2)$', 'varie', 's')
brace(ax, f(0), f(8), y - 14, 'limite', 'preuve : $n > 0$ seulement', down=True)
save(fig, '42-097')
