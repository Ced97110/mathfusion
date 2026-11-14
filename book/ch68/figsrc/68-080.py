import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cw, gap, x0 = 16, 6, 3
words = ['000', '100', '110', '111']
roles = ['sujet', 'resultat', 'resultat', 'limite']
counts = ['0 erreur', '1 erreur', '2 erreurs', '3 erreurs']
for i, (w, role, c) in enumerate(zip(words, roles, counts)):
    x = x0 + i * (cw + gap)
    box(ax, x, 28, cw, 10, role, label=w)
    text(ax, x + cw / 2, 22, c, role, 's')
    if i < 3:
        arrow(ax, (x + cw + 0.5, 33), (x + cw + gap - 0.5, 33), 'varie')
brace(ax, x0 + (cw + gap), x0 + 2 * (cw + gap) + cw, 40, 'resultat', label=r'détectées : 1 à $d-1$ = 2', down=False)
text(ax, 85, 12, 'non vue : 111 est dans $C$', 'limite', 's', ha='right')
save(fig, '68-080')
