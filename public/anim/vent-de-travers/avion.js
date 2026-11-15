// Copyright: Your Name. Apache 2.0
// Procedural Cessna 172S for « Vent de travers », version 2. True metres (span 11.0 m, length 8.28 m).
//
// NODE CONTRACT (what the caller sees):
//   noeud  : TransformNode owned by the caller (position, yaw). Local axes before yaw:
//            nose toward +x, right wing toward +z, up +y (heading east: right wing points south).
//   ORIGIN : on the ground plane, midway between the two main-wheel contact points (tyres unloaded,
//            aeroplane level). noeud.position.y = 0 means the main wheels touch the runway.
//            Pitch is applied about this point, so the main wheels stay put during the flare.
//   maj(t, e, mode) only moves things INSIDE noeud (attitude, heave, gear, controls, propeller, lights).
//
// Rendering is a pure function of the film time t (no clocks, no randomness).

import { etat, PLANS, COULEUR, smooth, smoother, prog, rad, lerp } from './communs.js';
import { construirePieces, contourDessus, CLES } from './avion_pieces.js';
import { texturesFuselage, textureAile, materiauDisque } from './avion_peau.js';

const B = globalThis.BABYLON;
const V = (x, y, z) => new B.Vector3(x, y, z);

export const DIMENSIONS = Object.freeze({ envergure: 11.0, longueur: 8.28, hauteur: 2.72 });
/** Approach phases, as values of e.approche: flare, then main wheels on the runway. */
export const APPROCHE = Object.freeze({ arrondi: [0.6, 0.9], toucher: 0.9 });
const R_HELICE = 0.965; // m
const CONTACT = [0, -1.27, 0.12]; // model frame: under the main axle, between the wheels
const TR_MIN = Object.freeze({ croisiere: 2400, approche: 1700, reduit: 1000, ralenti: 820 }); // propeller rpm

/**
 * Creates the aeroplane.
 * @param {any} scene BABYLON.Scene (right-handed, 1 unit = 1 m)
 * @param {any} d data from chargerDonnees()
 * @param {{qualite?:'film'|'direct', obturation?:number, lumiereHelice?:number}} [options]
 *   qualite: texture size (film 4096 px, direct 2048 px); obturation: shutter time in s for the
 *   propeller blur (default 1/60); lumiereHelice: brightness of the blur disc (default 1).
 */
