import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
cols = [3, 47]; w = 38; h = 11
box(ax, cols[0], 84, w, 10, 'fixe', label=r'$\sqrt{2}+\sqrt{3}$')
box(ax, cols[1], 84, w, 10, 'sujet', label=r'$\sqrt{3}+\sqrt{5}$')
rows = [(r'$s^2=5+2\sqrt{6}$', r'$t^2=8+2\sqrt{15}$'), (r'$(s^2-5)^2=24$', r'$(t^2-8)^2=60$'),
        (r'$s^4-10s^2+1=0$', r'$t^4-16t^2+4=0$')]
labs = ['au carré', 'retrancher, puis au carré', 'développer']
ytop = 84
for i, (a, b) in enumerate(rows):
    y = ytop - 9 - h
    box(ax, cols[0], y, w, h, 'fixe', label=a)
    box(ax, cols[1], y, w, h, 'resultat' if i == 2 else 'sujet', label=b)
    for cx in (cols[0] + w / 2, cols[1] + w / 2): arrow(ax, (cx, ytop), (cx, y + h), 'varie')
    text(ax, 44, (ytop + y + h) / 2, labs[i], 'varie', 's')
    ytop = y
text(ax, 44, 6, 'seuls les nombres changent', 'varie', 's')
save(fig, '61-224')
