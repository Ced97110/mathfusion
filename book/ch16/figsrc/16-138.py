import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role="fixe", label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(100)
fr = [("$x$ est l'ancien prix", 'sujet'), ('$x$ + 3 = 44', 'varie'), ('$x$ = 44 − 3 = 41', 'varie'),
      ('41 + 3 = 44 : vrai', 'varie'), ("L'ancien prix est 41 €", 'sujet')]
ys = [86 - i * 19 for i in range(5)]
for (t, r), y in zip(fr, ys):
    box(ax, 26, y, 60, 12, r, t, 'm')
for i in range(4):
    arrow(ax, (56, ys[i] - 0.5), (56, ys[i + 1] + 12.5), 'fixe')
text(ax, 12, ys[0] + 6, 'mots', 'sujet', 's'); text(ax, 12, ys[4] + 6, 'mots', 'sujet', 's')
text(ax, 11, (ys[1] + ys[3] + 12) / 2, 'signes', 'varie', 's')
line(ax, [(21, ys[1] + 12), (21, ys[3])], 'varie', lw=1.2)
save(fig, '16-138')