export function creerAvion(scene, d, options = {}) {
  const film = options.qualite !== 'direct';
  const obturation = options.obturation > 0 ? options.obturation : 1 / 60;

  /* ---------------- materials */
  const lin = (r, g, b) => new B.Color3(r, g, b).toLinearSpace();
  const pbr = (nom, albedo, rough, metal = 0, vernis = false) => {
    const m = new B.PBRMaterial(nom, scene);
    m.albedoColor = albedo;
    m.roughness = rough;
    m.metallic = metal;
    if (vernis) { m.clearCoat.isEnabled = true; m.clearCoat.intensity = 1; m.clearCoat.roughness = 0.04; }
    return m;
  };
  const blanc = lin(236 / 255, 238 / 255, 240 / 255);
  const tf = texturesFuselage(scene, film ? 4096 : 2048, film ? 2048 : 1024);
  const ta = textureAile(scene, film ? 2048 : 1024, film ? 1024 : 512);
  const mats = {
    peau: pbr('avion-peau', B.Color3.White(), 0.36, 0, true),
    aile: pbr('avion-aile', blanc, 0.36, 0, true),
    peinture: pbr('avion-peinture', blanc, 0.36, 0, true),
    bleu: pbr('avion-bleu', B.Color3.FromHexString(COULEUR.bleu).toLinearSpace(), 0.32, 0, true),
    vitre: pbr('avion-vitre', new B.Color3(0.012, 0.016, 0.02), 0.03),
    sombre: pbr('avion-joint', new B.Color3(0.02, 0.021, 0.024), 0.6),
    pneu: pbr('avion-pneu', new B.Color3(0.018, 0.018, 0.02), 0.88),
    metal: pbr('avion-metal', new B.Color3(0.62, 0.6, 0.57), 0.32, 1),
    interieur: pbr('avion-interieur', new B.Color3(0.035, 0.036, 0.04), 0.85),
    paroi: pbr('avion-paroi', new B.Color3(0.06, 0.06, 0.065), 0.9),
    siege: pbr('avion-siege', new B.Color3(0.06, 0.066, 0.078), 0.8),
  };
  mats.peau.albedoTexture = tf.albedo;
  mats.peau.useAlphaFromAlbedoTexture = true;
  mats.peau.transparencyMode = B.PBRMaterial.PBRMATERIAL_ALPHATEST;
  mats.peau.alphaCutOff = 0.5;
  mats.peau.bumpTexture = tf.normale;
  mats.peau.clearCoat.bumpTexture = tf.normale;
  mats.aile.bumpTexture = ta;
  mats.aile.clearCoat.bumpTexture = ta;
  mats.paroi.albedoTexture = tf.albedo; // same alpha: the liner has the same window holes
  mats.paroi.useAlphaFromAlbedoTexture = true;
  mats.paroi.transparencyMode = B.PBRMaterial.PBRMATERIAL_ALPHATEST;
  mats.paroi.alphaCutOff = 0.5;
  mats.paroi.environmentIntensity = 0.35;
  for (const k of ['interieur', 'siege']) { mats[k].environmentIntensity = 0.35; mats[k].backFaceCulling = false; mats[k].twoSidedLighting = true; }
  const mv = mats.vitre;
  // glass: dark tint, mirror-smooth, the sky's reflection at full strength
  mv.roughness = 0.05;
  mv.metallic = 0;
  mv.alpha = 0.35;
  mv.transparencyMode = B.PBRMaterial.PBRMATERIAL_ALPHABLEND;
  mv.useRadianceOverAlpha = true; // sky reflections stay at full strength on the clear glass
  mv.useSpecularOverAlpha = true;
  mv.backFaceCulling = false;
  mv.environmentIntensity = 2.2;

  /* ---------------- hierarchy: noeud → assiette (attitude) → repere (model → nose +x) */
  const noeud = new B.TransformNode('avion', scene);
  const assiette = new B.TransformNode('avion-assiette', scene);
  assiette.parent = noeud;
  assiette.rotationQuaternion = new B.Quaternion();
  const repere = new B.TransformNode('avion-repere', scene);
  repere.parent = assiette;
  repere.rotation.y = -Math.PI / 2;
  {
    // self-check of the rotation sign: the model nose (-z) must end on +x
    const m = B.Matrix.RotationY(repere.rotation.y);
    if (B.Vector3.TransformNormal(V(0, 0, -1), m).x < 0) repere.rotation.y = Math.PI / 2;
    const c = B.Vector3.TransformCoordinates(V(...CONTACT), B.Matrix.RotationY(repere.rotation.y));
    repere.position = c.scale(-1);
  }

  /* ---------------- parts */
  const pc = construirePieces(scene, { fuselageN: film ? 144 : 96 });
  const ombres = [];
  const prepare = (m, mat, parent) => {
    m.material = mat; m.parent = parent; m.isPickable = false; m.receiveShadows = true;
    if (mat !== mv) ombres.push(m);
    return m;
  };
  for (const k of CLES) {
    if (pc.P[k].length === 0) continue;
    const m = B.Mesh.MergeMeshes(pc.P[k], true, true);
    if (m) { m.name = `avion-${k}`; prepare(m, mats[k], repere); }
  }
  // flaps and ailerons: one pivot node each on its hinge line
  const surfaces = pc.volets.map((v) => {
    const pivot = new B.TransformNode(`avion-${v.type}-pivot`, scene);
    pivot.parent = repere;
    pivot.position = v.pivot.clone();
    pivot.rotationQuaternion = new B.Quaternion();
    v.mesh.position = v.pivot.scale(-1);
    prepare(v.mesh, mats.peinture, pivot);
    return { ...v, noeud: pivot };
  });
  const profPivot = new B.TransformNode('avion-profondeur-pivot', scene);
  profPivot.parent = repere;
  profPivot.position = pc.pivotProf.clone();
  profPivot.rotationQuaternion = new B.Quaternion();
  for (const m of pc.profondeur) { m.position = pc.pivotProf.scale(-1); prepare(m, mats.peinture, profPivot); }
  // gear groups (compression moves them up relative to the body)
  const groupe = (nom, liste) => {
    const n = new B.TransformNode(nom, scene);
    n.parent = repere;
    const parCle = {};
    for (const [k, m] of liste) (parCle[k] = parCle[k] || []).push(m);
    for (const k of Object.keys(parCle)) { const m = B.Mesh.MergeMeshes(parCle[k], true, true); if (m) prepare(m, mats[k], n); }
    return n;
  };
  const trainP = groupe('avion-train-principal', pc.train.principal);
  const trainA = groupe('avion-train-avant', pc.train.avant);
  // instrument faces: faint backlight
  const mCadran = new B.StandardMaterial('avion-cadran-mat', scene);
  mCadran.diffuseColor = new B.Color3(0.02, 0.02, 0.02);
  mCadran.emissiveColor = new B.Color3(0.08, 0.085, 0.09);
  mCadran.specularColor = new B.Color3(0.3, 0.3, 0.3);
  const cadrans = B.Mesh.MergeMeshes(pc.cadrans, true, true);
  cadrans.material = mCadran; cadrans.parent = repere; cadrans.isPickable = false;

  // propeller: spinner + exposure-integrated blur disc
  const rotor = new B.TransformNode('avion-rotor', scene);
  rotor.parent = repere;
  rotor.position = pc.rotor.clone();
  prepare(pc.cone, mats.peinture, rotor);
  prepare(pc.bague, mats.bleu, rotor);
  const disque = B.MeshBuilder.CreateDisc('avion-disque', { radius: R_HELICE + 0.01, tessellation: 160 }, scene);
  const md = materiauDisque(scene, R_HELICE);
  if (typeof options.lumiereHelice === 'number') md.regler(0, 1, options.lumiereHelice);
  disque.material = md.mat;
  disque.parent = rotor;
  disque.position.z = -0.045;
  disque.isPickable = false;

  /* ---------------- lights: emissive bulbs (for a GlowLayer), all driven by t */
  const bulbe = (nom, rgb, pos, diam, sz = 1) => {
    const m = new B.StandardMaterial(`${nom}-mat`, scene);
    m.disableLighting = true;
    m.diffuseColor = B.Color3.Black();
    m.emissiveColor = rgb.clone();
    const s = B.MeshBuilder.CreateSphere(nom, { diameter: diam, segments: 16 }, scene);
    s.scaling.z = sz;
    s.material = m; s.position = pos.clone(); s.parent = repere; s.isPickable = false;
    return { mesh: s, mat: m, base: rgb.clone() };
  };
  const f = pc.feux;
  const navG = bulbe('avion-feu-gauche', new B.Color3(1.6, 1.45, 1.2), f.navG, 0.06);
  const navD = bulbe('avion-feu-droit', new B.Color3(1.6, 1.45, 1.2), f.navD, 0.06);
  const navQ = bulbe('avion-feu-queue', new B.Color3(1.5, 1.5, 1.5), f.queue, 0.05);
  const balise = bulbe('avion-balise', new B.Color3(1.0, 0.92, 0.8), f.balise, 0.07);
  const strG = bulbe('avion-flash-gauche', new B.Color3(1, 1, 1), f.strobeG, 0.045);
  const strD = bulbe('avion-flash-droit', new B.Color3(1, 1, 1), f.strobeD, 0.045);
  const phare = bulbe('avion-phare', new B.Color3(1.0, 0.96, 0.88), f.phare, 0.09, 0.35);
  const lumineux = [navG, navD, navQ, balise, strG, strD, phare].map((l) => l.mesh);

  /* ---------------- time bases of the landing shot */
  // The caption « Posé. » appears at 51.3 s: the main wheels touch at 51.45 s, so it is true when read.
  // Approach progress (0..1, APPROCHE.toucher at touchdown) runs over the 3 s before it.
  const t0Pose = PLANS.pose.t[0];
  const tToucher = 51.45;
  const tRoueAvant = tToucher + 1.4;
  const approcheA = (tau) => APPROCHE.toucher * prog(tau, tToucher - 3, tToucher) + (1 - APPROCHE.toucher) * prog(tau, tToucher, tToucher + 1);

  /** Propeller rpm at film time tau in approach mode. */
  const trApproche = (tau) => {
    const a = approcheA(tau);
    const vol = lerp(TR_MIN.approche, TR_MIN.reduit, smooth(prog(a, 0.55, 0.85)));
    return lerp(vol, TR_MIN.ralenti, smooth(prog(tau, tToucher, tToucher + 1.5)));
  };
  /** Propeller angle (rad) at t: exact integral of the rpm from the shot start (fixed steps). */
  const angleHelice = (t, mode) => {
    if (mode !== 'approche') return ((2 * Math.PI * TR_MIN.croisiere) / 60) * t;
    const n = Math.max(1, Math.ceil((t - t0Pose) * 240)), h = (t - t0Pose) / n;
    let s = 0;
    for (let i = 0; i <= n; i++) s += (i === 0 || i === n ? 0.5 : 1) * trApproche(t0Pose + i * h);
    return ((2 * Math.PI) / 60) * s * h + 1.234;
  };

  const qA = new B.Quaternion(), qB = new B.Quaternion();
  const AXE_X = V(1, 0, 0), AXE_Z = V(0, 0, 1), AXE_MX = V(1, 0, 0);

  /**
   * Sets every animated property from the film time t.
   * @param {number} t film time (s)
   * @param {any} e etat(t, d)
   * @param {'croisiere'|'approche'} mode shot 3 or shot 10
   */
  function maj(t, e, mode = 'croisiere') {
    const ap = mode === 'approche';
    const a = ap ? approcheA(t) : 0;
    const surSol = ap && t >= tToucher;
    // light turbulence, calming down through the flare
    const calme = ap ? 0.6 * (1 - smooth(prog(a, 0.5, 0.85))) : 1;
    const roulis = rad(0.6) * calme * (Math.sin(1.31 * t) + 0.45 * Math.sin(2.87 * t + 1.1));
    const vRoulis = rad(0.6) * calme * (1.31 * Math.cos(1.31 * t) + 1.29 * Math.cos(2.87 * t + 1.1));
    const tangage0 = rad(0.3) * calme * Math.sin(0.93 * t + 0.5);
    const houle = (ap ? 0.04 : 0.08) * calme * (Math.sin(1.07 * t + 0.3) + 0.4 * Math.sin(2.3 * t));
    let tangageDeg = ap ? lerp(1, 6, smoother(prog(a, APPROCHE.arrondi[0], APPROCHE.arrondi[1]))) : 0; // never nose down near the ground
    if (ap) tangageDeg *= 1 - smoother(prog(t, tToucher + 0.5, tRoueAvant));
    const tangage = rad(tangageDeg) + tangage0;
    // main gear: spring legs take the load with a short damped bounce
    const tau = t - tToucher;
    const cP = surSol ? 0.045 * (1 - Math.exp(-5 * tau) * (Math.cos(11 * tau) + 0.45 * Math.sin(11 * tau))) : 0;
    const hRoueAvant = 2.54 * Math.sin(tangage) - cP; // nose wheel height above the runway
    const cA = surSol ? Math.max(0, -hRoueAvant) : 0;

    assiette.position.set(0, houle - cP, 0);
    B.Quaternion.RotationAxisToRef(AXE_Z, tangage, qA);
    B.Quaternion.RotationAxisToRef(AXE_X, roulis, qB);
    qA.multiplyToRef(qB, assiette.rotationQuaternion);
    trainP.position.y = cP;
    trainA.position.y = cA;

    // control surfaces (positive angle = trailing edge down)
    const volet = ap ? rad(30) : 0;
    const daRad = Math.max(-rad(8), Math.min(rad(8), 4 * vRoulis));
    for (const s of surfaces) {
      let ang = 0;
      if (s.type === 'volet') {
        ang = volet;
        s.noeud.position.set(s.pivot.x, s.pivot.y - 0.03 * (volet / rad(30)), s.pivot.z + 0.08 * (volet / rad(30)));
      } else ang = s.cote > 0 ? -daRad : daRad;
      B.Quaternion.RotationAxisToRef(s.axe, ang, s.noeud.rotationQuaternion);
    }
    const prof = ap ? -rad(2.2) * (tangageDeg + 1.5) : -3 * tangage0;
    B.Quaternion.RotationAxisToRef(AXE_MX, Math.max(-rad(20), Math.min(rad(6), prof)), profPivot.rotationQuaternion);

    // propeller blur: blades sweep omega * shutter during the exposure centred on t
    const tr = ap ? trApproche(t) : TR_MIN.croisiere;
    const balayage = ((2 * Math.PI * tr) / 60) * obturation;
    md.regler(angleHelice(t, mode) - balayage / 2, balayage);

    // lights: steady navigation lights, rotating beacon, double-flash strobes, landing light
    const bal = Math.pow(Math.max(0, Math.cos(2 * Math.PI * 0.75 * t)), 12);
    balise.mat.emissiveColor.copyFrom(balise.base.scale(0.12 + 2.2 * bal));
    const pf = ((t % 1.2) + 1.2) % 1.2;
    const flash = pf < 0.04 || (pf > 0.14 && pf < 0.18);
    strG.mesh.setEnabled(flash); strD.mesh.setEnabled(flash);
    strG.mat.emissiveColor.copyFrom(strG.base.scale(3)); strD.mat.emissiveColor.copyFrom(strD.base.scale(3));
    phare.mat.emissiveColor.copyFrom(phare.base.scale(ap ? 2.6 : 0.3));
  }

  const setOmbres = (gen) => {
    if (!gen) return;
    for (const m of ombres) gen.addShadowCaster(m, false);
  };

  maj(PLANS.avion.t[0], etat(PLANS.avion.t[0], d), 'croisiere');
  return {
    noeud, maj, setOmbres,
    /** emissive bulb meshes, to include in a GlowLayer */
    lumineux,
    /** blur disc (alpha-blended ShaderMaterial): exclude it from GlowLayer / effect layers */
    disque,
    /** film times: main wheels touch, nose wheel down (approach mode) */
    phases: { tToucher, tRoueAvant },
    dimensions: DIMENSIONS,
  };
}

