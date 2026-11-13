import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$t=12$, $p=3$, $t/p=4$', 'sujet', 'm')
w = 6.4; x = 5
for b in range(3):
    x0 = x
    for i in range(4):
        box(ax, x, 36, w, 9, 'sujet' if b == 0 else 'fixe', r=0.6); x += w
    brace(ax, x0, x, 36, 'sujet' if b == 0 else 'fixe', label=r'$t/p=4$ pas')
    x += 2.5
text(ax, 44, 52, r'$a$ répété 12 fois = $e$', 'encre', 's')
text(ax, 44, 17, r'$a^{4}$ répété 3 fois = $a^{12}=e$', 'resultat', 's')
text(ax, 44, 9, r"donc $a^{4}$ est d'ordre 3", 'resultat', 's')
save(fig, '50-140')
