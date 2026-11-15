// Copyright: Your Name. Apache 2.0
// Geometry of the procedural Cessna 172S (« Vent de travers », v2), in true metres.
// MODEL FRAME used in this file: x = right wing, y = up, z = toward the tail (nose along -z).
// avion.js turns the model so that the nose points along local +x (right wing +z).

const B = globalThis.BABYLON;
const rad = (d) => (d * Math.PI) / 180;
const lerp = (a, b, k) => a + (b - a) * k;

/* ------------------------------------------------------------------ interpolation and profiles */

/** Monotone cubic (PCHIP) interpolation through (xs, ys). */
export function pchip(xs, ys) {
  const n = xs.length;
  const h = [], dl = [], m = new Array(n).fill(0);
  for (let i = 0; i < n - 1; i++) { h[i] = xs[i + 1] - xs[i]; dl[i] = (ys[i + 1] - ys[i]) / h[i]; }
  m[0] = dl[0]; m[n - 1] = dl[n - 2];
  for (let i = 1; i < n - 1; i++) {
    if (dl[i - 1] * dl[i] <= 0) m[i] = 0;
    else { const w1 = 2 * h[i] + h[i - 1], w2 = h[i] + 2 * h[i - 1]; m[i] = (w1 + w2) / (w1 / dl[i - 1] + w2 / dl[i]); }
  }
  return (x) => {
    if (x <= xs[0]) return ys[0];
    if (x >= xs[n - 1]) return ys[n - 1];
    let i = 0; while (x > xs[i + 1]) i++;
    const u = (x - xs[i]) / h[i], u2 = u * u, u3 = u2 * u;
    return (2 * u3 - 3 * u2 + 1) * ys[i] + (u3 - 2 * u2 + u) * h[i] * m[i] + (-2 * u3 + 3 * u2) * ys[i + 1] + (u3 - u2) * h[i] * m[i + 1];
  };
}

/** NACA 4-digit half thickness (closed trailing edge), in chords. */
export const epaisseur = (c, ep) => 5 * ep * (0.2969 * Math.sqrt(Math.max(c, 0)) - 0.126 * c - 0.3516 * c * c + 0.2843 * c ** 3 - 0.1015 * c ** 4);
/** NACA 4-digit camber line, in chords. */
export const cambrure = (c, m, p) => (m === 0 ? 0 : c < p ? (m / p ** 2) * (2 * p * c - c * c) : (m / (1 - p) ** 2) * (1 - 2 * p + 2 * p * c - c * c));

/**
 * Closed section loop as points {c, y, v} (c chord fraction, y offset in chords, v texture row):
 * trailing edge → upper surface → leading edge → lower surface.
 *  'complet' : the whole profile;
 *  'avant'   : c in [0, coupe], closed by a flat rear face (wing box in front of a flap);
 *  'arriere' : c in [coupe, 1] with a round nose (flap, aileron, elevator). Also returns the hinge {c, y}.
 */
