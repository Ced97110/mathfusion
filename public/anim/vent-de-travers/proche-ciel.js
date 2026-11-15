// Copyright: Your Name. Apache 2.0
// « Vent de travers » v2 — PROCHE scene, sky side: real sun, sky dome, image-based light taken from
// that same sky, and the atmosphere post-process (height fog, the two humid cloud layers of the
// sounding, light shafts). Units: 1 = 1 metre, +x east, -z north, +y up.
// Everything here is a pure function of the values passed in by proche.js (themselves pure in t).

const B = globalThis.BABYLON;
const rad = (d) => (d * Math.PI) / 180;

// ---------------------------------------------------------------------------------------------
// Sun (NOAA solar calculator: declination + equation of time).
// De Bilt 52.100 N, 5.177 E, 2026-11-12:
//   12:00 UTC  declination -17.77°, equation of time +15.90 min, elevation 19.68°, azimuth 189.26°
//              (9.3° west of south: just past local solar noon, which is at 11:23 UTC);
//   13:00 UTC  elevation 17.02°, azimuth 204.04°.
// ---------------------------------------------------------------------------------------------
export const LAT = 52.1;
export const LON = 5.177;
export const MIDI_UTC = Date.UTC(2026, 10, 12, 12, 0, 0);

export function positionSoleil(latDeg, lonDeg, msUtc) {
  const jd = msUtc / 86400000 + 2440587.5;
  const T = (jd - 2451545) / 36525;
  const L0 = (280.46646 + T * (36000.76983 + 0.0003032 * T)) % 360;
  const M = 357.52911 + T * (35999.05029 - 0.0001537 * T);
  const ex = 0.016708634 - T * (0.000042037 + 1.267e-7 * T);
  const C = Math.sin(rad(M)) * (1.914602 - T * (0.004817 + 0.000014 * T))
    + Math.sin(rad(2 * M)) * (0.019993 - 0.000101 * T) + Math.sin(rad(3 * M)) * 0.000289;
  const om = 125.04 - 1934.136 * T;
  const lam = L0 + C - 0.00569 - 0.00478 * Math.sin(rad(om));
  const eps0 = 23 + (26 + (21.448 - T * (46.815 + T * (0.00059 - T * 0.001813))) / 60) / 60;
  const eps = eps0 + 0.00256 * Math.cos(rad(om));
  const dec = Math.asin(Math.sin(rad(eps)) * Math.sin(rad(lam)));
  const y = Math.tan(rad(eps / 2)) ** 2;
  const eqt = 4 * (180 / Math.PI) * (y * Math.sin(2 * rad(L0)) - 2 * ex * Math.sin(rad(M))
    + 4 * ex * y * Math.sin(rad(M)) * Math.cos(2 * rad(L0)) - 0.5 * y * y * Math.sin(4 * rad(L0))
    - 1.25 * ex * ex * Math.sin(2 * rad(M)));
  const minutes = ((msUtc / 60000) % 1440 + 1440) % 1440;
  const ha = rad((minutes + eqt + 4 * lonDeg) / 4 - 180);
  const lat = rad(latDeg);
  const cz = Math.sin(lat) * Math.sin(dec) + Math.cos(lat) * Math.cos(dec) * Math.cos(ha);
  const z = Math.acos(cz);
  let az = Math.acos((Math.sin(lat) * cz - Math.sin(dec)) / (Math.cos(lat) * Math.sin(z))) * 180 / Math.PI;
  az = ha > 0 ? (az + 180) % 360 : (540 - az) % 360;
  return { elevation: 90 - z * 180 / Math.PI, azimut: az };
}

/** Unit vector toward the sun, `heures` hours after 12:00 UTC (scene axes). */
export function versSoleil(heures) {
  const p = positionSoleil(LAT, LON, MIDI_UTC + heures * 3600e3);
  const el = rad(p.elevation);
  const az = rad(p.azimut);
  return { v: new B.Vector3(Math.sin(az) * Math.cos(el), Math.sin(el), -Math.cos(az) * Math.cos(el)), ...p };
}

