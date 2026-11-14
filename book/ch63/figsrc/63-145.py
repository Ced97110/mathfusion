import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
dy = 12

def lattice(x0, top, bottom, mids, green):
    w = 9
    cxm = x0 + 20.4
    box(ax, cxm - 7, 54 + dy, 14, 9, role='sujet', label=top, size='s')
    box(ax, cxm - 7, 8 + dy, 14, 9, role='sujet', label=bottom, size='s')
    pos = [x0 + (w + 0.9) * i for i in range(3)] + [x0 + 3 * w + 1.8 + 3]
    box(ax, x0 - 1, 29.5 + dy, 30.8, 12, 'fixe', fill=False, dash=True)
    for k, x in enumerate(pos):
        role = 'resultat' if k == 3 else 'varie'
        t = green if k == 3 else mids[k]
        box(ax, x, 31 + dy, w, 9, role=role, label=t, size='s', lw=1.6 if k == 3 else 0.8)
        line(ax, [(cxm, 53.2 + dy), (x + w / 2, 40.8 + dy)], 'fixe')
        line(ax, [(x + w / 2, 30.2 + dy), (cxm, 17.8 + dy)], 'fixe')

lattice(2, '{1}', 'S₃', ['⟨τ⟩', '⟨στ⟩', '⟨σ²τ⟩'], '⟨σ⟩')
lattice(45, 'E', 'ℚ', ['ℚ(r)', 'ℚ(jr)', 'ℚ(j²r)'], 'ℚ(j)')
text(ax, 22.4, 79, 'sous-groupes de S₃', 'sujet', 's')
text(ax, 65.4, 79, 'corps intermédiaires', 'sujet', 's')
text(ax, 44, 6, '⟨σ⟩ : seul sous-groupe normal non trivial\nℚ(j) : seul corps galoisien intermédiaire', 'resultat', 's')
save(fig, '63-145')
