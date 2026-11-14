import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, r'cas de la figure : degré $n=3$', 'sujet', 's')
text(ax, 44, 64, 'trois racines, trois facteurs de degré 1', 'sujet', 's')
w = 17
for i in range(3):
    box(ax, 4 + i * (w + 1), 46, w, 10, 'sujet', label=rf'$x-a_{i+1}$')
text(ax, 62, 51, r'$\times$', 'encre', 'm')
box(ax, 66, 46, 18, 10, 'fixe', label=r'$k=1/4$')
text(ax, 75, 41, 'degré 0', 'fixe', 's')
text(ax, 44, 33, r'$r = n = 3$ : le maximum', 'resultat', 's')
text(ax, 44, 25, 'autre cas : deux racines seulement', 'varie', 's')
for i in range(2):
    box(ax, 4 + i * (w + 1), 8, w, 10, 'sujet', label=rf'$x-a_{i+1}$')
text(ax, 42, 13, r'$\times$', 'encre', 'm')
box(ax, 46, 8, 30, 10, 'varie', label=r'$k$ de degré 1')
save(fig, '54-240')
