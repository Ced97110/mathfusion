import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
labs = [(r'$\alpha+\alpha$', 'sujet'), (r'$(1+1)\,\alpha$', 'varie'), (r'$0\cdot\alpha$', 'fixe'), ('0', 'resultat')]
ys = [56, 40, 24, 8]
for (s, r), y in zip(labs, ys):
    box(ax, 6, y, 34, 9, r, label=s)
for y in ys[:-1]:
    arrow(ax, (23, y), (23, y - 7), 'fixe')
notes = [r'départ : $2\alpha$', 'étape clé :\n' + r'$2\alpha=(2\cdot1)\alpha$', r'on remplace $1+1$ par 0', r'$2\alpha=0$ pour tout $\alpha$']
for s, y in zip(notes, ys):
    text(ax, 46, y + 4.5, s, 'encre', 's', ha='left')
save(fig, '67-034')