/** Warm colour of a low sun (linear), from its elevation in degrees. */
export function couleurSoleil(elevationDeg) {
  const k = Math.min(1, Math.max(0, (elevationDeg - 5) / 40));
  return new B.Color3(1.0, 0.80 + 0.12 * k, 0.60 + 0.22 * k);
}

// Sky radiance model, shared by the dome shader (GLSL) and the irradiance harmonics (JS).
const ZENITH = [0.066, 0.138, 0.32];
const HORIZON = [0.47, 0.515, 0.575];
const SOL_REBOND = [0.16, 0.165, 0.13];
const MIE_G = 0.78;
const MIE_K = 0.30;

function cielJS(d, s, sc) {
  const hp = Math.max(d.y, 0);
  const k = Math.pow(1 - hp, 5);
  const c = [0, 1, 2].map((i) => ZENITH[i] + (HORIZON[i] - ZENITH[i]) * k);
  const mu = d.x * s.x + d.y * s.y + d.z * s.z;
  const g = MIE_G;
  const hg = (1 - g * g) / (4 * Math.PI * Math.pow(1 + g * g - 2 * g * mu, 1.5));
  const a = hg * MIE_K * (0.35 + 0.65 * k) + 0.06 * Math.pow(Math.max(mu, 0), 3) * k;
  const sol = [sc.r, sc.g, sc.b];
  for (let i = 0; i < 3; i++) c[i] += sol[i] * a;
  if (d.y < 0) {
    const m = Math.min(1, -d.y / 0.25);
    const mm = m * m * (3 - 2 * m);
    for (let i = 0; i < 3; i++) c[i] += (SOL_REBOND[i] - c[i]) * mm;
  }
  return c;
}

const v3 = (a) => `vec3(${a.map((x) => x.toFixed(4)).join(', ')})`;

/** GLSL noise shared by sky, clouds, ground and grass (WebGL2: uint hashing). */
export const GLSL_BRUIT = `
uint hsh(uvec2 v){
  v = v * 1664525u + 1013904223u;
  v.x += v.y * 1664525u; v.y += v.x * 1664525u;
  v = v ^ (v >> 16u);
  v.x += v.y * 1664525u; v.y += v.x * 1664525u;
  v = v ^ (v >> 16u);
  return v.x;
}
float hf(vec2 c, float s){
  uvec2 u = uvec2(ivec2(floor(c)) + ivec2(1048576));
  u.x += uint(s) * 374761u;
  return float(hsh(u) & 0xffffffu) / 16777216.0;
}
float hf3(vec3 c, float s){ return hf(c.xy + vec2(c.z * 157.0, c.z * 311.0), s); }
float vn(vec2 p, float s){
  vec2 i = floor(p); vec2 f = fract(p); f = f * f * (3.0 - 2.0 * f);
  return mix(mix(hf(i, s), hf(i + vec2(1.0, 0.0), s), f.x),
             mix(hf(i + vec2(0.0, 1.0), s), hf(i + vec2(1.0, 1.0), s), f.x), f.y);
}
float vn3(vec3 p, float s){
  vec3 i = floor(p); vec3 f = fract(p); f = f * f * (3.0 - 2.0 * f);
  float a = mix(mix(hf3(i, s), hf3(i + vec3(1,0,0), s), f.x), mix(hf3(i + vec3(0,1,0), s), hf3(i + vec3(1,1,0), s), f.x), f.y);
  float b = mix(mix(hf3(i + vec3(0,0,1), s), hf3(i + vec3(1,0,1), s), f.x), mix(hf3(i + vec3(0,1,1), s), hf3(i + vec3(1,1,1), s), f.x), f.y);
  return mix(a, b, f.z);
}
float fbm(vec2 p, float s){
  float a = 0.5; float r = 0.0;
  for (int k = 0; k < 4; k++){ r += a * vn(p, s + float(k)); p = p * 2.03 + vec2(1.7, 9.2); a *= 0.5; }
  return r / 0.9375;
}
// value noise whose contrast fades before it aliases: fw = metres per pixel, fq = cycles per metre
float vnf(vec2 p, float fq, float s, float fw){
  return mix(vn(p * fq, s), 0.5, smoothstep(0.2, 0.55, fw * fq));
}
`;

