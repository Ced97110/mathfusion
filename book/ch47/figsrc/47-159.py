import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def prod(a, b): return ((a[0] + (-1) ** a[1] * b[0]) % 4, (a[1] + b[1]) % 2)
def grid(x0, y0, c, els, bs):
    for i, a in enumerate(els):
        for j, b in enumerate(els):
            role = 'sujet' if prod(a, b)[1] == 0 else 'varie'
            yt = y0 + 8 * c - i * c
            poly(ax, [(x0 + j * c, yt - c), (x0 + (j + 1) * c, yt - c), (x0 + (j + 1) * c, yt), (x0 + j * c, yt)], role, lw=0.25)
    for k in range(0, 9, bs):
        line(ax, [(x0 + k * c, y0), (x0 + k * c, y0 + 8 * c)], 'encre', lw=0.9); line(ax, [(x0, y0 + k * c), (x0 + 8 * c, y0 + k * c)], 'encre', lw=0.9)
c = 3.6
grid(6, 18, c, [(k, 0) for k in range(4)] + [(k, 1) for k in range(4)], 4)
grid(50, 18, c, [(k, f) for k in range(4) for f in range(2)], 2)
text(ax, 20.4, 55, r'$N=\langle r\rangle$', 'sujet', 'm'); text(ax, 64.4, 55, r'$N=\{1,\,s\}$', 'autre', 'm')
text(ax, 20.4, 11.5, 'blocs unicolores', 'resultat', 's'); text(ax, 64.4, 11.5, 'blocs à deux couleurs', 'limite', 's')
text(ax, 20.4, 3.5, 'bleu : rotation', 'sujet', 's'); text(ax, 64.4, 3.5, 'orange : retournement', 'varie', 's')
save(fig, '47-159')
