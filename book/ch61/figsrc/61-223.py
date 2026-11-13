import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def chain(ax, items, acts, x, w, h, gap, top, axx):
    n = len(items)
    for i, (lab, role) in enumerate(items):
        y = top - h - i * (h + gap)
        box(ax, x, y, w, h, role, label=lab)
        if i < n - 1:
            arrow(ax, (axx, y), (axx, y - gap), "varie")
            text(ax, axx + 3, y - gap / 2, acts[i], "varie", "s", ha="left")

fig, ax = canvas(100)
items = [(r'$s=\sqrt{2}+\sqrt{3}\approx 3{,}15$', 'sujet'), (r'$s^2=5+2\sqrt{6}\approx 9{,}9$', 'sujet'),
         (r'$s^2-5\approx 4{,}9$', 'sujet'), (r'$(s^2-5)^2=24$', 'sujet'), (r'$s^4-10s^2+1=0$', 'resultat')]
chain(ax, items, ['au carré', 'retrancher 5', 'au carré', 'développer'], 14, 60, 11, 8, 98, 44)
save(fig, '61-223')
