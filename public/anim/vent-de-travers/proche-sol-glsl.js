// Copyright: Your Name. Apache 2.0
// « Vent de travers » v2 — PROCHE scene: GLSL of the ground, in metres. Everything is computed from
// the world position with analytic filtering (box-filtered cells and stripes, noise octaves that
// fade before they alias), so the ground holds from a grass blade at the lens to the horizon.
// Site 0 = the launch field at De Bilt (origin = launch point). Site 1 = runway 09 (origin =
// threshold on the centreline, the runway runs east along +x for PISTE_L metres, 45 m wide).
// Uniforms expected (declared by the material): uSite, uTrou, uTrait, uTraitCol, uRoute, uRouteCol,
// uSoleil, uOmbreN, uCouches, uOeil, uChiffres.

import { GLSL_BRUIT, GLSL_COUVERTURE } from './proche-ciel.js';

export const PISTE_L = 2000; // runway length (scenery only, never shown as a number)
export const PISTE_W = 45; // runway width, true size
export const FOSSE_Z = 12.5; // launch site: drainage ditch centre line
export const CHEMIN_Z = [4.2, 6.4]; // launch site: gravel path
export const CLOTURE_Z = 15.0; // launch site: fence on the far bank

/** Grass presence used by the 3D blades (same rules as the ground shading). Needs uniform uSite. */
export const GLSL_HERBE_ICI = `
// grass presence used by the 3D blades (same rules as the shading)
float herbeIci(vec2 p){
  if (uSite.x < 0.5) {
    float dz = abs(p.y - FOSSE_Z0);
    if (dz < 2.3) return 0.0;
    if (p.y > CHEMIN_Z0 - 0.25 && p.y < CHEMIN_Z1 + 0.25) return 0.0;
    if (abs(p.x) < 1.7 && abs(p.y) < 1.7) return 0.0;
    return 1.0;
  }
  if (abs(p.y) < 24.5 && p.x > -3.5 && p.x < ${(PISTE_L + 3.5).toFixed(1)}) return 0.0;
  return 1.0;
}
`.replace(/CHEMIN_Z0/g, CHEMIN_Z[0].toFixed(2)).replace(/CHEMIN_Z1/g, CHEMIN_Z[1].toFixed(2)).replace(/FOSSE_Z0/g, FOSSE_Z.toFixed(2));

