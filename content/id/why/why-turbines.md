---
title: "Mengapa Turbin, Bukan Panel Surya"
date: 2026-02-24T12:00:07+09:00
lastmod: 2026-02-24T12:00:07+09:00
tags: ["panas-matahari", "turbin", "replikasi-diri", "fotovoltaik"]
summary: "Panel surya dan turbin sama-sama mengubah sinar matahari menjadi listrik dengan efisiensi ~30% di luar angkasa. Tapi turbin memanfaatkan 70% sisanya sebagai panas berguna secara bertingkat, bisa dibuat dari material asteroid, dan bisa diperbaiki di tempat — satu-satunya pilihan untuk kawanan Dyson yang mereplikasi diri."
image: "/images/why-turbines.webp"
author: "PARK JUN WOO"
imageCaption: "Pemasangan bilah rotor turbin uap di pabrik Siemens. Foto: Siemens Pressebild / Wikimedia Commons / CC BY-SA 3.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## "Kenapa turbin lagi?"

Ketika orang berpikir tentang pembangkit listrik kawanan Dyson, panel surya (PV) adalah pilihan yang jelas. Standar untuk energi luar angkasa. ISS menggunakan PV. Sebagian besar wahana antariksa menggunakan PV.

Namun desain ini menggunakan turbin. Mengapa kembali ke teknologi abad ke-19 di abad ke-21?

Jawabannya sederhana: **kamu tidak bisa membuat panel surya dari asteroid, tapi bisa membuat turbin.**

---

## Efisiensinya sama — 30%

Mari kita bahas ini dulu. "Bukankah PV lebih efisien?"

| | Panel Surya (GaAs multi-junction) | Turbin Termal Surya |
|---|---|---|
| Efisiensi konversi | ~30% (kelas luar angkasa) | ~30% (sisi panas 1.500 K / sisi dingin 500 K) |
| Batas Carnot | Tidak berlaku | 66,7% (terealisasi ~45%) |
| Output listrik | **Sama** | **Sama** |

Mengumpulkan 1.225 MW(termal) dengan cermin 1 km², baik menggunakan PV maupun turbin, **output listriknya ~370 MW sama saja.**

Jika efisiensinya sama, perbedaannya ada di tempat lain.

---

## Perbedaan 1: 70% sisanya

Baik PV maupun turbin gagal mengubah 70% energi yang masuk menjadi listrik. Tapi ke mana 70% itu pergi sangat berbeda.

### PV: 70% menghilang sebagai panas buangan bersuhu rendah

```
Input surya 1.225 MW
  ├→ 30% → 370 MW (listrik)
  └→ 70% → 855 MW → permukaan panel pada 60–80°C panas buangan
                     → tidak berguna. Diradiasikan ke angkasa melalui heat sink.
```

Pada 60–80°C, kamu tidak bisa melebur logam, menjalankan pabrik, atau memanaskan habitat. **70% energi begitu saja menghilang.**

### Turbin: 70% mengalir bertingkat dari suhu tinggi ke rendah

```
Input termal surya 1.225 MW
  ├→ 30% → 370 MW (listrik)
  └→ 70% → 855 MW (panas) → pemanfaatan bertahap berdasarkan suhu:
       ├→ 800–1.000°C: ~400 MW → peleburan (pencairan Fe-Ni)
       ├→ 400–600°C:   ~250 MW → pelapisan, perlakuan panas, pembentukan
       ├→ 100–200°C:   ~120 MW → pemanasan habitat
       └→ 30–60°C:      ~85 MW → panas lingkungan pusat data
```

**70% yang sama melewati secara berurutan peleburan → pabrik → habitat → pusat data, dan semuanya digunakan.** "Panas buangan" turbin bukan buangan — itu sumber energi untuk proses berikutnya.

Pemanfaatan efektif energi yang masuk:
- PV: ~30% (listrik saja)
- **Turbin: ~30% + kaskade termal → efektif 85%+**

---

## Perbedaan 2: Kompatibilitas dengan loop replikasi diri

Ini faktor penentunya.

### Membuat PV di luar angkasa

Manufaktur panel surya (GaAs multi-junction) membutuhkan:
1. Bahan baku galium (Ga) + arsenik (As) — **tidak ditemukan di asteroid**
2. Pertumbuhan kristal tunggal (MOCVD, MBE) — **peralatan presisi ekstrem**
3. Deposisi epitaksial multi-lapis — **membutuhkan cleanroom**
4. Pelapisan anti-reflektif, pengkabelan, perakitan modul — **jalur fabrikasi khusus**

Asteroid tidak memiliki Ga maupun As. Bahkan dengan peralatannya, tidak ada bahan baku. **PV tidak bisa masuk ke loop replikasi diri.** Harus terus dipasok dari Bumi.

Bagaimana dengan PV silikon (Si)? Sebenarnya, desain ini sudah mencakup proses untuk memproduksi ingot Si kelas semikonduktor dari slag silikat (zone refining, untuk chip AI). Jadi bahan baku Si tersedia. Namun:
- Efisiensi Si PV di luar angkasa ~20% — lebih rendah dari GaAs (30%) dan di bawah turbin (30%)
- Jalur manufaktur sel PV (difusi, pelapisan anti-reflektif, pola elektroda) **terpisah dari fab chip**
- Efisiensi menurun akibat radiasi luar angkasa → siklus penggantian lebih pendek
- Wafer Si yang sama **jauh lebih berharga sebagai chip AI**

