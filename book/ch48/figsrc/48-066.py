import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
steps = [(84, 'sujet', r"$h\in f^{-1}(H'),\ g\in G$", 'départ'),
         (65, 'fixe', r"$f(g^{-1}hg)=f(g)^{-1}f(h)f(g)$", 'f morphisme'),
         (46, 'fixe', r"$f(h)\in H'$", 'h dans l\'image'),
         (27, 'varie', r"$f(g)^{-1}f(h)f(g)\in H'$", 'H′ est normal'),
         (8, 'resultat', r"$g^{-1}hg\in f^{-1}(H')$", 'arrivée')]
for k, (y, r, s, tag) in enumerate(steps):
    box(ax, 2, y, 58, 12, r, label=s, size='s', weight='bold' if k == 3 else 'normal')
    text(ax, 74, y + 6, tag, r, 's', weight='bold' if k == 3 else 'normal')
    if k < 4: arrow(ax, (31, y), (31, y - 7), 'fixe')
save(fig, '48-066')