/** Cloud coverage, shared by the clouds (post-process) and their shadows on the ground. */
export const GLSL_COUVERTURE = `
float couvNuage(vec2 p, float seuil, float graine){
  float n = fbm(p * (1.0 / 2300.0), graine) * 0.64 + fbm(p * (1.0 / 610.0), graine + 5.0) * 0.36;
  return smoothstep(seuil, seuil + 0.17, n);
}
`;

const CIEL_VS = `precision highp float;
attribute vec3 position;
uniform mat4 worldViewProjection;
varying vec3 vDir;
void main(void){
  vDir = position;
  gl_Position = worldViewProjection * vec4(position, 1.0);
}`;

const CIEL_FS = `precision highp float;
varying vec3 vDir;
uniform vec3 uSun;
uniform vec3 uSunCol;
uniform vec4 uOpt;   // x = sun disc on, y = haze on (reflection probe only), z = haze amount
${GLSL_BRUIT}
vec3 cielBase(vec3 d){
  float hp = max(d.y, 0.0);
  float k = pow(1.0 - hp, 5.0);
  vec3 c = mix(${v3(ZENITH)}, ${v3(HORIZON)}, k);
  float mu = dot(d, uSun);
  float g = ${MIE_G.toFixed(3)};
  float hg = (1.0 - g * g) / (12.566371 * pow(1.0 + g * g - 2.0 * g * mu, 1.5));
  c += uSunCol * (hg * ${MIE_K.toFixed(3)} * (0.35 + 0.65 * k) + 0.06 * pow(max(mu, 0.0), 3.0) * k);
  if (d.y < 0.0) c = mix(c, ${v3(SOL_REBOND)}, smoothstep(0.0, 0.25, -d.y));
  return c;
}
void main(void){
  vec3 d = normalize(vDir);
  vec3 c = cielBase(d);
  float mu = dot(d, uSun);
  // faint high veil (cirrostratus) so the sky is not an empty gradient
  if (d.y > 0.0) {
    vec2 sp = d.xz / (d.y + 0.08);
    float n = fbm(sp * vec2(0.9, 2.6) + vec2(4.0, 1.0), 70.0);
    float v = smoothstep(0.52, 0.8, n) * smoothstep(0.03, 0.25, d.y) * 0.22;
    c = mix(c, vec3(0.8, 0.82, 0.86) + uSunCol * 0.25 * pow(max(mu, 0.0), 4.0), v);
  }
  // sun disc with limb darkening (0.53 degrees wide), HDR
  float r = acos(clamp(mu, -1.0, 1.0)) / 0.00465;
  float disc = (1.0 - smoothstep(0.86, 1.0, r)) * (0.6 + 0.4 * sqrt(max(1.0 - r * r, 0.0)));
  c += uSunCol * disc * 260.0 * uOpt.x;
  // the probe sees the haze the post-process adds to the main view
  c = mix(c, ${v3(HORIZON)} * 0.95 + uSunCol * 0.08 * pow(max(mu, 0.0), 6.0), uOpt.y * uOpt.z * pow(1.0 - abs(d.y), 9.0));
  gl_FragColor = vec4(c, 1.0);
}`;

