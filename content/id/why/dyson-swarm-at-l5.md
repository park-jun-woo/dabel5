---
title: "Mengapa L5, Bukan Dekat Matahari"
date: 2026-02-24T12:00:05+09:00
lastmod: 2026-02-24T12:00:05+09:00
tags: ["swarm-dyson", "SEL5", "replikasi-diri", "penskalaan"]
image: "/images/post005.webp"
summary: "Skenario standar Dyson swarm mengasumsikan pembongkaran Merkurius dekat Matahari. Tapi bagaimana jika menggunakan sumber daya asteroid dan membangun di titik Matahari-Bumi L5? Berikut perhitungannya."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Mempertanyakan Kebijaksanaan Konvensional

Skenario standar yang terlintas saat membicarakan Dyson swarm: membongkar Merkurius dan menempatkan panel/cermin dekat Matahari. Ini adalah kerangka yang dibangun oleh seri Isaac Arthur, dan kebanyakan orang menerimanya begitu saja.

Tapi saya menghitung pendekatan yang berbeda — bagaimana jika menggunakan sumber daya asteroid dan membangun di titik Matahari-Bumi L5?

---

## Mengapa L5?

### Fluks Matahari
- L5 (1 AU): ~1.361 W/m² — sama dengan orbit Bumi
- Orbit Merkurius (0,39 AU): ~8.942 W/m² — sekitar 6,6 kali lebih kuat
- "Bukankah Merkurius lebih baik?" — Ya, per satuan luas. Tapi itu bukan segalanya

### Keunggulan Tersembunyi L5
1. **Titik stabilitas gravitasi** — Biaya pemeliharaan orbit nyaris nol. Dekat Merkurius, gradien gravitasi Matahari curam sehingga memerlukan koreksi orbit terus-menerus
2. **Sinar matahari tanpa henti 24/7/365** — Bayangan Bumi tidak dapat menjangkau (150 juta km). Tidak ada gerhana
3. **Wilayah stabil seluas jutaan km** — Ratusan ribu modul dapat ditempatkan tanpa gangguan satu sama lain
4. **Jarak tetap dari Bumi** — Menyederhanakan perencanaan logistik. Penundaan komunikasi ~8 menit 20 detik satu arah (bukan real-time, tapi diselesaikan dengan operasi AI otonom)
5. **Dapat dihuni** — Dekat Merkurius, lingkungan termal sangat ekstrem. L5 membuat desain habitat manusia jauh lebih realistis

---

## Sumber Daya: Pembongkaran Merkurius vs Asteroid

### Biaya Tersembunyi Pendekatan Merkurius
- Kecepatan lepas Merkurius: 4,25 km/s — sumur gravitasi yang besar
- Suhu permukaan Merkurius: 430°C siang hari — manajemen termal ekstrem untuk peralatan penambangan
- Merkurius → penempatan di orbit Matahari: diperlukan delta-V tambahan
- **Masalah terbesar: Merkurius adalah planet** — Penambangan skala besar pada gravitasi permukaan 0,38g pada dasarnya adalah varian penambangan di Bumi

### Pendekatan Asteroid (1986 DA)
- Asteroid logam tipe M: **90%+ paduan Fe-Ni** — hampir logam murni
- Perkiraan massa: diameter ~2,3 km, densitas bulk asteroid tipe M → **20+ miliar ton**
- Mikrogravitasi → energi penambangan minimal, kecepatan lepas dapat diabaikan
- Bahkan produk sampingan dimanfaatkan sepenuhnya: terak silikat → pelindung radiasi + bahan baku ingot silikon

| Perbandingan | Pembongkaran Merkurius | Asteroid (1986 DA) |
|------|----------|----------------|
| Lepas dari sumur gravitasi | 4,25 km/s | ~beberapa m/s |
| Suhu permukaan | 430°C (siang) | Kriogenik (mudah dikelola) |
| Komposisi sumber daya | Didominasi silikat, perlu pemisahan logam | 90%+ paduan Fe-Ni (hampir siap pakai) |
| Kompleksitas peralatan tambang | Tinggi (gravitasi, panas) | Rendah (mikrogravitasi) |
| Total volume sumber daya | Sangat besar (seluruh planet) | Cukup untuk bootstrap K1 |

Merkurius unggul jauh dalam total volume sumber daya, tetapi **untuk tahap pertama (bootstrap phase), asteroid jauh lebih praktis.**

---

## Inti: Siklus Replikasi Diri

Pembeda sesungguhnya dari desain ini bukan sekadar "di mana menambang dan di mana menempatkan."

**Bijih asteroid → peleburan vakum dengan panas matahari cermin Dyson di L5 → hasil produksi membangun cermin baru → area pengumpulan bertambah → kecepatan peleburan meningkat → pertumbuhan eksponensial**

1. Cermin awal mengonsentrasikan sinar matahari
2. Panas terkonsentrasi memanaskan bijih hingga ~1.500°C → menghasilkan paduan Fe-Ni
3. Paduan membuat rangka cermin baru
4. Cermin baru ditambahkan → area pengumpulan bertambah → **pertumbuhan eksponensial dimulai**

### Penskalaan

| Skala | Daya | vs Bumi | Populasi | Komputasi AI |
|------|------|----------|------|---------|
| 1 modul | 370 MW | 1 PLTN kecil | 2.500 | 32 EF |
| 10 modul | 3,7 GW | 3 PLTN besar | 25.000 | 320 EF |
| 1.000 modul | 370 GW | 2% Bumi | 2,5M | 32 ZF |
| 10.000 modul | 3,7 TW | 20% Bumi | 25M | 320 ZF |
| 200.000 modul | 74 TW | **4x Bumi** | 500M | 6.400 ZF |

Periode penggandaan bergantung pada anggaran massa per modul dan kematangan proses. Dengan asumsi rentang 2–5 tahun, mencapai skala K1.0 dari 1 modul membutuhkan 50–125 tahun.

---

## Ini Bukan Berarti Merkurius Salah

Mari jujur tentang satu hal. Umat manusia saat ini berada di K 0,73. Bahkan hingga K1.0 (10¹⁶ W) ada kesenjangan ~550 kali dari posisi kita sekarang. **Sebelum membicarakan K2, kita harus mencapai K1 dulu.**

Skala yang dibutuhkan untuk K1.0 — ~27 juta modul, ~10 PW — sepenuhnya dapat dipenuhi dengan sumber daya asteroid. Tidak perlu menyentuh Merkurius. Pembongkaran Merkurius baru menjadi keharusan dalam hal total volume sumber daya pada K1.5+ (10²¹ W) ke atas.

Merkurius adalah jalan tol menuju K2. Tapi yang kita butuhkan sekarang adalah jalan masuk ke tol itu. **Kamu tidak butuh jalan tol untuk membangun jalan tol.**

Pada fase bootstrap:
- Asteroid memiliki biaya akses lebih rendah
- L5 memiliki biaya operasional lebih rendah
- Siklus replikasi diri dimulai lebih cepat

Bagaimana jika mencapai K1 di L5 terlebih dahulu, lalu menggunakan kapasitas industri tersebut untuk membongkar Merkurius, justru merupakan jalur yang lebih cepat?
