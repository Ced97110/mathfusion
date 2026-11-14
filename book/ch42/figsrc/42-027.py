import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for x, sym, r, d in [(16, r'$a$', 'varie', 'la gourde'), (44, r'$\in$', 'sujet', 'appartient à'), (72, r'$S$', 'fixe', 'le sac')]:
    text(ax, x, 56, sym, r, 22); text(ax, x, 44, d, r, 's')
box(ax, 18, 6, 52, 28, 'fixe')
text(ax, 23, 29, r'$S$', 'fixe', 's', ha='left')
disc(ax, 37, 17, 5, 'varie', label=r'$a$'); disc(ax, 53, 17, 5, 'fixe', label=r'$b$')
save(fig, '42-027')
