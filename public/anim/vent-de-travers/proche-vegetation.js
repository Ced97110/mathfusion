// Copyright: Your Name. Apache 2.0
// « Vent de travers » v2 — PROCHE scene: grass blades near the lens and tree rows to the horizon.
// Grass: a fixed grid of thin instances follows the camera in steps of one cell; each blade's place,
// size, lean and colour come from a hash of its world cell, so blades never swim. The instance
// matrices are scaled to almost nothing, so depth and shadow passes (which do not run the custom
// vertex code) see no stray geometry. Wind sway is a function of the film time only.

import { prng } from './communs.js';
import { GLSL_BRUIT } from './proche-ciel.js';
import { GLSL_HERBE_ICI, PISTE_L } from './proche-sol-glsl.js';

const B = globalThis.BABYLON;

function brin(scene) {
  // a blade: 6 levels, narrowing to a tip; local x across (-0.5..0.5), y up (0..1)
  const pos = []; const nor = []; const ind = [];
  const n = 6;
  for (let i = 0; i < n; i++) {
    const y = i / n;
    const w = 0.5 * Math.pow(1 - y, 0.6);
    pos.push(-w, y, 0, w, y, 0);
    nor.push(0, 0, 1, 0, 0, 1);
  }
  pos.push(0, 1, 0); nor.push(0, 0, 1);
  for (let i = 0; i < n - 1; i++) {
    const a = 2 * i;
    ind.push(a, a + 1, a + 2, a + 1, a + 3, a + 2);
  }
  ind.push(2 * (n - 1), 2 * (n - 1) + 1, 2 * n);
  const m = new B.Mesh('brin', scene);
  const vd = new B.VertexData();
  vd.positions = pos; vd.normals = nor; vd.indices = ind;
  vd.applyToMesh(m);
  return m;
}

/**
 * @param {BABYLON.Scene} scene
 * @param {{ film: boolean, uSite: BABYLON.Vector4, ventSol: {x:number,z:number} }} o
 */