// ---------------------------------------------------------------------------------------------
// Atmosphere post-process: reads the HDR scene and the linear depth, adds height fog with sun
// in-scattering, ray-marches the two measured cloud layers, and adds light shafts.
// Scene alpha = fog weight (1 everywhere except graphic markers drawn on the ground).
// ---------------------------------------------------------------------------------------------
const ATMO_FS = `precision highp float;
varying vec2 vUV;
uniform sampler2D textureSampler;
uniform sampler2D depthSampler;
uniform mat4 uInvVP;
uniform vec3 uEye;
uniform vec3 uFwd;
uniform vec2 uNF;
uniform vec3 uSun;
uniform vec3 uSunCol;
uniform vec3 uFogCol;
uniform vec3 uZenith;
uniform vec4 uFog;    // x = extinction at sea level (1/m), y = scale height (m), z = sky distance (m), w = sky radius test (m)
uniform vec4 uC1;     // lower layer: base, top, coverage threshold, opacity
uniform vec4 uC2;     // upper layer
uniform vec4 uAir;    // xy = air displacement since the start (m), z = steps, w = light samples
uniform vec4 uRay;    // xy = sun position (uv), z = strength, w = aspect
uniform float uGraine; // jitter offset, a pure function of the (sub-)frame time: offline sub-frames average it
${GLSL_BRUIT}
${GLSL_COUVERTURE}
float profondeurOptique(vec3 ro, vec3 rd, float t){
  float k = rd.y * t / uFog.y;
  float f = abs(k) < 1e-3 ? 1.0 - 0.5 * k : (1.0 - exp(-k)) / k;
  return uFog.x * exp(-ro.y / uFog.y) * t * f;
}
vec3 diffusion(vec3 rd){
  float mu = dot(rd, uSun);
  float g = 0.62;
  float hg = (1.0 - g * g) / (12.566371 * pow(1.0 + g * g - 2.0 * g * mu, 1.5));
  return uFogCol + uSunCol * hg * 0.55;
}
float densite(vec3 p, vec4 C, float graine, float lod){
  float th = C.y - C.x;
  float h = (p.y - C.x) / th;
  if (h <= 0.0 || h >= 1.0) return 0.0;
  vec2 q = p.xz - uAir.xy;
  float c = couvNuage(q, C.z, graine);
  if (c <= 0.0) return 0.0;
  // flat base (condensation level), domed tops: the denser the cell, the higher it rises
  float sommet = 0.3 + 0.7 * c;
  float prof = smoothstep(0.0, 0.07, h) * (1.0 - smoothstep(0.55 * sommet, sommet, h));
  if (prof <= 0.0) return 0.0;
  vec3 r = vec3(q.x, p.y, q.y);
  float det = vn3(r * (1.0 / 140.0), graine + 20.0) * 0.6 + vn3(r * (1.0 / 47.0), graine + 21.0) * 0.4;
  // detail finer than the march step would only add speckle: fade it to its mean
  det = mix(0.5, det, lod);
  // erosion grows with height: billowing tops, solid bases
  return clamp(c * prof * 1.8 - det * (0.6 + 0.8 * h), 0.0, 1.0);
}
vec4 couche(vec3 ro, vec3 rd, float tMax, vec4 C, float graine, inout float tPoids){
  if (C.w <= 0.0) return vec4(0.0);
  float t0; float t1;
  if (abs(rd.y) < 1e-5) {
    if (ro.y < C.x || ro.y > C.y) return vec4(0.0);
    t0 = 0.0; t1 = tMax;
  } else {
    float ta = (C.x - ro.y) / rd.y; float tb = (C.y - ro.y) / rd.y;
    t0 = max(min(ta, tb), 0.0); t1 = min(max(ta, tb), tMax);
  }
  t1 = min(t1, t0 + 9000.0);
  if (t1 <= t0) return vec4(0.0);
  int N = int(uAir.z);
  float dt = (t1 - t0) / float(N);
  // interleaved gradient noise: a fixed low-discrepancy dither (no white speckle); offline sub-frames
  // shift it by uGraine and average it out
  float j = fract(52.9829189 * fract(dot(gl_FragCoord.xy, vec2(0.06711056, 0.00583715))) + uGraine);
  float lod = clamp(1.0 - (dt - 30.0) / 170.0, 0.0, 1.0);
  float th = C.y - C.x;
  float mu = dot(rd, uSun);
  float ph = mix((1.0 - 0.36) / (12.566371 * pow(1.36 - 1.2 * mu, 1.5)), (1.0 - 0.09) / (12.566371 * pow(1.09 + 0.6 * mu, 1.5)), 0.3);
  vec3 amb = uZenith * 1.6 + uFogCol * 0.35;
  vec3 acc = vec3(0.0); float T = 1.0;
  float sig = 0.045 * C.w;
  for (int i = 0; i < 96; i++) {
    if (i >= N) break;
    float tt = t0 + (float(i) + j) * dt;
    vec3 p = ro + rd * tt;
    float dn = densite(p, C, graine, lod);
    if (dn > 0.002) {
      float dl = densite(p + uSun * th * 0.5, C, graine, lod);
      if (uAir.w > 1.5) dl = 0.5 * (dl + densite(p + uSun * th * 1.3, C, graine, lod));
      float lum = exp(-dl * sig * th * 3.0);
      float poudre = 1.0 - exp(-dn * 6.0);
      vec3 L = uSunCol * lum * ph * 9.0 * (0.3 + 0.7 * poudre) + amb * (0.55 + 0.45 * (p.y - C.x) / th);
      float Ts = exp(-dn * sig * dt);
      float w = T * (1.0 - Ts);
      // fog between the camera and this sample
      float Tf = exp(-profondeurOptique(ro, rd, tt));
      acc += w * (L * Tf + diffusion(rd) * (1.0 - Tf));
      tPoids += w * tt;
      T *= Ts;
      if (T < 0.01) break;
    }
  }
  return vec4(acc, 1.0 - T);
}
void main(void){
  vec4 sc = texture2D(textureSampler, vUV);
  float m = texture2D(depthSampler, vUV).r;
  vec2 ndc = vUV * 2.0 - 1.0;
  vec4 p0 = uInvVP * vec4(ndc, -1.0, 1.0);
  vec4 p1 = uInvVP * vec4(ndc, 1.0, 1.0);
  vec3 rd = normalize(p1.xyz / p1.w - p0.xyz / p0.w);
  float n = uNF.x; float f = uNF.y;
  float zc = m * (n + f) - n;
  float dv = (zc + 2.0 * f * n / (f - n)) * (f - n) / (f + n);
  float t = dv / max(dot(rd, uFwd), 1e-3);
  bool ciel = t > uFog.w;
  float tf = ciel ? uFog.z : t;
  float w = clamp(sc.a, 0.0, 1.0);
  float Tf = exp(-profondeurOptique(uEye, rd, tf) * w);
  vec3 col = sc.rgb * Tf + diffusion(rd) * (1.0 - Tf);
  // clouds, nearest layer first
  float tMax = ciel ? 1e9 : t;
  float tp = 0.0;
  bool bas = uEye.y < 0.5 * (uC1.y + uC2.x);
  vec4 a = couche(uEye, rd, tMax, bas ? uC1 : uC2, bas ? 31.0 : 47.0, tp);
  vec4 b = couche(uEye, rd, tMax, bas ? uC2 : uC1, bas ? 47.0 : 31.0, tp);
  vec3 nuage = a.rgb + (1.0 - a.a) * b.rgb;
  float an = 1.0 - (1.0 - a.a) * (1.0 - b.a);
  col = col * (1.0 - an) + nuage;
  // light shafts: radial gather of open sky toward the sun
  if (uRay.z > 0.0) {
    vec2 dlt = (uRay.xy - vUV) / 48.0;
    vec2 uv = vUV + dlt * hf(gl_FragCoord.xy, 92.0);
    float acc = 0.0; float dec = 1.0;
    for (int i = 0; i < 48; i++) {
      uv += dlt;
      if (uv.x < 0.0 || uv.y < 0.0 || uv.x > 1.0 || uv.y > 1.0) break;
      float ms = texture2D(depthSampler, uv).r;
      vec2 e = (uv - uRay.xy) * vec2(uRay.w, 1.0);
      acc += step(0.55, ms) * exp(-dot(e, e) * 18.0) * dec;
      dec *= 0.965;
    }
    vec2 e0 = (vUV - uRay.xy) * vec2(uRay.w, 1.0);
    col += uSunCol * acc / 48.0 * uRay.z * (1.0 - an) * exp(-length(e0) * 1.5);
  }
  gl_FragColor = vec4(col, 1.0);
}`;