export function boucle(type, { n = 28, m = 0.02, p = 0.4, ep = 0.12, coupe = 0.72 } = {}) {
  const pt = (c, haut) => ({ c, y: cambrure(c, m, p) + (haut ? 1 : -1) * epaisseur(c, ep), v: haut ? 0.5 - 0.5 * c : 0.5 + 0.5 * c });
  const pts = [];
  if (type === 'complet') {
    for (let k = 0; k <= n; k++) pts.push(pt(0.5 * (1 + Math.cos((Math.PI * k) / n)), true));
    for (let k = 1; k < n; k++) pts.push(pt(0.5 * (1 - Math.cos((Math.PI * k) / n)), false));
    return { pts };
  }
  if (type === 'avant') {
    for (let k = 0; k <= n; k++) pts.push(pt(coupe * (1 - Math.cos((Math.PI / 2) * (1 - k / n))), true));
    for (let k = 1; k <= n; k++) pts.push(pt(coupe * (1 - Math.cos((Math.PI / 2) * (k / n))), false));
    pts.push({ ...pts[pts.length - 1] }, { ...pts[0] }); // duplicated corners: sharp rear face
    return { pts };
  }
  // 'arriere': nose circle of radius r centred at cc, tangent to the local thickness
  let r = epaisseur(coupe, ep);
  for (let i = 0; i < 4; i++) r = epaisseur(coupe + r, ep);
  const cc = coupe + r, yc = cambrure(cc, m, p);
  const na = Math.max(8, Math.round(n / 2));
  for (let k = 0; k <= n; k++) pts.push(pt(1 - (1 - cc) * (k / n), true));
  for (let k = 1; k < na; k++) {
    const a = Math.PI / 2 + (Math.PI * k) / na;
    pts.push({ c: cc + r * Math.cos(a), y: yc + r * Math.sin(a), v: 0.5 });
  }
  for (let k = 0; k < n; k++) pts.push(pt(cc + (1 - cc) * (k / n), false));
  return { pts, charniere: { c: cc, y: yc } };
}

/* ------------------------------------------------------------------ fuselage surface */

// stations: z, half-width, half-height, centre height, superellipse exponent
const ST = [
  [-2.93, 0.3, 0.26, -0.1, 2.2], [-2.8, 0.44, 0.36, -0.1, 2.4], [-2.5, 0.52, 0.45, -0.07, 2.6],
  [-2.0, 0.55, 0.52, -0.03, 2.8], [-1.7, 0.57, 0.58, 0.0, 3.0], [-1.05, 0.58, 0.7, 0.08, 3.2],
  [0.55, 0.58, 0.7, 0.08, 3.2], [1.2, 0.52, 0.6, 0.12, 3.0], [2.0, 0.42, 0.48, 0.18, 2.8],
  [3.0, 0.3, 0.36, 0.25, 2.5], [4.0, 0.18, 0.24, 0.33, 2.3], [4.7, 0.08, 0.15, 0.38, 2.2], [4.82, 0.025, 0.06, 0.4, 2.0],
];
const zs = ST.map((s) => s[0]);
export const fA = pchip(zs, ST.map((s) => s[1]));
export const fB = pchip(zs, ST.map((s) => s[2]));
export const fC = pchip(zs, ST.map((s) => s[3]));
const fN = pchip(zs, ST.map((s) => s[4]));

/** Fuselage extent along z (texture u = 0 → 1). */
export const FUS = Object.freeze({ z0: -2.935, z1: 4.83 });

/** Point [x, y, z] on the skin at station z and angle th (0 = right side, π/2 = top), pushed out by off. */
export function peau(z, th, off = 0) {
  const a = fA(z) + off, b = fB(z) + off, n = fN(z);
  const c = Math.cos(th), s = Math.sin(th);
  return [a * Math.sign(c) * Math.abs(c) ** (2 / n), fC(z) + b * Math.sign(s) * Math.abs(s) ** (2 / n), z];
}
/** Angle on the skin for height y at station z, right (+1) or left (-1) side; in [-π/2, 3π/2). */
export function angleY(z, y, cote) {
  const n = fN(z), r = Math.max(-0.999, Math.min(0.999, (y - fC(z)) / fB(z)));
  const th = Math.asin(Math.sign(r) * Math.abs(r) ** (n / 2));
  return cote > 0 ? th : Math.PI - th;
}

/* ------------------------------------------------------------------ mesh builder */

/**
 * Builds a smooth mesh from rows of points (each row one section, same length).
 * Normals are smooth; seam and collapsed rows (poles) are averaged; winding is fixed so that
 * normals point away from the row centre (or toward it when inverser).
 * @param {any} scene
 * @param {string} nom
 * @param {number[][][]} rangs rows of [x, y, z]
 * @param {{fermer?:boolean, uv?:(i:number,j:number,p:number[])=>number[], centre?:(i:number)=>number[], inverser?:boolean}} o
 */
