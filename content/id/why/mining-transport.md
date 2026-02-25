---
title: "Mengapa Tidak Melebur di Lokasi"
date: 2026-02-24T12:00:04+09:00
lastmod: 2026-02-24T12:00:04+09:00
tags: ["penambangan-asteroid", "transportasi", "SMR", "NTP"]
image: "/images/1986da-orbit.webp"
summary: "Desain teknik lengkap untuk menambang asteroid logam 1986 DA dengan kapal tambang bertenaga SMR, mengemas bijih dalam jaring kawat Fe-Ni, dan mengangkut 200.000 ton per jendela transfer."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

*Orbital visualization: [SpaceReference.org](https://www.spacereference.org/asteroid/6178-1986-da), built with [SpaceKit](https://typpo.github.io/spacekit/). Data: JPL Small Body Database.*

## Menambang Kedengarannya Bagus, tapi Bagaimana?

Di artikel sebelumnya, kami mengusulkan 1986 DA sebagai sumber bahan baku untuk swarm Dyson. Lebih dari 90% Fe-Ni, mikrogravitasi, nol limbah. Lebih unggul dari Merkurius dalam segala hal untuk bootstrap.

Tapi pertanyaan tersisa: **Bagaimana sebenarnya menambang gumpalan logam di mikrogravitasi, dan bagaimana memindahkannya?**

Prinsip inti terlebih dahulu: **"Di lokasi, hanya gali, hancurkan, dan kemas. Pekerjaan berat dilakukan di tempat energi berlimpah."**

---

## Pembagian Peran: Lokasi vs Pangkalan

| Tugas | Lokasi | Alasan |
|-------|--------|--------|
| Penggalian & penghancuran | 1986 DA di lokasi | Tempat bijih berada |
| Pengemasan (jaring kawat) | 1986 DA di lokasi | Dibuat dari Fe-Ni lokal |
| Penyortiran | **Tidak dilakukan** | Semua komponen punya kegunaan |
| Peleburan | **Pangkalan (cermin Dyson)** | Panas matahari cermin kelas GW >> SMR lokasi kelas kW |
| Fabrikasi & perakitan | **Pangkalan** | Kluster terspesialisasi |

Mengapa tidak melebur di lokasi? Peleburan membutuhkan 1.600°C. SMR di lokasi menghasilkan 50~100 kW. Cermin Dyson di pangkalan menghasilkan ~600 MW (termal). **Kesenjangan energi ribuan kali lipat.** Membangun peleburan di asteroid sama seperti mendirikan pabrik baja di puncak gunung — lebih masuk akal mengirim bijihnya.

---

![mining-transport](/images/post004.webp)

## Kapal Tambang: Mesin yang Menggali, Menghancurkan, dan Mengemas

### Energi: SMR + Dorongan Surya

Orbit sangat elips 1986 DA (eksentrisitas 0,58) menyebabkan fluks surya bervariasi lebih dari 14 kali tergantung posisi orbit.

| Posisi Orbit | Jarak | Fluks Surya | vs Bumi |
|-------------|-------|-------------|---------|
| Perihelion | 1,17 AU | ~995 W/m² | 73% |
| Sumbu semi-mayor | 2,81 AU | ~172 W/m² | 13% |
| Aphelion | 4,46 AU | ~68 W/m² | 5% |

**Tenaga surya saja tidak bisa menopang penambangan kontinu.** SMR (Reaktor Modular Kecil, 50~100 kW) adalah sumber energi utama. Dekat perihelion, panel surya bergabung sebagai pendorong.

| Segmen Orbit | SMR | Surya | Gabungan | Mode |
|-------------|-----|-------|----------|------|
| Dekat perihelion (~1,2 AU) | 50~100 kW | 50~100 kW | **100~200 kW** | Dorongan |
| Orbit tengah (~2,8 AU) | 50~100 kW | ~15 kW | ~65~115 kW | Normal |
| Dekat aphelion (~4,5 AU) | 50~100 kW | ~5 kW | ~55~105 kW | Kecepatan rendah |

Bahkan di aphelion, SMR menjaga penambangan tetap berjalan. Hanya melambat.

### Peralatan

| Peralatan | Fungsi | Konsumsi Daya |
|-----------|--------|--------------|
| Ekskavator | Penambangan permukaan/bawah permukaan | ~20~50 kW |
| Penghancur | Memecah bijih ke ukuran transportasi | ~10~30 kW |
| Tungku listrik kecil | Fe-Ni → bahan kawat | ~10~20 kW |
| Mesin penarik kawat | Kawat → jaring | ~5~10 kW |
| Kontrol & komunikasi | Kontrol otonom AI | ~5 kW |
| **Total** | | **~50~115 kW** |

Satu SMR menggerakkan semua peralatan. Kapal tambang **ditempatkan secara permanen** — mengorbit bersama 1986 DA dan menambang tanpa henti.

### Produktivitas

Asumsi konservatif: rata-rata 50 kW, ~100 kg bijih diproses per kWh (penghancuran mekanis dan pengemasan di mikrogravitasi; sebanding dengan penghancuran batuan terestrial pada 10–25 Wh/kg; peleburan dilakukan terpisah di pangkalan).

| Item | Nilai |
|------|-------|
| Produksi harian | ~120 ton |
| Produksi tahunan | ~43.800 ton |
| **Per periode orbit (4,71 tahun)** | **~200.000 ton** |

---

## Kontainer: Jaring, Bukan Kotak

Apa yang dibutuhkan kontainer kargo di luar angkasa?
- Penahanan tekanan — vakum, tidak perlu
- Penopang berat sendiri — mikrogravitasi, tidak perlu
- Hambatan udara — vakum, tidak perlu
- **Menjaga bijih tidak berhamburan selama transportasi**

Itu satu-satunya persyaratan. Bukan kotak kaku — **jaring sudah cukup.**

### Proses Fabrikasi

```
Bijih yang ditambang
  ├─ 99,5% → Kargo (bundel bijih)
  └─ 0,5% → Tungku listrik kecil → Penarikan kawat → Anyaman jaring
                                                    → Pengemasan bundel bijih
```

| Metode | Rasio Massa Kontainer:Kargo |
|--------|---------------------------|
| Kontainer logam dari Bumi | Pemborosan transportasi ekstrem |
| Kotak Fe-Ni cetak di lokasi | ~2~3% (berlebihan) |
| **Jaring kawat Fe-Ni di lokasi** | **~0,1~0,5%** |

**Jaring itu sendiri menjadi bahan baku peleburan saat tiba.** Bahkan kemasannya dimanfaatkan 100%.

---

## Transportasi: Jendela Transfer dan Propulsi

### Mekanika Orbit

Periode orbit 1986 DA: 4,71 tahun. Jendela transfer optimal ke ruang Bumi terbuka sekali per periode orbit.

| Item | Nilai |
|------|-------|
| LEO → rendezvous 1986 DA | delta-V ~7,1 km/s |
| Keberangkatan optimal | Dekat perihelion (1,17 AU) |
| Pendekatan dekat berikutnya | **2038 (0,21 AU)** |

### Opsi Propulsi

| Metode | Impuls Spesifik (Isp) | Karakteristik | Kesesuaian |
|--------|---------------------|---------------|------------|
| Kimia (LH2/LOX) | ~450 s | Fraksi muatan sangat rendah | ❌ |
| **Propulsi Nuklir Termal (NTP)** | **~900 s** | Gaya dorong tinggi, cepat | ✅ |
| **Propulsi Nuklir Elektrik (NEP)** | **~3.000 s+** | Propelan minimal, lambat | ✅ Transportasi massal |
| Propulsi Surya Elektrik (SEP) | ~3.000 s | Efisiensi turun di aphelion | ⚠️ Terbatas |

**Hibrida NTP + NEP mungkin optimal:** satu reaktor berfungsi sebagai sumber panas NTP (gaya dorong tinggi untuk keberangkatan perihelion) dan sumber listrik NEP (gaya dorong rendah, efisiensi tinggi saat pelayaran).

### Siklus Logistik

```
[Tahun 0]  Kapal tambang tiba di 1986 DA, penambangan dimulai
             │ 4,71 tahun penambangan, pengemasan, penyimpanan (~200.000 ton)
[Tahun ~5] Jendela transfer → kapal transportasi memuat dan berangkat
             │ Transfer Hohmann (~2-3 tahun)
[Tahun ~7] Kapal transportasi tiba, bijih dibongkar
             │ Perawatan & pengisian ulang
[Tahun ~8] Kapal transportasi berangkat kembali
             │
[Tahun ~10] Pemuatan kedua ... siklus berulang
```

Kapal tambang tetap di tempat; kapal transportasi bolak-balik. Penambangan dan transportasi berjalan **secara asinkron dan paralel.**

---

## 2038: Lewatkan dan Tunggu Puluhan Tahun

| Waktu | Peristiwa |
|-------|-----------|
| 2030-an | Starship dikomersialkan, teknologi SMR luar angkasa matang |
| **2038** | **Pendekatan dekat 1986 DA (0,21 AU) — jendela optimal untuk mengerahkan kapal tambang** |
| 2038~2042 | Kapal tambang tiba di lokasi, penambangan dimulai |
| ~2043 | Kapal transportasi pertama memuat dan berangkat |
| **~2046** | **Pengiriman bijih pertama** |

Setelah 2038, pendekatan dekat berikutnya dengan skala ini baru terjadi puluhan tahun kemudian. **Melewatkan jendela ini akan menunda jadwal secara signifikan.**

### Status Teknologi yang Dibutuhkan

| Teknologi | Saat Ini (2026) | Prospek 2038 |
|-----------|----------------|--------------|
| Starship (kendaraan peluncuran berat) | Penerbangan uji berlangsung | ✅ Komersialisasi diharapkan |
| SMR luar angkasa | NASA FSP kelas 40 kW dalam pengembangan | ✅ Demonstrasi bulan diharapkan |
| Propulsi NTP | DARPA DRACO dalam pengembangan | ⚠️ Penerbangan uji diharapkan |
| Penambangan asteroid | OSIRIS-REx pengembalian sampel berhasil | ⚠️ Skala besar belum terbukti |
| Operasi luar angkasa otonom AI | Level rover Mars | ✅ Kematangan memadai diharapkan |

Tidak ada teknologi yang mustahil. Semuanya **sedang dikembangkan atau diharapkan matang dalam satu dekade.**

---

## Setelah Tiba: Matahari yang Melebur

Saat bijih tiba, cermin Dyson memanaskannya langsung hingga 1.600°C. Vakum luar angkasa adalah "peralatan pemurnian gratis":

1. **Peleburan optik** — Panas cermin terkonsentrasi melelehkan bijih mentah menjadi logam cair
2. **Degassing vakum** — Belerang dan fosfor menguap secara alami dalam vakum (ditangkap oleh jebakan dingin)
3. **Pemisahan sentrifugal** — Lapisan luar: Fe-Ni + logam kelompok platina / Lapisan dalam: terak silikat

```
Bundel bijih tiba
  ├→ Jaring kawat Fe-Ni → Dimasukkan ke peleburan (kemasan jadi bahan baku)
  └→ Bijih → Pemanasan cermin hingga 1.600°C
       ├→ Paduan Fe-Ni (90%+) → Elemen struktural, rangka cermin, pipa
       ├→ Terak silikat → Pelindung + bahan baku ingot silikon
       ├→ Logam kelompok platina → Pelapis, katalis
       └→ S, P → Bahan kimia, doping semikonduktor
```

Apa yang dicapai pabrik baja di Bumi dengan energi dan bahan kimia besar-besaran, **vakum luar angkasa dan panas matahari menyediakannya secara gratis.**

---

## Ringkasan Satu Baris

Kapal tambang menggali, menghancurkan, dan mengemas dengan satu SMR. Kontainer adalah jaring Fe-Ni lokal — bahkan kemasannya adalah bahan baku. Kapal transportasi mengangkut 200.000 ton per jendela transfer. 2038 adalah jendela kesempatan pertama. Bijih yang tiba dilebur oleh Matahari. Tidak ada yang terbuang.
