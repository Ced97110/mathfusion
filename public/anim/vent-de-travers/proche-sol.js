// Copyright: Your Name. Apache 2.0
// « Vent de travers » v2 — PROCHE scene: ground meshes. A polar ring of the ground centred under the
// camera (dense near the lens, 300 km wide, with the Earth's curvature), the dug drainage ditch of the
// launch field (a true 3D patch), its water (planar mirror), and the fence along the far bank.
// Shading is in proche-sol-glsl.js (analytic, filtered). Units: metres.

import { COULEUR, prng } from './communs.js';
import { GLSL_SOL, GLSL_SOL_ALBEDO, GLSL_SOL_FINAL, FOSSE_Z, CLOTURE_Z } from './proche-sol-glsl.js';

const B = globalThis.BABYLON;
const R_TERRE = 6371000;
const SOL_R = 300000;
const PATCH = { x0: -80, x1: 80, z0: 7.5, z1: 17.5 };

const lin = (hex) => B.Color3.FromHexString(hex).toLinearSpace();

/** Polar grid: rings of geometric radius (0.25 m … 300 km), 160 segments, curvature built in. */
function anneauSol(scene) {
  const seg = 160;
  const rayons = [0];
  for (let r = 0.25; r < SOL_R; r *= 1.11) rayons.push(r);
  rayons.push(SOL_R);
  const pos = []; const nor = []; const ind = [];
  for (let i = 0; i < rayons.length; i++) {
    const r = rayons[i];
    const y = -(r * r) / (2 * R_TERRE);
    const n = i === 0 ? 1 : seg;
    for (let j = 0; j < n; j++) {
      const a = (j / seg) * Math.PI * 2;
      pos.push(r * Math.cos(a), y, r * Math.sin(a));
      nor.push(0, 1, 0);
    }
  }
  for (let j = 0; j < seg; j++) ind.push(0, 1 + ((j + 1) % seg), 1 + j);
  for (let i = 1; i < rayons.length - 1; i++) {
    const a0 = 1 + (i - 1) * seg; const a1 = 1 + i * seg;
    for (let j = 0; j < seg; j++) {
      const j1 = (j + 1) % seg;
      ind.push(a0 + j, a0 + j1, a1 + j, a0 + j1, a1 + j1, a1 + j);
    }
  }
  const m = new B.Mesh('sol', scene);
  const vd = new B.VertexData();
  vd.positions = pos; vd.normals = nor; vd.indices = ind;
  vd.applyToMesh(m);
  return m;
}

/** Ditch profile across the launch field (height in metres, 0 = field level). */
export function hauteurFosse(x, z) {
  const wob = 0.12 * Math.sin(x * 0.21) + 0.07 * Math.sin(x * 0.57 + 1.0);
  const d = Math.abs(z - FOSSE_Z + wob);
  const s = Math.min(1, Math.max(0, (d - 0.85) / 0.85));
  const lisse = s * s * (3 - 2 * s);
  const fond = -0.78 + 0.03 * Math.sin(x * 1.3);
  const micro = 0.012 * Math.sin(x * 2.7 + z * 3.1) + 0.008 * Math.sin(x * 5.3 - z * 4.7);
  return d > 1.7 ? micro : fond * (1 - lisse) + micro * lisse;
}

function patchFosse(scene) {
  const nx = 641; const nz = 81;
  const pos = []; const ind = [];
  for (let k = 0; k < nz; k++) {
    const z = PATCH.z0 + ((PATCH.z1 - PATCH.z0) * k) / (nz - 1);
    for (let i = 0; i < nx; i++) {
      const x = PATCH.x0 + ((PATCH.x1 - PATCH.x0) * i) / (nx - 1);
      const bordX = Math.min(1, (x - PATCH.x0) / 0.5, (PATCH.x1 - x) / 0.5);
      const bordZ = Math.min(1, (z - PATCH.z0) / 0.5, (PATCH.z1 - z) / 0.5);
      pos.push(x, hauteurFosse(x, z) * Math.max(0, Math.min(bordX, bordZ)), z);
    }
  }
  for (let k = 0; k < nz - 1; k++) {
    for (let i = 0; i < nx - 1; i++) {
      const a = k * nx + i; const b = a + 1; const c = a + nx; const d = c + 1;
      ind.push(a, c, b, b, c, d);
    }
  }
  const nor = [];
  B.VertexData.ComputeNormals(pos, ind, nor);
  const m = new B.Mesh('fosse', scene);
  const vd = new B.VertexData();
  vd.positions = pos; vd.normals = nor; vd.indices = ind;
  vd.applyToMesh(m);
  return m;
}

