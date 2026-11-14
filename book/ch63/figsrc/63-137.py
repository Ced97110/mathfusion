import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, 'élément de E : a + b√2 + c√3 + d√6', 'encre', 's')
xs = [3, 24, 46, 67]
top = ['a', 'b√2', 'c√3', 'd√6']
bot = ['a', '−b√2', 'c√3', '−d√6']
rb = ['fixe', 'varie', 'fixe', 'varie']
for x, t, b, r in zip(xs, top, bot, rb):
    box(ax, x, 38, 18, 10, role='sujet', label=t)
    arrow(ax, (x + 9, 37.2), (x + 9, 25.8), r)
    box(ax, x, 15, 18, 10, role=r, label=b)
text(ax, 17.5, 31.5, 'σ', 'varie', 'm')
text(ax, 44, 7, 'fixe ⇔ b = d = 0 : Inv⟨σ⟩ = ℚ(√3)', 'resultat', 'm', weight='bold')
save(fig, '63-137')
