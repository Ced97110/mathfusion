import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, r'idéaux de $\mathbb{Z}$, chacun contient le précédent', 'sujet', 's')
labs = [r'$(1024)$', r'$(512)$', r'$(256)$', '...', r'$(2)$', r'$(1)$']
w, gap = 12, 1.8
for k, s in enumerate(labs):
    x = 3 + k * (w + gap)
    h = 8 + k * 5
    role = 'resultat' if k == len(labs) - 1 else ('fixe' if s == '...' else 'sujet')
    box(ax, x, 12, w, h, role, label=s, size='s')
arrow(ax, (6, 8), (83, 8), 'varie')
text(ax, 44, 3.5, 'la chaîne grandit puis s\'arrête', 'varie', 's')
save(fig, '56-206')
