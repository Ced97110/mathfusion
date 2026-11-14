import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role="fixe", label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(86)
brace(ax, 3.5, 84.5, 75, 'sujet', "ch. 15 : l'expression 4$x$ − 7", down=False)
for i, t in enumerate(['$x$', '× 4', '− 7', '9']):
    x = 3.5 + i * 22
    box(ax, x, 61, 15, 11, 'sujet' if i in (0, 3) else 'fixe', t, 'm')
    if i < 3: arrow(ax, (x + 15.5, 66.5), (x + 21.5, 66.5), 'sujet')
text(ax, 44, 55, 'ch. 4 : ordre inversé', 'varie', 's')
arrow(ax, (82, 50), (6, 50), 'varie', lw=1.2)
bw = ['9', '+ 7', '16', '÷ 4', '$x$ = 4']
for i, t in enumerate(bw):
    x = 1.5 + i * 18
    role = 'varie' if t[0] in '+÷' else ('resultat' if i == 4 else 'sujet')
    box(ax, x, 31, 13, 11, role, t, 'm' if i < 4 else 's')
    if i < 4: arrow(ax, (x + 13.5, 36.5), (x + 17.5, 36.5), 'varie')
brace(ax, 19.5, 68.5, 29, 'varie', 'ch. 2-3 : opérations inverses', down=True)
text(ax, 44, 17, 'ch. 12 : égalité conservée', 'varie', 's')
save(fig, '16-146')