/** The runway designator "09": white digits on black, mip-mapped (u across, v along the runway). */
function texteChiffres(scene) {
  const tex = new B.DynamicTexture('chiffres09', { width: 512, height: 384 }, scene, true);
  const ctx = tex.getContext();
  ctx.fillStyle = '#000'; ctx.fillRect(0, 0, 512, 384);
  ctx.fillStyle = '#fff';
  ctx.textBaseline = 'alphabetic';
  ctx.font = '700 400px "Helvetica Neue", Arial, sans-serif';
  const chiffre = (c, cx) => {
    const m = ctx.measureText(c);
    const h = (m.actualBoundingBoxAscent || 290) + (m.actualBoundingBoxDescent || 0);
    ctx.save();
    ctx.translate(cx, 384 - 8);
    ctx.scale(118 / m.width, 368 / h);
    ctx.fillText(c, -m.width / 2, -(m.actualBoundingBoxDescent || 0));
    ctx.restore();
  };
  chiffre('0', 512 * 0.2917);
  chiffre('9', 512 * 0.7083);
  tex.update(true);
  tex.anisotropicFilteringLevel = 16;
  tex.wrapU = B.Texture.CLAMP_ADDRESSMODE;
  tex.wrapV = B.Texture.CLAMP_ADDRESSMODE;
  return tex;
}

/**
 * @param {BABYLON.Scene} scene
 * @param {{ ombres: BABYLON.CascadedShadowGenerator, film: boolean, couches: number[][] }} o
 */
