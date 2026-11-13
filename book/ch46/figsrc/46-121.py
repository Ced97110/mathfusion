import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 8, 72, 24, 0, 12, step=1, labels=False, arrow_right=False)
for v in range(13):
    if v % 3 == 0 and v < 12: disc(ax, f(v), 24, 1.8, 'sujet')
for v in (0, 3, 6, 9):
    text(ax, f(v), 17, str(v), 'sujet', 's')
for v in (0, 3, 6):
    arrow(ax, (f(v) + 1.5, 26), (f(v + 3) - 1.5, 26), 'varie', curve=-0.5)
    text(ax, (f(v) + f(v + 3)) / 2, 36, r'$s$', 'varie', 's')
brace(ax, f(0), f(9), 12, 'varie', label=r'$q$ = 3 pas de $s$')
text(ax, 44, 62, r'$m = qs + t$ avec $0\leq t<s$', 'encre', 'l')
text(ax, 44, 54, r'9 = 3 × 3 + 0 : $m$ = 9, $s$ = 3', 'sujet', 's')
disc(ax, f(9), 24, 1.8, 'resultat')
text(ax, 44, 46, r'$s$ minimal : $t>0$ impossible', 'limite', 's')
text(ax, 44, 3, r'donc $t$ = 0 et $H=\langle a^{s}\rangle$', 'resultat', 's')
save(fig, '46-121')
