import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'être dans le même bloc', 'fixe', 's')
rows = [(48, r'$a\ E\ a$', 1), (28, r'$a\ E\ b \Rightarrow b\ E\ a$', 2), (9, r'$a\ E\ b,\ b\ E\ c \Rightarrow a\ E\ c$', 3)]
for y, form, n in rows:
    box(ax, 50, y - 8, 36, 17, 'sujet', fill=True, r=2)
    text(ax, 3, y, form, 'sujet', 's', ha='left') if n < 3 else text(ax, 3, y, form, 'sujet', 's', ha='left')
    xs = [68] if n == 1 else [58, 78] if n == 2 else [56, 68, 80]
    for x, nm in zip(xs, 'abc'): disc(ax, x, y, 3.2, 'autre', label=nm, size='s')
    if n == 2: arrow(ax, (61.5, y+1), (74.5, y+1), 'varie'); arrow(ax, (74.5, y-1), (61.5, y-1), 'varie')
    if n == 3:
        arrow(ax, (59.5, y), (64.5, y), 'varie'); arrow(ax, (71.5, y), (76.5, y), 'varie')
        arrow(ax, (56, y+3.5), (80, y+3.5), 'resultat', curve=-0.5)
save(fig, '43-027')
