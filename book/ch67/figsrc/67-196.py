import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
X = lambda v: 8 + v * 1.1
bh = 7
def bar(a, b, y, role):
    poly(ax, [(X(a), y - bh / 2), (X(b), y - bh / 2), (X(b), y + bh / 2), (X(a), y + bh / 2)], role)
text(ax, 44, 84, r'$n=6$ : diviseurs 1, 2, 3, 6', 'encre', 'm')
bar(0, 64, 72, 'sujet')
text(ax, X(32), 72, r'$d=1$ : $+2^{6}=+64$', 'sujet', 'm')
bar(56, 64, 60, 'varie')
text(ax, X(56) - 1.5, 60, r'$d=2$ : $-2^{3}=-8$', 'varie', 'm', ha='right')
bar(52, 56, 48, 'varie')
text(ax, X(52) - 1.5, 48, r'$d=3$ : $-2^{2}=-4$', 'varie', 'm', ha='right')
bar(52, 54, 36, 'sujet')
text(ax, X(52) - 1.5, 36, r'$d=6$ : $+2^{1}=+2$', 'sujet', 'm', ha='right')
for v, y0, y1 in [(64, 72, 60), (56, 60, 48), (52, 48, 36)]:
    line(ax, [(X(v), y0 - bh / 2), (X(v), y1 + bh / 2)], 'fixe', lw=0.6, dash=True)
bar(0, 54, 22, 'resultat')
for i in range(1, 9):
    line(ax, [(X(6 * i), 22 - bh / 2), (X(6 * i), 22 + bh / 2)], 'resultat', lw=0.6)
text(ax, X(54) + 1.5, 22, '54', 'resultat', 'm', ha='left')
text(ax, 44, 9, '54 ÷ 6 = 9 polynômes', 'resultat', 'm')
save(fig, '67-196')