export function creerSol(scene, o) {
  const u = {
    site: new B.Vector4(0, 0, 0, 0),
    trou: new B.Vector4(PATCH.x0 + 0.5, PATCH.z0 + 0.5, PATCH.x1 - 0.5, PATCH.z1 - 0.5),
    trait: new B.Vector4(0, 0, 3, 0),
    traitCol: new B.Vector4(0, 0, 0, 0),
    route: new B.Vector4(0, 0, 2.5, 0),
    routeCol: new B.Vector4(0, 0, 0, 0),
    soleil: new B.Vector4(0, 1, 0, 0),
    ombreN: new B.Vector4(0, 0, 0.66, 0.55),
    couches: new B.Vector4(0.5 * (o.couches[0][0] + o.couches[0][1]), 0.5 * (o.couches[1][0] + o.couches[1][1]), 1, 0),
    oeil: new B.Vector4(0, 0, 0, 0),
  };
  const violet = lin(COULEUR.violet).scale(1.6);
  const gris = lin(COULEUR.gris).scale(0.55);
  u.traitCol.set(violet.r, violet.g, violet.b, 0);
  u.routeCol.set(gris.r, gris.g, gris.b, 0);

  const mat = new B.PBRCustomMaterial('matSol', scene);
  mat.metallic = 0;
  mat.roughness = 0.9;
  mat.albedoColor = B.Color3.White();
  mat.backFaceCulling = false; // flat ground: winding does not matter, culling would only hide it
  mat.AddUniform('uSite', 'vec4', u.site);
  mat.AddUniform('uTrou', 'vec4', u.trou);
  mat.AddUniform('uTrait', 'vec4', u.trait);
  mat.AddUniform('uTraitCol', 'vec4', u.traitCol);
  mat.AddUniform('uRoute', 'vec4', u.route);
  mat.AddUniform('uRouteCol', 'vec4', u.routeCol);
  mat.AddUniform('uSoleil', 'vec4', u.soleil);
  mat.AddUniform('uOmbreN', 'vec4', u.ombreN);
  mat.AddUniform('uCouches', 'vec4', u.couches);
  mat.AddUniform('uOeil', 'vec4', u.oeil);
  mat.AddUniform('uChiffres', 'sampler2D', texteChiffres(scene));
  mat.Fragment_Definitions(GLSL_SOL);
  mat.Fragment_Custom_Albedo(GLSL_SOL_ALBEDO);
  mat.Fragment_Custom_MetallicRoughness('metallicRoughness.r = 0.0; metallicRoughness.g = gRough;');
  mat.Fragment_Before_Fog(GLSL_SOL_FINAL);

  const sol = anneauSol(scene);
  sol.material = mat;
  sol.receiveShadows = true;
  sol.isPickable = false;
  sol.alwaysSelectAsActiveMesh = true;

  const fosse = patchFosse(scene);
  fosse.material = mat;
  fosse.receiveShadows = true;
  fosse.isPickable = false;

  // ---- water in the ditch: dark, smooth, planar reflection of what stands above it ----------
  const eau = B.MeshBuilder.CreateGround('eau', { width: PATCH.x1 - PATCH.x0, height: 3.8, subdivisions: 1 }, scene);
  eau.position.set(0, -0.55, FOSSE_Z);
  const matEau = new B.PBRMaterial('matEau', scene);
  matEau.albedoColor = new B.Color3(0.012, 0.016, 0.014);
  matEau.metallic = 0;
  matEau.roughness = 0.03;
  const miroir = new B.MirrorTexture('miroirFosse', o.film ? 1024 : 512, scene, false, B.Constants.TEXTURETYPE_HALF_FLOAT);
  miroir.mirrorPlane = new B.Plane(0, -1, 0, -0.55);
  miroir.level = 1;
  matEau.reflectionTexture = miroir;
  eau.material = matEau;
  eau.receiveShadows = true;
  eau.isPickable = false;

  // ---- fence: weathered posts every 2.5 m and three sagging wires ---------------------------
  const r = prng(1222);
  const poteau = B.MeshBuilder.CreateBox('poteau', { width: 0.09, depth: 0.09, height: 1.15 }, scene);
  poteau.bakeTransformIntoVertices(B.Matrix.Translation(0, 0.575 - 0.08, 0));
  const matBois = new B.PBRMaterial('matBois', scene);
  matBois.albedoColor = new B.Color3(0.20, 0.17, 0.13);
  matBois.metallic = 0; matBois.roughness = 0.88;
  poteau.material = matBois;
  const xs = [];
  for (let x = PATCH.x0 + 2; x <= PATCH.x1 - 2; x += 2.5) xs.push(x + (r() - 0.5) * 0.25);
  const mats = new Float32Array(xs.length * 16);
  const sommets = [];
  xs.forEach((x, i) => {
    const z = CLOTURE_Z + (r() - 0.5) * 0.1;
    const q = B.Quaternion.FromEulerAngles((r() - 0.5) * 0.06, r() * Math.PI, (r() - 0.5) * 0.06);
    const s = new B.Vector3(1, 0.92 + r() * 0.12, 1);
    B.Matrix.Compose(s, q, new B.Vector3(x, 0, z)).copyToArray(mats, i * 16);
    sommets.push(new B.Vector3(x, 0, z));
  });
  poteau.thinInstanceSetBuffer('matrix', mats, 16, true);
  poteau.receiveShadows = true;
  poteau.isPickable = false;
  o.ombres.addShadowCaster(poteau);
  const matFil = new B.PBRMaterial('matFil', scene);
  matFil.albedoColor = new B.Color3(0.35, 0.35, 0.34);
  matFil.metallic = 0.9; matFil.roughness = 0.45;
  const fils = [0.38, 0.68, 0.98].map((h, k) => {
    const chemin = [];
    for (let i = 0; i < sommets.length - 1; i++) {
      const a = sommets[i]; const b = sommets[i + 1];
      for (let s = 0; s < 6; s++) {
        const t = s / 6;
        const sag = 0.025 * 4 * t * (1 - t);
        chemin.push(new B.Vector3(a.x + (b.x - a.x) * t, h - sag, a.z + (b.z - a.z) * t - 0.05));
      }
    }
    const f = B.MeshBuilder.CreateTube(`fil${k}`, { path: chemin, radius: 0.0018, tessellation: 5 }, scene);
    f.material = matFil;
    f.isPickable = false;
    return f;
  });

  miroir.renderList.push(fosse, poteau, ...fils);

  /**
   * @param {{ site: number, decalage: number[], oeil: BABYLON.Vector3, soleil: BABYLON.Vector3,
   *   air: {x:number,z:number}, nuages: number, trait: number[]|null, route: number[]|null }} p
   */
  function maj(p) {
    u.site.set(p.site, p.decalage[0], p.decalage[1], 0);
    sol.position.set(p.oeil.x, 0, p.oeil.z);
    u.oeil.set(p.oeil.x, p.oeil.y, p.oeil.z, 0);
    u.soleil.set(p.soleil.x, p.soleil.y, p.soleil.z, 0);
    u.ombreN.x = p.air.x; u.ombreN.y = p.air.z;
    u.couches.z = p.nuages;
    const lacher = p.site === 0;
    if (lacher) u.trou.set(PATCH.x0 + 0.5, PATCH.z0 + 0.5, PATCH.x1 - 0.5, PATCH.z1 - 0.5);
    else u.trou.set(1, 1, -1, -1);
    const proche = lacher && Math.hypot(p.oeil.x, p.oeil.z - FOSSE_Z) < 400 && p.oeil.y < 60;
    fosse.setEnabled(lacher);
    eau.setEnabled(proche);
    poteau.setEnabled(lacher && p.oeil.y < 400);
    for (const f of fils) f.setEnabled(lacher && p.oeil.y < 400);
    if (p.trait) u.trait.set(p.trait[0], p.trait[1], p.trait[2], p.trait[3]); else u.trait.w = 0;
    if (p.route) u.route.set(p.route[0], p.route[1], p.route[2], p.route[3]); else u.route.w = 0;
  }

  return { sol, fosse, eau, miroir, poteau, fils, materiau: mat, uniformes: u, maj };
}
