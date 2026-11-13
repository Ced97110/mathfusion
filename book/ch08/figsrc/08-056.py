import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
bw, g = 10, 1.5; x0 = (W - (7 * bw + 6 * g)) / 2
for i in range(7):
    box(ax, x0 + i * (bw + g), 34, bw, 12, 'resultat', label='16,3', size='s')
xe = x0 + 7 * bw + 6 * g
brace(ax, x0, xe, 49, 'sujet', label='114,1 euros', down=False, size='m')
brace(ax, x0, xe, 32, 'fixe', label='7 parts égales', down=True, size='m')
text(ax, 44, 8, r'$7\times16{,}3=114{,}1$', 'varie', 'l', weight='bold')
text(ax, 44, 16, 'vérification :', 'varie', 's')
save(fig, '08-056')