export function creerHerbe(scene, o) {
  const pas = o.film ? 0.032 : 0.06; // cell size (m)
  const cote = o.film ? 600 : 300; // cells per side
  const m = brin(scene);
  const N = cote * cote;
  const buf = new Float32Array(N * 16);
  const tiny = 1e-4;
  for (let j = 0; j < cote; j++) {
    for (let i = 0; i < cote; i++) {
      const k = (j * cote + i) * 16;
      buf[k] = tiny; buf[k + 5] = tiny; buf[k + 10] = tiny; buf[k + 15] = 1;
      buf[k + 12] = (i - cote / 2) * pas; buf[k + 13] = 0; buf[k + 14] = (j - cote / 2) * pas;
    }
  }
  m.thinInstanceSetBuffer('matrix', buf, 16, true);
  m.alwaysSelectAsActiveMesh = true;
  m.isPickable = false;
  m.receiveShadows = true;

  const uH = new B.Vector4(pas, cote * pas * 0.5, 0, 1); // cell, fade radius, time, height scale
  const uOeilH = new B.Vector4(0, 0, 0, 0);
  const uVentH = new B.Vector4(o.ventSol.x, o.ventSol.z, 0, 0);
  const mat = new B.PBRCustomMaterial('matHerbe', scene);
  mat.metallic = 0;
  mat.roughness = 0.72;
  mat.backFaceCulling = false;
  mat.twoSidedLighting = true;
  mat.AddUniform('uSite', 'vec4', o.uSite);
  mat.AddUniform('uHerbe', 'vec4', uH);
  mat.AddUniform('uOeilH', 'vec4', uOeilH);
  mat.AddUniform('uVentH', 'vec4', uVentH);
  mat.Vertex_Definitions(`${GLSL_BRUIT}\n${GLSL_HERBE_ICI}\nvarying vec2 vHerbe;\n`);
  mat.Fragment_Definitions('varying vec2 vHerbe;\n');
  mat.Vertex_After_WorldPosComputed(`
  {
    vec3 rac = (finalWorld * vec4(0.0, 0.0, 0.0, 1.0)).xyz;
    vec2 cell = floor(rac.xz / uHerbe.x + 0.5);
    float h1 = hf(cell, 101.0); float h2 = hf(cell, 102.0); float h3 = hf(cell, 103.0); float h4 = hf(cell, 104.0);
    vec2 base = (cell + vec2(h1, h2) - 0.5) * uHerbe.x;
    float dist = length(base - uOeilH.xz);
    float fade = 1.0 - smoothstep(uHerbe.y * 0.6, uHerbe.y * 0.95, dist);
    float touffe = vn(base * 1.7, 105.0);
    float haut = (0.05 + 0.15 * h3 * h3 + 0.08 * touffe) * fade * herbeIci(base) * uHerbe.w;
    float larg = 0.003 + 0.0035 * h4;
    float a = (h1 * 7.0 + h2 * 3.0) * 3.14159;
    vec3 lat = vec3(cos(a), 0.0, sin(a));
    vec3 nrm = vec3(-lat.z, 0.0, lat.x);
    float y = position.y;
    vec2 penche = (vec2(hf(cell, 106.0), hf(cell, 107.0)) - 0.5) * 0.9;
    float ph = dot(base, vec2(0.9, 1.3)) + h4 * 6.2832;
    float raf = 0.5 + 0.5 * sin(uHerbe.z * 2.3 + ph) * sin(uHerbe.z * 0.71 + ph * 0.37);
    vec2 sway = uVentH.xy * (0.25 + 0.45 * raf) + penche;
    vec3 pw = vec3(base.x, 0.0, base.y) + lat * position.x * larg + vec3(0.0, y * haut, 0.0)
      + vec3(sway.x, 0.0, sway.y) * y * y * haut;
    worldPos = vec4(pw, 1.0);
    vPositionW = pw;
    vNormalW = normalize(nrm + vec3(sway.x, 0.8, sway.y));
    vHerbe = vec2(y, h3 * 0.6 + touffe * 0.4);
  }
`);
  mat.Fragment_Custom_Albedo(`
    vec3 cH = mix(vec3(0.36, 0.50, 0.22), vec3(0.50, 0.57, 0.28), vHerbe.y);
    cH = mix(cH, vec3(0.58, 0.53, 0.33), smoothstep(0.78, 0.95, vHerbe.y)); // a few dry blades
    surfaceAlbedo = pow(cH, vec3(2.2)) * mix(0.28, 1.0, smoothstep(0.0, 0.7, vHerbe.x));
  `);
  m.material = mat;

  /** @param {number} t film time @param {BABYLON.Vector3} oeil camera position @param {number} hauteur 0 hides the grass */
  function maj(t, oeil, hauteur) {
    m.setEnabled(hauteur > 0 && oeil.y < 30);
    m.position.set(Math.round(oeil.x / pas) * pas, 0, Math.round(oeil.z / pas) * pas);
    uH.z = t; uH.w = hauteur;
    uOeilH.set(oeil.x, oeil.y, oeil.z, 0);
  }
  return { maillage: m, maj };
}

/** One lumpy blob: an icosphere pushed by deterministic noise (phase f), smooth normals. */
function blob(scene, f, sub) {
  const m = B.MeshBuilder.CreateIcoSphere('blob', { radius: 1, subdivisions: sub, flat: false }, scene);
  const p = m.getVerticesData(B.VertexBuffer.PositionKind);
  for (let i = 0; i < p.length; i += 3) {
    const x = p[i]; const y = p[i + 1]; const z = p[i + 2];
    // a few large lobes (branch clusters), then smaller leafy bumps
    const lobes = 0.1 * Math.sin(x * 4.1 + y * 2.3 + f) * Math.cos(z * 3.7 - y * 2.9 + 2 * f)
      + 0.08 * Math.sin(x * 7.3 - z * 6.1 + y * 5.2 + 3 * f);
    const feuilles = 0.035 * Math.sin(x * 17 + y * 13 + f) * Math.sin(z * 19 - y * 11) + 0.02 * Math.sin(x * 31 + z * 29 + y * 23);
    const n = 1 + lobes + feuilles;
    p[i] = x * n; p[i + 1] = y * n; p[i + 2] = z * n;
  }
  m.setVerticesData(B.VertexBuffer.PositionKind, p);
  return m;
}

/**
 * Crown template k: 3 to 5 leafy masses of different sizes, stacked unevenly (prng(700 + k)).
 * Fits roughly in the unit sphere stretched 1.25 upward, like the single crown it replaces.
 */
