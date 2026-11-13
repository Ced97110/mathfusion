import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'$2^{72} \approx 4{,}72 \times 10^{21}$', 'sujet', 'l')
p, w, x0 = 3.7, 3.2, 4
for i in range(22):
    box(ax, x0 + i * p, 22, w, 8, 'sujet' if i == 0 else 'varie', r=0.3, lw=0.6)
text(ax, x0 + 1.6, 34, '4,72', 'sujet', 's')
brace(ax, x0 + p, x0 + 21 * p + w, 32, 'varie', '21 chiffres derrière : exposant 21', down=False, depth=1.4)
brace(ax, x0, x0 + 21 * p + w, 20, 'fixe', '22 chiffres en tout', down=True)
save(fig, '14-091')
