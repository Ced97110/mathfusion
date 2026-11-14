import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from figstyle import *
from bitkit import bitrow, cells, cell
# Aides du lot L07 (chapitre 68) : rangées de bits avec cases, alignées à gauche ou centrées.
BL = ' '  # chiffre vide (case sans digit)
_P = {}

def pitch(size='l', k=5):
    key = (size, k)
    if key not in _P:
        f, a = canvas(20); _, p = bitrow(f, a, 44, 10, '00', size=size, k=k); plt.close(f); _P[key] = p
    return _P[key]

def brow(fig, ax, xc, y, s, role=None, roles=None, size='l', k=5, h=6.0, ink='encre', weight='normal'):
    """Rangée de bits centrée en xc, avec une case par bit. roles : un rôle par bit (None = pas de case)."""
    xs, p = bitrow(fig, ax, xc, y, s, ink, size, k, weight)
    rs = roles if roles else [role] * len(s)
    cells(ax, xs, p, y, h, rs)
    return xs, p

def lrow(fig, ax, x0, y, s, **kw):
    """Comme brow, mais le bord gauche de la première case est en x0."""
    p = pitch(kw.get('size', 'l'), kw.get('k', 5))
    return brow(fig, ax, x0 + p * len(s) / 2, y, s, **kw)