function couronne(scene, k) {
  const r = prng(700 + k);
  const nb = 3 + Math.floor(r() * 3);
  const parts = [];
  for (let i = 0; i < nb; i++) {
    const m = blob(scene, 1.3 * k + 0.9 * i, 4);
    const R = 0.42 + 0.3 * r();
    const a = r() * Math.PI * 2; const d = (1 - R) * (0.4 + 0.6 * r());
    m.scaling.set(R, R * (1 + 0.3 * r()), R);
    m.position.set(Math.cos(a) * d, -0.6 + 1.6 * (i + r() * 0.6) / nb, Math.sin(a) * d);
    m.bakeCurrentTransformIntoVertices();
    parts.push(m);
  }
  const m = B.Mesh.MergeMeshes(parts, true, true);
  m.name = `couronne${k}`;
  const nor = [];
  B.VertexData.ComputeNormals(m.getVerticesData(B.VertexBuffer.PositionKind), m.getIndices(), nor);
  m.setVerticesData(B.VertexBuffer.NormalKind, nor);
  return m;
}
const N_GABARITS = 5;

/** Rows of trees along polder roads around both sites (none near the camera paths). */
export function creerArbres(scene) {
  const gab = Array.from({ length: N_GABARITS }, (_, k) => couronne(scene, k));
  const tronc = B.MeshBuilder.CreateCylinder('tronc', { height: 1, diameterTop: 0.35, diameterBottom: 0.6, tessellation: 7 }, scene);
  tronc.bakeTransformIntoVertices(B.Matrix.Translation(0, 0.5, 0));
  const matC = new B.PBRMaterial('matCouronne', scene);
  matC.albedoColor = new B.Color3(0.052, 0.062, 0.034); // late-autumn olive, varied per tree below
  matC.metallic = 0; matC.roughness = 0.95;
  const matT = new B.PBRMaterial('matTronc', scene);
  matT.albedoColor = new B.Color3(0.07, 0.06, 0.05);
  matT.metallic = 0; matT.roughness = 0.95;
  for (const c of gab) c.material = matC;
  tronc.material = matT;

  const sites = [];
  for (const [site, exclu] of [[0, (x, z) => Math.hypot(x, z) < 380], [1, (x, z) => Math.abs(z) < 200 && x > -1400 && x < PISTE_L + 300]]) {
    const r = prng(5000 + site);
    const mc = gab.map(() => []); const mt = []; const coul = gab.map(() => []);
    for (let k = 0; k < 46; k++) {
      const ang = (r() < 0.5 ? 0 : Math.PI / 2) + (r() - 0.5) * 0.06;
      const d = 400 + 5600 * r() * r();
      const a = r() * Math.PI * 2;
      const x0 = Math.cos(a) * d; const z0 = Math.sin(a) * d;
      const L = 120 + 700 * r();
      // irregular spacing: gaps, pairs, the odd missing tree
      for (let s = 0; s < L; s += 4.5 + 10 * r() * r()) {
        const x = x0 + Math.cos(ang) * s + (r() - 0.5) * 4;
        const z = z0 + Math.sin(ang) * s + (r() - 0.5) * 4;
        if (exclu(x, z) || r() < 0.14) continue;
        const g = Math.floor(r() * N_GABARITS);
        const h = 7 + 9 * r();
        const R = 2.2 + 2.8 * r();
        const q = B.Quaternion.FromEulerAngles(0, r() * 6.28, 0);
        mc[g].push(B.Matrix.Compose(new B.Vector3(R, h * 0.4, R), q, new B.Vector3(x, h * 0.58, z)));
        mt.push(B.Matrix.Compose(new B.Vector3(1, h * 0.6, 1), q, new B.Vector3(x, 0, z)));
        const v = 0.65 + 0.6 * r();
        const brun = r();
        coul[g].push(v * (0.9 + 0.4 * brun), v * (0.95 + 0.05 * brun), v * (0.85 - 0.15 * brun), 1);
      }
    }
    sites.push({ mc, mt, coul: coul.map((c) => new Float32Array(c)) });
  }
  const remplir = (m, liste) => {
    const buf = new Float32Array(Math.max(1, liste.length) * 16);
    liste.forEach((mm, i) => mm.copyToArray(buf, i * 16));
    m.thinInstanceSetBuffer('matrix', buf, 16, false);
  };
  let courant = -1;
  /** @param {number} site 0 launch field, 1 runway */
  function maj(site) {
    if (site === courant) return;
    courant = site;
    gab.forEach((c, g) => {
      remplir(c, sites[site].mc[g]);
      c.thinInstanceSetBuffer('color', sites[site].coul[g], 4, false);
      c.thinInstanceRefreshBoundingInfo();
    });
    remplir(tronc, sites[site].mt);
    tronc.thinInstanceRefreshBoundingInfo();
  }
  for (const m of [...gab, tronc]) { m.isPickable = false; }
  return { couronne: gab[0], couronnes: gab, tronc, maj };
}