export const GLSL_SOL = `
${GLSL_BRUIT}
${GLSL_COUVERTURE}
vec3 gAlb; float gRough; float gEau; float gHerbe; float gMarque;

// 1D box filter of the interval [a, b] seen through a pixel footprint w centred on x
float boite(float x, float a, float b, float w){
  w = max(w, 1e-5);
  return clamp((min(x + 0.5 * w, b) - max(x - 0.5 * w, a)) / w, 0.0, 1.0);
}
float rect(vec2 p, vec2 a, vec2 b, vec2 w){ return boite(p.x, a.x, b.x, w.x) * boite(p.y, a.y, b.y, w.y); }
// periodic dashes [a, b] of period P along x; fades to the mean when unresolved
float tirets(float x, float P, float a, float b, float w){
  float m = (b - a) / P;
  if (w > 0.45 * P) return m;
  float xm = mod(x, P);
  float c = boite(xm, a, b, w) + boite(xm - P, a, b, w) + boite(xm + P, a, b, w);
  return mix(c, m, smoothstep(0.2, 0.45, w / P));
}
// band of half-width h around d = 0, filtered; fades to its mean coverage m when unresolved
float bande(float d, float h, float fw, float m){
  float c = boite(d, -h, h, fw);
  return m < 0.0 ? c : mix(c, m, smoothstep(0.3, 1.0, fw / max(2.0 * h / max(m, 1e-4), 1e-4)));
}
// same but never thinner than k pixels (graphic marks that must stay visible)
float trait(float d, float h, float fw, float k){ float he = max(h, 0.5 * k * fw); return boite(d, -he, he, fw); }

vec3 parcelle(float h, float k, float labour){
  // November polder (sRGB): wet pasture greens, young winter wheat, ploughed clay, pale stubble
  if (h < labour) {
    if (k < 0.45) return mix(vec3(0.40, 0.33, 0.25), vec3(0.33, 0.27, 0.21), k / 0.45);
    if (k < 0.72) return vec3(0.52, 0.48, 0.35);
    return vec3(0.40, 0.47, 0.27);
  }
  vec3 a = vec3(0.38, 0.45, 0.26); vec3 b = vec3(0.45, 0.50, 0.30); vec3 c = vec3(0.32, 0.40, 0.23);
  return k < 0.5 ? mix(a, b, k * 2.0) : mix(b, c, (k - 0.5) * 2.0);
}
// filtered parcel colour in strip coordinates l (metres) with strip size sz
vec3 parcellesFiltrees(vec2 l, vec2 sz, vec2 fwl, float labour, vec2 bloc, float s, vec3 moy){
  vec2 q = l / sz; vec2 wq = fwl / sz;
  vec2 i = floor(q); vec2 f = q - i;
  vec2 dir = vec2(f.x < 0.5 ? -1.0 : 1.0, f.y < 0.5 ? -1.0 : 1.0);
  vec2 dd = min(f, 1.0 - f);
  vec2 a = clamp((0.5 * wq - dd) / max(wq, vec2(1e-5)), 0.0, 0.5);
  vec2 o = bloc * 517.0;
  vec3 c00 = parcelle(hf(i + o, s), hf(i + o, s + 1.0), labour);
  vec3 c10 = parcelle(hf(i + vec2(dir.x, 0.0) + o, s), hf(i + vec2(dir.x, 0.0) + o, s + 1.0), labour);
  vec3 c01 = parcelle(hf(i + vec2(0.0, dir.y) + o, s), hf(i + vec2(0.0, dir.y) + o, s + 1.0), labour);
  vec3 c11 = parcelle(hf(i + dir + o, s), hf(i + dir + o, s + 1.0), labour);
  vec3 c = c00 * (1.0 - a.x) * (1.0 - a.y) + c10 * a.x * (1.0 - a.y) + c01 * (1.0 - a.x) * a.y + c11 * a.x * a.y;
  return mix(c, moy, smoothstep(0.35, 0.9, max(wq.x, wq.y)));
}

// ---------------------------------------------------------------------------------------------
// Polder far field (both sites)
// ---------------------------------------------------------------------------------------------
void polder(vec2 p, float fw){
  vec2 q = p + (vec2(vn(p / 900.0, 1.0), vn(p / 900.0, 2.0)) - 0.5) * 300.0;
  vec2 tb = vec2(2400.0, 1700.0);
  vec2 bc = floor(q / tb); vec2 bf = fract(q / tb);
  float hb = hf(bc, 3.0); float hb2 = hf(bc, 4.0); float hb3 = hf(bc, 5.0);
  float ang = hb < 0.55 ? 0.0 : (hb < 0.9 ? 1.5708 : (hb - 0.9) * 3.0 - 0.15);
  float ca = cos(ang); float sa = sin(ang);
  vec2 l = vec2(ca * p.x - sa * p.y, sa * p.x + ca * p.y);
  vec2 fwl = vec2(fw);
  float sW = 70.0 + 60.0 * hb2;
  float sL = 260.0 + 420.0 * hb3;
  float labour = hb2 < 0.55 ? 0.15 : 0.55;
  vec3 moy = mix(vec3(0.39, 0.45, 0.27), vec3(0.42, 0.42, 0.30), labour) * (0.94 + 0.12 * hb3);
  // stagger strip ends per strip
  float iu = floor(l.x / sW);
  vec2 lv = vec2(l.x, l.y + hf(vec2(iu, bc.x * 31.0 + bc.y), 6.0) * sL);
  vec3 col = mix(parcellesFiltrees(lv, vec2(sW, sL), fwl, labour, bc, 7.0, moy), moy, 0.35);
  // within-field texture: tractor lines, wet patches; octaves fade with distance
  float ph = hf(floor(lv / vec2(sW, sL)) + bc * 517.0, 7.0);
  col *= 0.90 + 0.2 * vnf(p, 1.0 / 35.0, 9.0 + ph * 10.0, fw);
  col *= 0.94 + 0.12 * vnf(p, 1.0 / 7.0, 10.0, fw);
  if (ph < labour) col *= 1.0 + 0.10 * (1.0 - smoothstep(0.08, 0.3, fw)) * sin(l.y * 6.2832 / 0.7);
  else col *= 0.97 + 0.06 * (1.0 - smoothstep(0.6, 1.6, fw)) * sin(l.x * 6.2832 / 3.0);
  float rough = 0.9;
  // ditches between strips and at strip ends (water: sky reflection)
  float d1 = (0.5 - abs(fract(lv.x / sW) - 0.5)) * sW;
  float d2 = (0.5 - abs(fract(lv.y / sL) - 0.5)) * sL;
  float fosse = max(bande(d1, 1.1, fw, 2.2 / sW), bande(d2, 0.8, fw, 1.6 / sL));
  float berge = max(bande(d1, 2.4, fw, 4.8 / sW), bande(d2, 1.8, fw, 3.6 / sL)) * (1.0 - fosse);
  // block borders: canals, roads, tree rows
  float dBx = hf(vec2(floor(q.x / tb.x + 0.5), bc.y), 15.0) < 0.6 ? min(bf.x, 1.0 - bf.x) * tb.x : 1e5;
  float dBy = hf(vec2(bc.x, floor(q.y / tb.y + 0.5)), 16.0) < 0.6 ? min(bf.y, 1.0 - bf.y) * tb.y : 1e5;
  float dB = min(dBx, dBy);
  float canal = bande(dB, 7.0, fw, 0.0);
  float route = hb3 > 0.45 ? bande(abs(dB - 22.0), 3.0, fw, 0.0) : 0.0;
  float arbre = bande(abs(dB - 30.0), 5.0, fw, 0.0) * smoothstep(0.35, 0.55, vn(p / 18.0, 40.0) * 0.6 + 0.4 * step(0.5, hb3));
  // farms: yard, roofs, ring of trees
  vec2 fc = floor(p / 1400.0);
  vec2 fcen = (fc + 0.2 + 0.6 * vec2(hf(fc, 11.0), hf(fc, 12.0))) * 1400.0;
  float ferme = 0.0;
  if (hf(fc, 13.0) < 0.65) {
    vec2 r = p - fcen; float fa = (hf(fc, 14.0) < 0.5 ? 0.0 : 1.5708) + ang;
    vec2 rr = vec2(cos(fa) * r.x - sin(fa) * r.y, sin(fa) * r.x + cos(fa) * r.y);
    float dr = length(r);
    float cour = bande(dr, 70.0, fw, 0.0);
    float toit1 = rect(rr, vec2(-30.0, -10.0), vec2(30.0, 10.0), fwl);
    float toit2 = rect(rr, vec2(-14.0, 22.0), vec2(8.0, 34.0), fwl);
    float haie = bande(abs(dr - 82.0), 9.0, fw, 0.0) * step(0.35, vn(vec2(atan(r.y, r.x) * 7.0, 0.0), 41.0));
    vec3 fcol = mix(vec3(0.46, 0.45, 0.41), vec3(0.42, 0.24, 0.18), toit1);
    fcol = mix(fcol, vec3(0.30, 0.31, 0.33), toit2);
    ferme = cour;
    col = mix(col, fcol, cour);
    col = mix(col, vec3(0.19, 0.22, 0.12), haie * 0.5);
    rough = mix(rough, 0.75, cour);
  }
  col = mix(col, col * 0.82 + vec3(0.02, 0.03, 0.0), berge * (1.0 - ferme));
  col = mix(col, vec3(0.05, 0.065, 0.07), fosse * (1.0 - ferme));
  float eau = fosse * (1.0 - ferme);
  col = mix(col, vec3(0.05, 0.065, 0.07), canal); eau = max(eau, canal);
  col = mix(col, vec3(0.40, 0.40, 0.39), route);
  col = mix(col, vec3(0.22, 0.23, 0.14), arbre);
  // villages: roofs and streets inside a noisy disc
  vec2 tc = floor(p / 9000.0);
  vec2 tcen = (tc + 0.25 + 0.5 * vec2(hf(tc, 21.0), hf(tc, 22.0))) * 9000.0;
  if (hf(tc, 23.0) < 0.55) {
    float R = 600.0 + 1300.0 * hf(tc, 24.0);
    float dt = length(p - tcen) + (fbm(p / 1500.0, 25.0) - 0.5) * 700.0;
    float tm = 1.0 - smoothstep(R - 160.0, R, dt);
    if (tm > 0.0) {
      vec2 cq = p / 26.0;
      float hc = hf(floor(cq), 26.0);
      vec3 toit = hc < 0.45 ? vec3(0.53, 0.32, 0.22) : (hc < 0.75 ? vec3(0.35, 0.34, 0.33) : vec3(0.45, 0.29, 0.21));
      vec2 cf = fract(cq);
      float rue = 1.0 - rect(cf * 26.0, vec2(3.0), vec2(23.0), fwl);
      vec3 tcol = mix(toit * (0.85 + 0.3 * hf(floor(cq * 3.0), 27.0)), vec3(0.43, 0.43, 0.41), rue);
      vec3 tmoy = vec3(0.40, 0.37, 0.33);
      tcol = mix(tcol, tmoy, smoothstep(0.08, 0.35, fw / 26.0));
      col = mix(col, tcol, tm); rough = mix(rough, 0.78, tm); eau *= 1.0 - tm;
    }
  }
  gAlb = col; gRough = mix(rough, 0.05, eau); gEau = eau;
  gHerbe = (1.0 - eau) * (1.0 - ferme) * (1.0 - route) * step(labour, ph) * 0.0; // far field: no blades
}

// close-range grass colour (sRGB), mown lawn or pasture, with blade-scale grain
vec3 herbeProche(vec2 p, float fw, float tondu){
  vec3 base = mix(vec3(0.42, 0.50, 0.27), vec3(0.46, 0.54, 0.30), tondu);
  base *= 0.88 + 0.24 * vnf(p, 1.0 / 3.0, 32.0, fw);
  base = mix(base, vec3(0.50, 0.47, 0.30), 0.35 * smoothstep(0.55, 0.8, vnf(p, 1.0 / 1.7, 33.0, fw))); // straw
  base *= 0.85 + 0.3 * vnf(p, 14.0, 34.0, fw) * vnf(p, 41.0, 35.0, fw) * 1.4;
  // mowing stripes on lawns
  // (faded out before the 1.6 m period nears the pixel footprint: no moire bands in the distance)
  float ampT = 0.03 * (1.0 - smoothstep(0.05, 0.2, fw / 1.6)) * (0.5 + vnf(p, 1.0 / 23.0, 36.0, fw));
  base *= 1.0 + tondu * ampT * (boite(mod(p.x, 1.6), 0.0, 0.8, fw) * 2.0 - 1.0);
  return base;
}

// ---------------------------------------------------------------------------------------------
// Site 0: the launch field (origin = launch point; ditch, gravel path, concrete pad)
// ---------------------------------------------------------------------------------------------
void siteLacher(vec2 p, float fw, float y){
  vec2 fwl = vec2(fw);
  float bord = 1.0 - rect(p, vec2(-260.0, -140.0), vec2(320.0, 260.0), vec2(fw) + 30.0);
  // pasture and lawn
  float tondu = boite(p.y, -120.0, CHEMIN_Z0 + 0.0, fw + 4.0);
  vec3 h = herbeProche(p, fw, tondu);
  gAlb = mix(h, gAlb, bord); gRough = mix(0.92, gRough, bord); gEau *= bord;
  gHerbe = 1.0 - bord;
  // concrete launch pad 3 x 3 m
  float dalle = rect(p, vec2(-1.5), vec2(1.5), fwl);
  vec3 beton = vec3(0.56, 0.56, 0.53) * (0.9 + 0.2 * vnf(p, 3.0, 50.0, fw)) * (1.0 - 0.25 * trait(abs(p.x), 0.008, fw, 0.0));
  gAlb = mix(gAlb, beton, dalle); gRough = mix(gRough, 0.82, dalle); gHerbe *= 1.0 - dalle;
  // gravel path with ragged edges
  float ond = (vnf(p, 0.7, 51.0, fw) - 0.5) * 0.35;
  float chemin = boite(p.y + ond, CHEMIN_Z0, CHEMIN_Z1, fw) * boite(p.x, -240.0, 300.0, fw);
  float g1 = vnf(p, 38.0, 52.0, fw); float g2 = vnf(p, 95.0, 53.0, fw);
  vec3 gravier = vec3(0.60, 0.57, 0.51) * (0.78 + 0.3 * g1 + 0.2 * g2);
  gravier = mix(gravier, vec3(0.45, 0.43, 0.39), 0.4 * smoothstep(0.45, 0.6, vnf(p, 2.5, 54.0, fw))); // wheel tracks
  gAlb = mix(gAlb, gravier, chemin); gRough = mix(gRough, 0.95, chemin); gHerbe *= 1.0 - chemin;
  // the ditch: far field draws it as a band, the 3D patch digs it (y < 0)
  float dz = abs(p.y - FOSSE_Z0);
  float fosse = bande(dz, 1.6, fw, -1.0) * boite(p.x, -400.0, 400.0, fw);
  float mouille = smoothstep(-0.05, -0.5, y);
  vec3 berge = mix(vec3(0.30, 0.33, 0.18), vec3(0.17, 0.15, 0.11), mouille) * (0.85 + 0.3 * vnf(p, 6.0, 55.0, fw));
  gAlb = mix(gAlb, berge, fosse * 0.85);
  gEau = max(gEau, bande(dz, 0.9, fw, -1.0) * boite(p.x, -400.0, 400.0, fw) * step(-0.01, y) );
  gHerbe *= 1.0 - bande(dz, 2.3, fw, -1.0);
  gRough = mix(gRough, 0.6, mouille);
}

// ---------------------------------------------------------------------------------------------
// Site 1: runway 09 (origin = threshold on the centreline)
// ---------------------------------------------------------------------------------------------
float marquesPiste(vec2 p, float fw){
  vec2 w = vec2(fw);
  float m = 0.0;
  float az = abs(p.y);
  // threshold bars: 12 bars 1.8 m wide, 30 m long, from 6 m
  if (p.x > 5.0 && p.x < 37.0) {
    m += boite(p.x, 6.0, 36.0, fw) * boite(az, 1.8, 21.6, fw) * (az < 1.8 + 3.6 * 6.0 ? tirets(az - 1.8, 3.6, 0.0, 1.8, fw) : 0.0);
  }
  // centreline dashes 30 m / gap 20 m, 0.9 m wide, from 70 m
  m += boite(p.x, 70.0, ${(PISTE_L - 70).toFixed(1)}, fw) * boite(p.y, -0.45, 0.45, fw) * tirets(p.x - 70.0, 50.0, 0.0, 30.0, fw);
  // edge lines 0.9 m
  m += boite(p.x, 0.0, ${PISTE_L.toFixed(1)}, fw) * boite(az, 21.3, 22.2, fw);
  // aiming point: 45 x 6 m from 400 m, inner edge 9 m from the centreline
  m += rect(vec2(p.x, az), vec2(400.0, 9.0), vec2(445.0, 15.0), w);
  // touchdown zone: pairs of bars 22.5 x 1.8 m, 1.5 m apart
  for (int k = 0; k < 5; k++) {
    float x0 = k == 0 ? 150.0 : (k == 1 ? 300.0 : (k == 2 ? 600.0 : (k == 3 ? 750.0 : 900.0)));
    float nb = k == 0 ? 3.0 : (k < 3 ? 2.0 : 1.0);
    m += boite(p.x, x0, x0 + 22.5, fw) * boite(az, 9.0, 9.0 + nb * 3.3 - 1.5, fw) * tirets(az - 9.0, 3.3, 0.0, 1.8, fw);
  }
  return clamp(m, 0.0, 1.0);
}
void sitePiste(vec2 p, float fw){
  vec2 fwl = vec2(fw);
  float az = abs(p.y);
  // runway strip: mown grass
  float bande = rect(p, vec2(-960.0, -80.0), vec2(${(PISTE_L + 80).toFixed(1)}, 80.0), fwl + 8.0);
  vec3 h = herbeProche(p, fw, 1.0);
  gAlb = mix(gAlb, h, bande); gRough = mix(gRough, 0.92, bande); gEau *= 1.0 - bande;
  gHerbe = bande;
  // asphalt with shoulders
  float epaule = rect(p, vec2(-3.0, -24.0), vec2(${(PISTE_L + 3).toFixed(1)}, 24.0), fwl);
  float asph = rect(p, vec2(0.0, -22.5), vec2(${PISTE_L.toFixed(1)}, 22.5), fwl);
  float g1 = vnf(p, 60.0, 60.0, fw); float g2 = vnf(p, 180.0, 61.0, fw);
  vec3 a = vec3(0.24, 0.24, 0.235) * (0.86 + 0.22 * g1 + 0.12 * g2);
  a *= 0.92 + 0.16 * vnf(p * vec2(0.08, 1.0), 0.5, 62.0, fw);   // paving lanes
  a *= 0.93 + 0.14 * vnf(p, 1.0 / 9.0, 63.0, fw);
  // crack sealing lines
  float fis = trait(abs(p.y - 7.5 * floor(p.y / 7.5 + 0.5)), 0.02, fw, 0.0) * 0.5 + trait(abs(mod(p.x, 37.0) - 18.5), 0.02, fw, 0.0) * 0.35;
  a = mix(a, vec3(0.08), fis * (1.0 - smoothstep(0.02, 0.08, fw)));
  // rubber in the touchdown zone, along the wheel tracks
  float rz = smoothstep(120.0, 230.0, p.x) * (1.0 - smoothstep(520.0, 820.0, p.x));
  float trace = exp(-pow((az - 1.3) / 1.6, 2.0)) * 0.8 + exp(-pow(az / 4.5, 2.0)) * 0.35;
  float strie = 0.55 + 0.45 * vnf(vec2(p.x * 0.03, p.y * 2.2), 1.0, 64.0, fw);
  float caout = clamp(rz * trace * strie * (0.7 + 0.6 * vnf(p, 1.0 / 25.0, 65.0, fw)), 0.0, 0.85);
  a = mix(a, vec3(0.045, 0.045, 0.045), caout);
  vec3 epc = vec3(0.36, 0.36, 0.33) * (0.9 + 0.2 * g1);
  gAlb = mix(gAlb, epc, epaule); gRough = mix(gRough, 0.88, epaule); gHerbe *= 1.0 - epaule;
  gAlb = mix(gAlb, a, asph); gRough = mix(gRough, mix(0.72, 0.42, caout), asph); // worn asphalt: grazing sheen
  // white paint: markings, then the designator digits from the texture
  float m = marquesPiste(p, fw);
  vec2 uvc = vec2((p.y + 6.0) / 12.0, (57.0 - p.x) / 9.0);
  if (uvc.x > 0.0 && uvc.x < 1.0 && uvc.y > 0.0 && uvc.y < 1.0) m = max(m, texture2D(uChiffres, vec2(uvc.x, 1.0 - uvc.y)).r);
  m *= asph * (1.0 - 0.55 * caout);
  vec3 peinture = vec3(0.80, 0.80, 0.78) * (0.92 + 0.08 * g2);
  gAlb = mix(gAlb, peinture, m); gRough = mix(gRough, 0.62, m); gMarque = m;
}

// ---------------------------------------------------------------------------------------------
// Entry point: fills gAlb (sRGB), gRough, gEau; y = world height (the dug ditch is below 0)
// ---------------------------------------------------------------------------------------------
void sol(vec3 pw){
  vec2 p = pw.xz;
  vec2 g = fwidth(p); float fw = max(max(g.x, g.y), 1e-5);
  gMarque = 0.0;
  polder(p + uSite.yz, fw);
  vec2 dc = p - uOeil.xz;
  float yc = pw.y + dot(dc, dc) / 12742000.0; // remove the Earth's curvature
  if (uSite.x < 0.5) siteLacher(p, fw, yc); else sitePiste(p, fw);
  // cloud shadows: the coverage the sun crosses on its way down, carried by the wind
  vec2 dS = uSoleil.xz / max(uSoleil.y, 0.05);
  float c1 = couvNuage(p + dS * uCouches.x - uOmbreN.xy, uOmbreN.z, 31.0);
  float c2 = couvNuage(p + dS * uCouches.y - uOmbreN.xy, uOmbreN.w, 47.0);
  float ombre = 1.0 - 0.55 * uCouches.z * (1.0 - (1.0 - 0.6 * c1) * (1.0 - 0.75 * c2));
  gAlb *= ombre;
}

${GLSL_HERBE_ICI}
`.replace(/CHEMIN_Z0/g, CHEMIN_Z[0].toFixed(2)).replace(/CHEMIN_Z1/g, CHEMIN_Z[1].toFixed(2)).replace(/FOSSE_Z0/g, FOSSE_Z.toFixed(2));