export function maillage(scene, nom, rangs, o = {}) {
  const n = rangs.length, m = rangs[0].length, mc = o.fermer ? m + 1 : m;
  const pos = [], uvs = [], idx = [];
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < mc; j++) {
      const p = rangs[i][j % m];
      pos.push(p[0], p[1], p[2]);
      const uv = o.uv ? o.uv(i, j, p) : [j / (mc - 1), i / (n - 1)];
      uvs.push(uv[0], uv[1]);
    }
  }
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < mc - 1; j++) {
      const a = i * mc + j, b = a + 1, c = a + mc, d = c + 1;
      idx.push(a, c, b, b, c, d);
    }
  }
  let nor = [];
  B.VertexData.ComputeNormals(pos, idx, nor);
  let s = 0;
  for (let i = 0; i < n; i++) {
    let ce = o.centre ? o.centre(i) : null;
    if (!ce) {
      ce = [0, 0, 0];
      for (const p of rangs[i]) { ce[0] += p[0] / m; ce[1] += p[1] / m; ce[2] += p[2] / m; }
    }
    for (let j = 0; j < mc; j++) {
      const k = 3 * (i * mc + j);
      s += nor[k] * (pos[k] - ce[0]) + nor[k + 1] * (pos[k + 1] - ce[1]) + nor[k + 2] * (pos[k + 2] - ce[2]);
    }
  }
  if ((s < 0) !== Boolean(o.inverser)) {
    for (let k = 0; k < idx.length; k += 3) { const t = idx[k + 1]; idx[k + 1] = idx[k + 2]; idx[k + 2] = t; }
    nor = [];
    B.VertexData.ComputeNormals(pos, idx, nor);
  }
  const moyenne = (liste) => {
    let x = 0, y = 0, z = 0;
    for (const v of liste) { x += nor[3 * v]; y += nor[3 * v + 1]; z += nor[3 * v + 2]; }
    const l = Math.hypot(x, y, z) || 1;
    for (const v of liste) { nor[3 * v] = x / l; nor[3 * v + 1] = y / l; nor[3 * v + 2] = z / l; }
  };
  for (let i = 0; i < n; i++) {
    if (o.fermer) moyenne([i * mc, i * mc + m]);
    const r = rangs[i];
    let etendue = 0;
    for (const p of r) etendue = Math.max(etendue, Math.abs(p[0] - r[0][0]) + Math.abs(p[1] - r[0][1]) + Math.abs(p[2] - r[0][2]));
    if (etendue < 1e-7) moyenne(Array.from({ length: mc }, (_, j) => i * mc + j));
  }
  const vd = new B.VertexData();
  vd.positions = pos; vd.indices = idx; vd.normals = nor; vd.uvs = uvs;
  const mesh = new B.Mesh(nom, scene);
  vd.applyToMesh(mesh);
  mesh.isPickable = false;
  return mesh;
}

/** Appends a duplicated last row and a collapsed centroid row: a flat cap with a sharp edge. */
export function fermerBout(rangs, debut = false) {
  const r = debut ? rangs[0] : rangs[rangs.length - 1];
  const c = [0, 0, 0];
  for (const p of r) { c[0] += p[0] / r.length; c[1] += p[1] / r.length; c[2] += p[2] / r.length; }
  const cap = [r.map((p) => [...p]), r.map(() => [...c])];
  return debut ? [...cap.reverse(), ...rangs] : [...rangs, ...cap];
}

/* ------------------------------------------------------------------ rounded polygons (windows, doors) */

