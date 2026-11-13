import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def edge(a, b, r, role):
    dx, dy = b[0] - a[0], b[1] - a[1]; k = r / math.hypot(dx, dy)
    line(ax, [(a[0] + dx * k, a[1] + dy * k), (b[0] - dx * k, b[1] - dy * k)], role)
text(ax, 22, 74, 'chaîne : diviseurs de 8', 'sujet', 's')
ch = [(22, 14 + 16 * i) for i in range(4)]
for a, b in zip(ch, ch[1:]): edge(a, b, 4, 'sujet')
for p, n in zip(ch, ['1', '2', '4', '8']): disc(ax, p[0], p[1], 4, 'sujet', label=n)
text(ax, 22, 5, 'toute paire se compare', 'resultat', 's')
text(ax, 66, 74, 'diviseurs de 60 (extrait)', 'autre', 's')
n4, n12, n20, n60 = (66, 14), (54, 38), (78, 38), (66, 62)
for a, b in [(n4, n12), (n4, n20), (n12, n60), (n20, n60)]: edge(a, b, 4, 'autre')
line(ax, [(58.5, 38), (73.5, 38)], 'limite', dash=True)
text(ax, 66, 33.5, 'incomparables', 'limite', 's')
for p, n in [(n4, '4'), (n12, '12'), (n20, '20'), (n60, '60')]: disc(ax, p[0], p[1], 4, 'autre', label=n)
save(fig, '79-022')
