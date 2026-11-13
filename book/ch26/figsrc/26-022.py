import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def tri(ax, ox, oy, s, p=4, q=3, hl=None, arc=None):
    """Triangle rectangle en C ; A bas-gauche, C bas-droite, B haut-droite ; cotes p (AC) et q (BC)."""
    A = (ox, oy); C = (ox + p * s, oy); B = (ox + p * s, oy + q * s)
    poly(ax, [A, C, B], "fixe")
    for pts, k in (((A, C), "b"), ((C, B), "a"), ((A, B), "c")):
        line(ax, list(pts), (hl or {}).get(k, "fixe"), lw=2.2 if k in (hl or {}) else 0.9)
    line(ax, [(C[0] - 2.2, C[1]), (C[0] - 2.2, C[1] + 2.2), (C[0], C[1] + 2.2)], "fixe", lw=0.8)
    if arc:
        t1 = math.atan2(q, p)
        line(ax, [(ox + 7 * math.cos(t1 * i / 20), oy + 7 * math.sin(t1 * i / 20)) for i in range(21)], arc, lw=1.1)
    return A, B, C
fig, ax = canvas(66)
A, B, C = tri(ax, 6, 30, 2.5, p=12, q=5, hl={"a": "varie", "c": "fixe"}, arc="sujet")
text(ax, A[0] - 2.5, A[1] - 2, "A", "sujet", "l", weight="bold")
text(ax, 21, 25, "$b$ = 12", "fixe", "s")
text(ax, C[0] + 6, C[1] + 6, "$a$ = 5", "varie", "s")
text(ax, 17, 49, "$c$ = 13", "fixe", "s")
box(ax, 46, 50, 40, 10, "sujet", label="Temps 1 : choisir A", size="s")
box(ax, 46, 36, 40, 10, "varie", label="Temps 2 : numérateur", size="s")
box(ax, 46, 22, 40, 10, "fixe", label="Temps 3 : $c$ en bas", size="s")
arrow(ax, (66, 50), (66, 46.5), "fixe"); arrow(ax, (66, 36), (66, 32.5), "fixe")
box(ax, 2, 4, 40, 10, "resultat", label="sin A = 5/13", size="m")
box(ax, 46, 4, 40, 10, "resultat", label="cos A = 12/13", size="m")
save(fig, "26-022")