/** Rounds every corner of a convex polygon [[a, b], ...] with radius r (n points per arc). */
export function arrondir(poly, r, n = 8) {
  const out = [];
  const L = poly.length;
  for (let k = 0; k < L; k++) {
    const P = poly[k], A = poly[(k + L - 1) % L], C = poly[(k + 1) % L];
    const u1 = [A[0] - P[0], A[1] - P[1]], u2 = [C[0] - P[0], C[1] - P[1]];
    const l1 = Math.hypot(...u1), l2 = Math.hypot(...u2);
    u1[0] /= l1; u1[1] /= l1; u2[0] /= l2; u2[1] /= l2;
    const demi = Math.acos(Math.max(-1, Math.min(1, u1[0] * u2[0] + u1[1] * u2[1]))) / 2;
    const rr = Math.min(r, 0.45 * Math.min(l1, l2) * Math.tan(demi));
    const d = rr / Math.tan(demi);
    const bis = [u1[0] + u2[0], u1[1] + u2[1]], lb = Math.hypot(...bis);
    const ce = [P[0] + (bis[0] / lb) * (rr / Math.sin(demi)), P[1] + (bis[1] / lb) * (rr / Math.sin(demi))];
    const p1 = [P[0] + u1[0] * d, P[1] + u1[1] * d], p2 = [P[0] + u2[0] * d, P[1] + u2[1] * d];
    let a1 = Math.atan2(p1[1] - ce[1], p1[0] - ce[0]), a2 = Math.atan2(p2[1] - ce[1], p2[0] - ce[0]);
    let da = a2 - a1;
    while (da > Math.PI) da -= 2 * Math.PI;
    while (da < -Math.PI) da += 2 * Math.PI;
    for (let i = 0; i <= n; i++) { const a = a1 + (da * i) / n; out.push([ce[0] + rr * Math.cos(a), ce[1] + rr * Math.sin(a)]); }
  }
  return out;
}

/** Densifies a closed polyline so that no segment is longer than pas. */
export function densifier(poly, pas) {
  const out = [];
  for (let k = 0; k < poly.length; k++) {
    const a = poly[k], b = poly[(k + 1) % poly.length];
    const nn = Math.max(1, Math.ceil(Math.hypot(b[0] - a[0], b[1] - a[1]) / pas));
    for (let i = 0; i < nn; i++) out.push([lerp(a[0], b[0], i / nn), lerp(a[1], b[1], i / nn)]);
  }
  return out;
}

const R_TOIT = 0.62; // metres per radian on the cabin roof, to round corners in (z, angle) space

/**
 * Cabin openings as closed polylines in (z, th) skin coordinates.
 * kind: 'vitre' (glass) or 'porte' (door and panel outlines, drawn as grooves only).
 */
export function ouvertures() {
  const res = [];
  const cote = (poly, s, kind, r) => {
    const p = densifier(arrondir(poly, r, 8), 0.02);
    return { kind, pts: p.map(([z, y]) => [z, angleY(z, y, s)]) };
  };
  const toit = (poly, kind, r) => {
    const p = densifier(arrondir(poly.map(([z, th]) => [z, th * R_TOIT]), r, 8), 0.02);
    return { kind, pts: p.map(([z, a]) => [z, a / R_TOIT]) };
  };
  for (const s of [1, -1]) {
    res.push(cote([[-0.98, 0.2], [-0.24, 0.2], [-0.24, 0.7], [-0.98, 0.7]], s, 'vitre', 0.08)); // door window
    res.push(cote([[-0.12, 0.2], [0.55, 0.2], [0.55, 0.7], [-0.12, 0.7]], s, 'vitre', 0.07)); // rear side window
    res.push(cote([[0.68, 0.22], [1.45, 0.24], [1.45, 0.46], [0.68, 0.66]], s, 'vitre', 0.06)); // quarter window
    res.push(cote([[-1.04, -0.42], [-0.17, -0.42], [-0.17, 0.75], [-1.04, 0.75]], s, 'porte', 0.09)); // door
  }
  res.push(cote([[0.85, -0.36], [1.35, -0.34], [1.35, 0.1], [0.85, 0.1]], -1, 'porte', 0.05)); // baggage door, left
  // windscreen: A-pillars lean back, from low at the cowling to the wing root
  res.push(toit([[-1.72, rad(26)], [-1.08, rad(44)], [-1.08, rad(136)], [-1.72, rad(154)]], 'vitre', 0.07));
  // rear window, narrowing aft
  res.push(toit([[0.64, rad(56)], [1.55, rad(70)], [1.55, rad(110)], [0.64, rad(124)]], 'vitre', 0.06));
  return res;
}