/**
 * Builds the sky, the sun light, the environment and the atmosphere pass of the PROCHE scene.
 * @param {BABYLON.Scene} scene
 * @param {BABYLON.Camera} camera
 * @param {{ film: boolean, couches: number[][] }} opts couches = [[base, top], [base, top]] in metres
 */
export function creerCiel(scene, camera, opts) {
  const engine = scene.getEngine();
  B.Effect.ShadersStore.vdtProcheCielVertexShader = CIEL_VS;
  B.Effect.ShadersStore.vdtProcheCielFragmentShader = CIEL_FS;
  B.Effect.ShadersStore.vdtProcheAtmoFragmentShader = ATMO_FS;

  // ---- sun light (direction set by maj) --------------------------------------------------
  const soleil = new B.DirectionalLight('soleil', new B.Vector3(0, -1, 0), scene);
  soleil.intensity = 6.0;
  soleil.shadowMinZ = 0;

  // ---- sky dome: follows the camera, radius set per shot -----------------------------------
  const matCiel = new B.ShaderMaterial('ciel', scene, { vertex: 'vdtProcheCiel', fragment: 'vdtProcheCiel' }, {
    attributes: ['position'], uniforms: ['worldViewProjection', 'uSun', 'uSunCol', 'uOpt'],
  });
  matCiel.backFaceCulling = false;
  matCiel.setVector4('uOpt', new B.Vector4(1, 0, 1, 0));
  const dome = B.MeshBuilder.CreateSphere('dome', { diameter: 2, segments: 48, sideOrientation: B.Mesh.BACKSIDE }, scene);
  dome.material = matCiel;
  dome.infiniteDistance = true;
  dome.isPickable = false;
  dome.alwaysSelectAsActiveMesh = true;
  dome.applyFog = false;

  // ---- environment: the same sky captured in a cube, irradiance from our own harmonics -------
  const sonde = new B.ReflectionProbe('sondeCiel', opts.film ? 256 : 128, scene, true, true, true);
  sonde.renderList.push(dome);
  // captured every frame (one small dome, cheap): the environment is then a function of the frame
  // alone; a capture kept from an earlier shot made revisits differ (seek purity)
  sonde.refreshRate = B.RenderTargetTexture.REFRESHRATE_RENDER_ONEVERYFRAME;
  sonde.cubeTexture.onBeforeRenderObservable.add(() => matCiel.setVector4('uOpt', new B.Vector4(0, 1, 1, 0)));
  sonde.cubeTexture.onAfterRenderObservable.add(() => matCiel.setVector4('uOpt', new B.Vector4(1, 0, 1, 0)));
  scene.environmentTexture = sonde.cubeTexture;
  scene.environmentIntensity = 1.0;

  function harmoniques(s, sc) {
    const sh = new B.SphericalHarmonics();
    const N = 1600;
    const dA = (4 * Math.PI) / N;
    for (let i = 0; i < N; i++) {
      const y = 1 - (2 * (i + 0.5)) / N;
      const r = Math.sqrt(1 - y * y);
      const a = i * 2.399963229728653;
      const d = { x: r * Math.cos(a), y, z: r * Math.sin(a) };
      const c = cielJS(d, s, sc);
      // right-handed scene: cube lookups use the opposite z
      sh.addLight(new B.Vector3(d.x, d.y, -d.z), new B.Color3(c[0], c[1], c[2]), dA);
    }
    sh.convertIncidentRadianceToIrradiance();
    sh.convertIrradianceToLambertianRadiance();
    return B.SphericalPolynomial.FromHarmonics(sh);
  }

  // ---- atmosphere post-process (first in the camera chain, HDR) ------------------------------
  const prof = scene.enableDepthRenderer(camera, false, true);
  const atmo = new B.PostProcess('atmosphere', 'vdtProcheAtmo',
    ['uInvVP', 'uEye', 'uFwd', 'uNF', 'uSun', 'uSunCol', 'uFogCol', 'uZenith', 'uFog', 'uC1', 'uC2', 'uAir', 'uRay', 'uGraine'],
    ['depthSampler'], 1.0, camera, B.Texture.BILINEAR_SAMPLINGMODE, engine, false, null, B.Constants.TEXTURETYPE_HALF_FLOAT);
  atmo.samples = Math.max(1, Math.min(opts.film ? 8 : 4, engine.getCaps().maxMSAASamples || 1));

  const etat = {
    sun: new B.Vector3(0, 1, 0), sunCol: new B.Color3(1, 1, 1), fogCol: new B.Color3(0.6, 0.66, 0.74),
    zenith: new B.Color3(ZENITH[0], ZENITH[1], ZENITH[2]),
    fog: new B.Vector4(1.1e-4, 950, 60000, 50000),
    c1: new B.Vector4(...opts.couches[0], 0.66, 1), c2: new B.Vector4(...opts.couches[1], 0.55, 1),
    air: new B.Vector4(0, 0, opts.film ? 64 : 28, opts.film ? 2 : 1),
    ray: new B.Vector4(0.5, 0.5, 0, 16 / 9),
  };
  const invVP = new B.Matrix();
  atmo.onApply = (fx) => {
    camera.getViewMatrix().multiply(camera.getProjectionMatrix()).invertToRef(invVP);
    fx.setTexture('depthSampler', prof.getDepthMap());
    fx.setMatrix('uInvVP', invVP);
    fx.setVector3('uEye', camera.globalPosition);
    fx.setVector3('uFwd', camera.getForwardRay(1).direction);
    fx.setFloat2('uNF', camera.minZ, camera.maxZ);
    fx.setVector3('uSun', etat.sun);
    fx.setColor3('uSunCol', etat.sunCol);
    fx.setColor3('uFogCol', etat.fogCol);
    fx.setColor3('uZenith', etat.zenith);
    fx.setVector4('uFog', etat.fog);
    fx.setVector4('uC1', etat.c1);
    fx.setVector4('uC2', etat.c2);
    fx.setVector4('uAir', etat.air);
    fx.setVector4('uRay', etat.ray);
    fx.setFloat('uGraine', etat.graine);
  };

  let dernierSoleil = null;
  const tmp = new B.Vector3();
  /**
   * @param {{ heures: number, air: {x:number,z:number}, nuages: number, brume: number, rayons: number }} p
   */
  function maj(p) {
    const s = versSoleil(p.heures);
    const sc = couleurSoleil(s.elevation);
    etat.sun.copyFrom(s.v);
    etat.sunCol.copyFrom(sc.scale(5.0));
    soleil.direction.copyFrom(s.v.scale(-1));
    soleil.diffuse.copyFrom(sc);
    soleil.specular.copyFrom(sc);
    matCiel.setVector3('uSun', s.v);
    matCiel.setColor3('uSunCol', etat.sunCol);
    // haze colour: pale, a little warmer on the sun side is added per ray in the shader
    etat.fogCol.set(0.40 + 0.03 * sc.g, 0.445 + 0.025 * sc.g, 0.51);
    etat.fog.x = 1.05e-4 * p.brume;
    etat.fog.z = camera.maxZ * 0.7;
    etat.fog.w = camera.maxZ * 0.82;
    etat.graine = typeof p.graine === 'number' ? p.graine : 0;
    etat.air.x = p.air.x;
    etat.air.y = p.air.z;
    etat.c1.w = p.nuages * 0.7; // the lower layer is barely saturated (93 %): thin and broken
    etat.c2.w = p.nuages;
    dome.scaling.setAll(camera.maxZ * 0.9);
    // light shafts: sun position on screen
    etat.ray.z = 0;
    if (p.rayons > 0) {
      // this frame's camera only (p.oeil, p.vise from the shot plan): never state derived at the
      // previous render, which would make the picture depend on the frame drawn before
      const vp = camera.getViewMatrix(true).multiply(camera.getProjectionMatrix(true));
      const oeil = p.oeil || camera.position;
      B.Vector3.TransformCoordinatesToRef(oeil.add(s.v.scale(1000)), vp, tmp);
      const devant = B.Vector3.Dot(p.vise || camera.getForwardRay(1).direction, s.v) > 0.2;
      if (devant) {
        etat.ray.x = tmp.x * 0.5 + 0.5;
        etat.ray.y = tmp.y * 0.5 + 0.5;
        etat.ray.z = p.rayons;
        etat.ray.w = engine.getRenderWidth() / Math.max(1, engine.getRenderHeight());
      }
    }
    // environment: re-capture only when the sun really moved (pure: depends on the sun only)
    const cle = `${s.v.x.toFixed(4)},${s.v.y.toFixed(4)},${s.v.z.toFixed(4)}`;
    if (cle !== dernierSoleil) {
      dernierSoleil = cle;
      sonde.cubeTexture.sphericalPolynomial = harmoniques(s.v, etat.sunCol);
    }
    return s;
  }

  return { soleil, dome, sonde, atmo, profondeur: prof, maj, etat };
}
