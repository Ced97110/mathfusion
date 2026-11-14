import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def edge(p, q, r=4.8):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy)
    return (p[0]+dx/d*r, p[1]+dy/d*r), (q[0]-dx/d*r, q[1]-dy/d*r)
fig, ax = canvas(78)
xs = [20, 44, 68]
rows = [(48, 'β puis α : α∘β = γ', [{1: 1, 2: 1}, {1: 2, 2: 1}]),
        (14, 'α puis β : β∘α = β', [{1: 2, 2: 1}, {1: 1, 2: 1}])]
for yc, title, steps in rows:
    ny = {1: yc + 5, 2: yc - 5}
    text(ax, 44, yc + 14, title, 'encre', 'm')
    reach = [{1, 2}]
    for mp in steps: reach.append({mp[n] for n in reach[-1]})
    for c, x in enumerate(xs):
        for n in (1, 2):
            role = 'resultat' if c == 2 else ('sujet' if c == 0 else 'fixe')
            disc(ax, x, ny[n], 4, role, fill=(n in reach[c]), label=str(n))
    for s_, mp in enumerate(steps):
        for n in reach[s_]:
            p, q = edge((xs[s_], ny[n]), (xs[s_+1], ny[mp[n]]))
            arrow(ax, p, q, 'varie' if s_ == 0 else 'sujet', lw=1.1)
cx, cy = 44, 35.5
line(ax, [(cx-3.5, cy+1.2), (cx+3.5, cy+1.2)], 'limite', lw=1.2)
line(ax, [(cx-3.5, cy-1.2), (cx+3.5, cy-1.2)], 'limite', lw=1.2)
line(ax, [(cx-2, cy-3.5), (cx+2, cy+3.5)], 'limite', lw=1.2)
save(fig, '44-048')
