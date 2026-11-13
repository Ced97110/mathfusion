import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
X, XP = r'$x_i$', r"$x_i^{\prime}$"
def row(y, seq, x0):
    for k, (lab, r) in enumerate(seq):
        box(ax, x0 + k * 12.5, y, 11, 10, r, label=lab, size='s')
row(54, [(X, 'varie'), (XP, 'varie'), (X, 'sujet'), (XP, 'sujet'), (X, 'sujet')], 20)
# first pair and the later pair are the erased ones
row(32, [(X, 'sujet'), (XP, 'varie'), (X, 'varie')], 20)
row(10, [(X, 'resultat')], 20)
text(ax, 2, 59, '5 lettres', 'encre', 's', ha='left')
text(ax, 2, 37, '3 lettres', 'encre', 's', ha='left')
text(ax, 2, 15, '1 lettre', 'encre', 's', ha='left')
arrow(ax, (32, 53), (32, 43), 'varie'); text(ax, 36, 48, r'$x_ix_i^{\prime}=1$', 'varie', 's', ha='left')
arrow(ax, (32, 31), (32, 21), 'varie'); text(ax, 36, 26, r"$x_i^{\prime}x_i=1$", 'varie', 's', ha='left')
save(fig, '49-043')