/* ------------------------------------------------------------------ wing, tailplane, fin */

export const AILE = Object.freeze({ y: 0.8, diedre: Math.tan(rad(1.73)), rond: 5.3, bout: 5.55, bf: 0.58 });
export const bordAttaqueAile = pchip([0, 2.6, 5.45], [-1.05, -1.05, -0.55]);
const kRond = (x, x0, x1) => (x <= x0 ? 1 : Math.sqrt(Math.max(0, 1 - ((x - x0) / (x1 - x0)) ** 2)));

/** Right-wing section at span x for a loop (points {c, y}); tip rounded beyond AILE.rond. */
export function sectionAile(x, pts, off = 0) {
  const ch0 = AILE.bf - bordAttaqueAile(x), k = kRond(x, AILE.rond, AILE.bout);
  const ch = ch0 * k, le = bordAttaqueAile(x) + (1 - k) * 0.45 * ch0, y0 = AILE.y + x * AILE.diedre;
  return pts.map((p) => [x, y0 + p.y * ch + Math.sign(p.v - 0.5 || -1) * -off, le + p.c * ch]);
}
/** Span stations of the rounded tip, from x0 to the tip end (dense near the end). */
export function stationsBout(x0, xr, xb, n = 10) {
  const out = [];
  for (let x = x0; x < xr - 1e-6; x += 0.03) out.push(x);
  for (let i = 0; i <= n; i++) out.push(xr + (xb - xr) * Math.sin((Math.PI / 2) * (i / n)));
  return out;
}

export const STAB = Object.freeze({ y: 0.4, rond: 1.6, bout: 1.75 });
/** Right-stabiliser section at span x. */
export function sectionStab(x, pts) {
  const le0 = lerp(3.85, 4.15, Math.min(x, 1.725) / 1.725), te0 = lerp(4.9, 4.87, Math.min(x, 1.725) / 1.725);
  const ch0 = te0 - le0, k = kRond(x, STAB.rond, STAB.bout), ch = ch0 * k, le = le0 + (1 - k) * 0.45 * ch0;
  return pts.map((p) => [x, STAB.y + p.y * ch, le + p.c * ch]);
}

// fin stations: y, leading edge z, trailing edge z, total thickness (m)
const FIN = [[0.42, 2.4, 4.95, 0.1], [0.62, 3.25, 4.95, 0.12], [0.78, 3.62, 4.95, 0.11], [1.2, 4.02, 4.93, 0.08], [1.45, 4.25, 4.92, 0.06]];
const finLE = pchip(FIN.map((f) => f[0]), FIN.map((f) => f[1]));
const finTE = pchip(FIN.map((f) => f[0]), FIN.map((f) => f[2]));
const finEp = pchip(FIN.map((f) => f[0]), FIN.map((f) => f[3]));
export const DERIVE = Object.freeze({ y0: 0.42, rond: 1.45, haut: 1.53 });
/** Fin section at height y, for a symmetric loop built with ep = 1 (y offsets scaled to metres). */
export function sectionDerive(y, pts, off = 0) {
  const yy = Math.min(y, DERIVE.rond), k = kRond(y, DERIVE.rond, DERIVE.haut);
  const le0 = finLE(yy), ch0 = finTE(yy) - le0, ch = ch0 * k, le = le0 + (1 - k) * 0.5 * ch0;
  return pts.map((p) => [p.y * finEp(yy) * k + Math.sign(p.y) * off, y, le + p.c * ch]);
}
