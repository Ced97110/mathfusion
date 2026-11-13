import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for k, s in enumerate(['p', '(', 'a', ',', 'b', ')']):
    box(ax, 17 + 9*k, 52, 9, 9, 'fixe', label=s, size='m', r=0.3)
brace(ax, 17, 71, 62, 'fixe', label='6 signes', down=False)
arrow(ax, (44, 50), (44, 40), 'varie')
for k, s in enumerate(['a', 'b']):
    box(ax, 35 + 9*k, 29, 9, 9, 'sujet', label=s, size='m', r=0.3)
brace(ax, 35, 53, 28, 'sujet', label='2 lettres')
text(ax, 44, 12, "ab = a ∘ b : b agit d'abord", 'varie', 's')
save(fig, '44-062')