Bahkan dengan Si tersedia, membuatnya jadi PV itu pemborosan. **Kalau punya silikon, buat chip.**

### Membuat turbin di luar angkasa

| Komponen | Material | Sumber | Fabrikasi |
|----------|----------|--------|-----------|
| Bilah & nosel suhu tinggi | Superalloy Ni | Asteroid Fe-Ni | Pengecoran presisi |
| Kompresor & poros suhu rendah | Alloy Ti | Ilmenit bulan | Permesinan |
| Casing | Fe-Ni | Asteroid | Lembaran logam & pengelasan |

**Semuanya bisa dibuat dari material yang sudah ada di loop replikasi diri (Fe-Ni, Ti).** Tidak perlu bahan baku tambahan, tidak perlu jalur fabrikasi tambahan. Turbin keluar dari jalur produksi yang sama dengan yang membuat rangka cermin.

---

## Perbedaan 3: Umur pakai dan pemeliharaan

### Masalah radiasi PV luar angkasa

PV luar angkasa rusak oleh partikel berenergi tinggi (proton, ion berat) yang mengganggu kisi kristal. Efisiensi menurun ~1–3% per tahun.

- Setelah 10 tahun: efisiensi turun ke 70–80%
- Perlu penggantian → **tidak bisa diproduksi, harus dipasok dari Bumi**
- Jika pasokan tidak tersedia: terima penurunan output

### Keausan turbin

Turbin juga tidak bertahan selamanya. Creep bilah suhu tinggi dan keausan bantalan adalah mekanisme degradasi utama.

Tapi:
- Bilah bisa **dicetak ulang di tempat dari superalloy Ni**
- Bantalan → **bantalan magnetik tanpa kontak**: nol keausan
- Desain modular: hanya komponen yang aus yang diganti, bukan seluruh unit

**Komponen turbin bisa diproduksi dan diganti di tempat. Komponen PV tidak bisa.** Dalam sistem replikasi diri, perbedaan ini menentukan.

---

## Keterbatasan nyata turbin — dan solusinya

Mari jujur soal kekurangannya.

### Keterbatasan 1: Dibutuhkan fluida kerja

Turbin membutuhkan fluida yang mengembang saat dipanaskan untuk memutar rotor. Dari mana mendapatkan fluida ini di luar angkasa?

| Kandidat | Kelebihan | Kekurangan | Perolehan |
|----------|-----------|------------|-----------|
| Helium (He) | Inert, stabil suhu tinggi | Sulit diisi ulang jika bocor | Ditangkap dari outgassing asteroid |
| CO₂ superkritis | Densitas tinggi, turbin kompak | Perlu manajemen korosi | Outgassing asteroid |
| Natrium/Kalium (logam cair) | Suhu ultra-tinggi, transfer panas sangat baik | Reaktif (aman di vakum) | Jejak dari asteroid |

Sistem beroperasi dalam siklus tertutup, jadi tidak ada konsumsi fluida. Hanya muatan awal yang perlu diamankan. Gas bisa ditangkap selama outgassing peleburan asteroid, atau sejumlah kecil bisa dipasok dari Bumi pada awalnya.

### Keterbatasan 2: Komponen bergerak — risiko kegagalan di luar angkasa

Kelemahan mendasar turbin: komponen berputar berkecepatan tinggi. Bahkan di Bumi, pemeliharaan turbin adalah pekerjaan yang menuntut.

**Solusi:**
- **Bantalan magnetik** — penopang rotasi tanpa kontak. Nol keausan. Sudah dikomersialkan dalam turbomachinery berkecepatan tinggi di Bumi
- **Kartrid bilah modular** — mengganti set bilah sebagai satu unit. Tidak perlu servis individual
- **Manufaktur lokal** — mencetak komponen pengganti sesuai kebutuhan. Tidak perlu menunggu pasokan dari Bumi
- **Redundansi** — beberapa turbin per modul. Output tetap terjaga bahkan saat satu unit dalam pemeliharaan

### Keterbatasan 3: Getaran

Rotasi berkecepatan tinggi menghasilkan getaran. Ini masalah jika fab semikonduktor atau peralatan optik presisi berada di modul yang sama.

**Solusi:**
- **Kluster terspesialisasi** — memisahkan secara fisik modul turbin dari modul fabrikasi (struktur terpisah)
- **Dudukan peredam getaran** — memasang turbin pada sambungan struktural fleksibel
- Di Bumi juga tidak menempatkan pembangkit listrik dan pabrik semikonduktor di gedung yang sama

### Keterbatasan 4: Pembuangan panas

Panas sisi dingin turbin harus diradiasikan ke luar angkasa. Tidak ada atmosfer di luar angkasa, jadi pendinginan konveksi tidak mungkin — hanya pendinginan radiasi yang bekerja.

**Ini topik besar yang berdiri sendiri. Akan dibahas secara detail di artikel berikutnya.**

---

## Ringkasan satu baris

Panel surya dan turbin memiliki efisiensi listrik yang sama (30%). Tapi PV membuang 70% sisanya, sementara turbin memanfaatkannya. PV tidak bisa dibuat di luar angkasa; turbin bisa. Ketika PV rusak, menunggu dari Bumi; ketika bilah turbin aus, dicetak ulang di tempat. Dalam sistem replikasi diri, jawabannya jelas.