/** Fragment code after the PBR albedo block: ground albedo, roughness, water, graphic marks. */
export const GLSL_SOL_ALBEDO = `
  if (uTrou.x < uTrou.z && vPositionW.x > uTrou.x && vPositionW.x < uTrou.z && vPositionW.z > uTrou.y && vPositionW.z < uTrou.w) discard;
  sol(vPositionW);
  surfaceAlbedo = pow(gAlb, vec3(2.2));
  // micro relief: tilt the normal with the same filtered noise (grass clumps, gravel, asphalt grain)
  {
    vec2 p = vPositionW.xz; vec2 g = fwidth(p); float fw = max(max(g.x, g.y), 1e-5);
    float k = (1.0 - smoothstep(0.01, 0.06, fw)) * (1.0 - gEau);
    vec2 dn = vec2(vnf(p, 9.0, 80.0, fw) - 0.5, vnf(p + 3.1, 9.0, 81.0, fw) - 0.5) * 0.35 * k;
    normalW = normalize(normalW + vec3(dn.x, 0.0, dn.y));
  }
`;

/** Fragment code before the fog: water reflection and the drawn lines (violet drift, grey route). */
export const GLSL_SOL_FINAL = `
  {
    vec3 vv = normalize(vPositionW - vEyePosition.xyz);
    float fr = 0.02 + 0.98 * pow(1.0 - abs(vv.y), 5.0);
    vec3 rfl = reflect(vv, vec3(0.0, 1.0, 0.0));
    vec3 env = vec3(0.0);
    #ifdef REFLECTIONMAP_3D
    env = textureCube(reflectionSampler, vec3(rfl.x, rfl.y, -rfl.z)).rgb;
    #endif
    finalColor.rgb = mix(finalColor.rgb, env * 0.9, gEau * fr * 0.9);
    vec2 p = vPositionW.xz; vec2 g = fwidth(p); float fw = max(max(g.x, g.y), 1e-5);
    // violet line: ground track of the balloon, from the launch point to below it
    float lv = 0.0;
    if (uTrait.w > 0.0) {
      vec2 b = uTrait.xy; float L2 = max(dot(b, b), 1e-6);
      float u = clamp(dot(p, b) / L2, 0.0, 1.0);
      float d = length(p - b * u);
      lv = trait(d, 0.0, fw, uTrait.z) * uTrait.w * (dot(b, b) > 1.0 ? 1.0 : 0.0);
      finalColor.rgb = mix(finalColor.rgb, uTraitCol.rgb, lv);
    }
    // grey line: straight toward the runway, due east from the start
    float lg = 0.0;
    if (uRoute.w > 0.0) {
      lg = trait(abs(p.y - uRoute.y), 0.0, fw, uRoute.z) * step(uRoute.x, p.x) * uRoute.w;
      finalColor.rgb = mix(finalColor.rgb, uRouteCol.rgb, lg);
    }
    finalColor.a = 1.0 - 0.8 * lv;
  }
`;