/* ------------------------------------------------------------------ top-view icon for the CARTE scene */

function trianguler(pts) {
  const cr = (a, b, c) => (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
  let aire = 0;
  for (let i = 0; i < pts.length; i++) { const p = pts[i], q = pts[(i + 1) % pts.length]; aire += p[0] * q[1] - q[0] * p[1]; }
  const idx = [...pts.keys()];
  if (aire < 0) idx.reverse();
  const tris = [];
  const dedans = (p, a, b, c) => cr(a, b, p) > 1e-12 && cr(b, c, p) > 1e-12 && cr(c, a, p) > 1e-12;
  while (idx.length > 3) {
    let coupe = false;
    for (let i = 0; i < idx.length && !coupe; i++) {
      const ia = idx[(i + idx.length - 1) % idx.length], ib = idx[i], ic = idx[(i + 1) % idx.length];
      const A = pts[ia], Bp = pts[ib], C = pts[ic];
      if (cr(A, Bp, C) <= 1e-12) continue;
      if (idx.some((j) => j !== ia && j !== ib && j !== ic && dedans(pts[j], A, Bp, C))) continue;
      tris.push(ia, ib, ic); idx.splice(i, 1); coupe = true;
    }
    if (!coupe) { // only flat corners left: drop the flattest
      let best = 0, bv = Infinity;
      for (let i = 0; i < idx.length; i++) {
        const v = Math.abs(cr(pts[idx[(i + idx.length - 1) % idx.length]], pts[idx[i]], pts[idx[(i + 1) % idx.length]]));
        if (v < bv) { bv = v; best = i; }
      }
      idx.splice(best, 1);
    }
  }
  if (idx.length === 3) tris.push(...idx);
  return tris;
}

/**
 * Flat top-view silhouette of the same aircraft for the CARTE scene: in the XZ plane (y = 0, seen
 * from +y), overall length 1 (nose to elevator trailing edge), nose toward +x, right wing toward +z,
 * origin at mid-length. A single non-overlapping polygon, so a translucent material shows no
 * darker overlaps. Double-sided.
 * @param {any} scene
 * @param {{nom?:string, materiau?:any}} [options] materiau: replaces the default white emissive one
 */
export function silhouetteDessus(scene, options = {}) {
  const c = contourDessus(); // [x right, z back] in metres
  let z0 = Infinity, z1 = -Infinity;
  for (const p of c) { z0 = Math.min(z0, p[1]); z1 = Math.max(z1, p[1]); }
  const L = z1 - z0, zc = (z0 + z1) / 2;
  const pts = c.map(([x, z]) => [-(z - zc) / L, x / L]); // [X forward, Z right]
  const tris = trianguler(pts);
  const vd = new B.VertexData();
  vd.positions = pts.flatMap(([X, Z]) => [X, 0, Z]);
  vd.indices = tris;
  vd.normals = pts.flatMap(() => [0, 1, 0]);
  const mesh = new B.Mesh(options.nom || 'avion-silhouette', scene);
  vd.applyToMesh(mesh);
  mesh.isPickable = false;
  let m = options.materiau;
  if (!m) {
    m = new B.StandardMaterial(`${mesh.name}-mat`, scene);
    m.disableLighting = true;
    m.emissiveColor = B.Color3.White();
  }
  m.backFaceCulling = false;
  mesh.material = m;
  return mesh;
}
