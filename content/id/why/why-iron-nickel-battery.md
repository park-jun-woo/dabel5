---
title: "Mengapa Baterai Nikel-Besi, Bukan Litium-Ion"
date: 2026-02-25T12:00:01+09:00
lastmod: 2026-02-25T12:00:01+09:00
tags: ["baterai-nikel-besi", "baterai-edison", "battolyser", "ESS", "replikasi-diri"]
image: "/images/why-iron-nickel-battery.webp"
summary: "Di asteroid tidak ada litium, di luar angkasa tidak bisa mengganti baterai setiap 10 tahun, dan di ruang hampa tidak bisa memadamkan api. Baterai nikel-besi dibuat dari produk sampingan peleburan asteroid, bertahan 30-50 tahun, dan setelah terisi penuh menghasilkan hidrogen dan oksigen."
author: "Park Jun Woo"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Baterai nikel-besi yang dikembangkan Edison pada 1901. Thomas Edison National Historical Park. Photo: z22 / Wikimedia Commons / CC BY-SA 3.0"
---

## "Penyimpanan energi sudah pasti litium-ion, kan?"

Modul Dyson mengumpulkan panas matahari dengan cermin dan memutar turbin. Akan bagus jika matahari bersinar 24 jam sehari, 365 hari setahun, tapi kenyataannya tidak demikian.

- **Gerhana (eclipse):** Pangkalan EML5 memasuki bayangan Bumi dan Bulan 2-3 kali per tahun, total 3-12 jam
- **Fluktuasi beban:** Turbin merespons lambat terhadap perubahan beban mendadak. Tanpa ESS, tegangan berfluktuasi saat permintaan berubah sesaat
- **Penghentian darurat:** Saat pemeliharaan cermin atau kerusakan turbin, sistem kritis — penunjang kehidupan, AI, komunikasi — tidak boleh berhenti
- **Daya penyalaan:** Saat penambatan dan manuver penghindaran kapal tunda, diperlukan daya besar sesaat

Tanpa baterai, modul Dyson tidak bisa beroperasi. Lalu baterai apa?

Di Bumi, jawabannya sudah jelas. Litium-ion. Kepadatan energi, efisiensi pengisian/pengosongan, bobot ringan — unggul di semua indikator. Namun dengan alasan yang sama mengapa turbin mengalahkan panel surya di artikel sebelumnya, **di luar angkasa standarnya berbeda.**

Litium-ion harus diganti setiap 10 tahun, dan tambang litium terdekat ada di Bumi. Di asteroid, besi dan nikel berserakan di mana-mana.

---

## Standar Bumi vs. Standar Luar Angkasa

| Kriteria | Nikel-Besi (Edison) | Litium-Ion | Apa yang penting di luar angkasa? |
|----------|--------------------|-----------|---------------------------------|
| Kepadatan energi volumetrik | 30-60 Wh/L | 250-700 Wh/L | Pada skala km², volume tidak berarti |
| Kepadatan energi gravimetrik | 30-50 Wh/kg | 150-270 Wh/kg | Struktur tidak bergerak → tidak relevan |
| Umur pakai | **30-50 tahun** | 5-15 tahun | Biaya penggantian di luar angkasa **astronomis** |
| Toleransi pengisian berlebih | **Sangat tinggi** | Rendah (thermal runaway, kebakaran) | Kebakaran di ruang hampa = kehilangan total modul |
| Toleransi pengosongan berlebih | **Tinggi** | Kerusakan tak dapat dipulihkan | Kemungkinan pengosongan total saat gerhana |
| Pengadaan material lokal | **Mungkin** (Fe, Ni, KOH) | **Tidak mungkin** (Li, Co, elektrolit organik) | Pertanyaan keberadaan siklus replikasi diri |
| Elektrolit | Larutan kalium hidroksida (berbasis air) | Pelarut organik (mudah terbakar) | Stabilitas radiasi, keamanan kebakaran |
| Pengosongan sendiri | Tinggi (~1%/hari) | Rendah (~0,1%/hari) | Tidak berarti dalam lingkungan pengisian terus-menerus |

**Yang penting di Bumi: ringan, kecil, kepadatan energi tinggi.**
**Yang penting di luar angkasa: bisa dibuat di tempat, aman, tahan lama.**

Standar berbeda, jawaban berbeda.

---

## Material — Di Asteroid Tidak Ada Litium

Untuk membuat baterai litium-ion diperlukan:

| Material | Kegunaan | Ketersediaan di asteroid |
|----------|---------|------------------------|
| Litium (Li) | Material aktif katoda | **Tidak ada** — unsur nukleosintesis Big Bang, hanya jejak pada asteroid batuan |
| Kobalt (Co) | Stabilisasi katoda | Hanya jejak — ekstraksi ekonomis tidak mungkin |
| Grafit (C) | Anoda | Ada di asteroid karbon, tapi bukan grafit kristal |
| Elektrolit organik | Konduksi ion | **Perlu disintesis** — etilen karbonat dll., kimia organik kompleks |
| Separator (PE/PP) | Pencegahan hubung singkat | **Perlu disintesis** — manufaktur polimer presisi |

Tidak ada litium. Itu saja sudah game over. Jika harus terus dipasok dari Bumi, itu **bukan replikasi diri melainkan ketergantungan pada jalur pasokan**.

"Bagaimana dengan natrium-ion?" Na ada di asteroid. Tapi umur pakai 30-50 tahun belum terbukti, tidak ada fungsi battolyser, dan memerlukan elektrolit organik. Masalah degradasi elektrolit organik oleh radiasi kosmik pada natrium-ion juga sama persis.

"Bukankah baterai solid-state segera hadir?" Jika tidak bisa dibuat di asteroid, sebaik apa pun tidak ada artinya. Faktor kunci bukan kepadatan energi, melainkan **kemampuan produksi lokal**.

Untuk membuat baterai nikel-besi diperlukan:

| Material | Kegunaan | Sumber |
|----------|---------|--------|
| Besi (Fe) | Anoda | Komponen utama 1986 DA — **berserakan di mana-mana** |
| Nikel (Ni) | Katoda | Komponen utama 1986 DA — **berserakan di mana-mana** |
| Kalium hidroksida (KOH) | Elektrolit | K terkandung dalam silikat asteroid, air dari asteroid karbon |
| Lembaran baja | Casing | Pengolahan paduan Fe-Ni |

**Semua komponen baterai adalah produk sampingan proses peleburan.** Saat membuat rangka cermin, baterai juga bisa dibuat sekaligus. Impor bahan baku tambahan: nol.

---

## Umur Pakai — Biaya Penggantian Menentukan Segalanya

Di Bumi, umur litium-ion 10-15 tahun sudah cukup. Biaya penggantian hanya harga baterai.

Di luar angkasa, biaya penggantian meliputi:
1. Produksi baterai baru (jika memungkinkan)
2. Transportasi (jika tidak memungkinkan, dari Bumi — **ribuan dolar per kg**)
3. EVA atau pekerjaan penggantian robotik
4. Downtime sistem selama penggantian

**Umur pakai baterai nikel-besi: 30-50 tahun.** Ada **contoh yang masih berfungsi** dari baterai nikel-besi Edison tahun 1901. Jika elektrolit (larutan KOH) diisi ulang setiap 10-15 tahun, elektroda bertahan nyaris selamanya.

Satu-satunya kimia baterai yang memungkinkan **nol penggantian** selama seluruh umur pakai modul.

---

## Keamanan — Kebakaran di Ruang Hampa Berarti Kematian

Elektrolit organik baterai litium-ion mudah terbakar. Saat pengisian berlebih, kerusakan fisik, atau hubung singkat internal:

```
Kenaikan suhu internal → Penyusutan separator → Perluasan hubung singkat → Dekomposisi elektrolit
→ Pelepasan gas mudah terbakar → Penyalaan → Thermal runaway berantai pada sel yang berdekatan
```

Di Bumi: mobil pemadam datang.
Di luar angkasa: **di ruang hampa tidak ada pemadam kebakaran.** Kebakaran di modul tertutup = hilangnya penunjang kehidupan + penuh gas beracun + penyelamatan tidak mungkin.

Bahkan di ISS, kebakaran litium-ion adalah salah satu skenario yang paling ditakuti. Dengan ribuan modul Dyson yang menggunakan litium-ion, **secara statistik kebakaran adalah kepastian**.

Keamanan inheren nikel-besi:

- Elektrolit: **larutan air** kalium hidroksida — berbasis air. Tidak terbakar
- Saat pengisian berlebih: air dielektrolisis menjadi H₂ + O₂ — bukan thermal runaway
- Saat pengosongan berlebih: tidak ada kerusakan elektroda yang tak dapat dipulihkan — dipulihkan dengan pengisian ulang
- Saat kerusakan fisik: kebocoran KOH — korosif tapi **tidak ada ledakan, tidak ada kebakaran**

**"Baterai yang tidak terbakar" di luar angkasa bukan kemewahan, melainkan keharusan.**

---

## Battolyser — Baterai yang Juga Melakukan Elektrolisis Air

Di sinilah nikel-besi melampaui sekadar "pilihan kedua" dan memiliki **keunggulan unik**.

### Prinsip

Konsep Battolyser yang dikembangkan oleh TU Delft. Secara aktif memanfaatkan toleransi pengisian berlebih baterai nikel-besi:

```
[Selama pengisian]       Energi listrik → Penyimpanan energi kimia di elektroda Fe/Ni
[Setelah terisi penuh]   Arus tambahan → Elektrolisis air dalam larutan KOH
                         Katoda: 2H₂O + 2e⁻ → H₂↑ + 2OH⁻
                         Anoda: 2OH⁻ → ½O₂↑ + H₂O + 2e⁻
```

**Satu perangkat menggabungkan baterai + elektroliser.** Tidak perlu fasilitas elektrolisis terpisah. Penghematan massa, volume, dan kompleksitas.

Pada litium-ion, pengisian berlebih = kebakaran. Pada nikel-besi, pengisian berlebih = **produksi hidrogen**.

### Siklus Operasi di Modul Dyson

```
[Operasi normal] Turbin 370 MW beroperasi
  ├→ Konsumsi beban (~320 MW)
  └→ Daya berlebih (~50 MW) → Mode battolyser
       └→ H₂ ~890 kg/jam + O₂ ~7.100 kg/jam akumulasi (dengan asumsi efisiensi elektrolisis ~70%)

[Gerhana (eclipse)] 3-12 jam/tahun
  ├→ Pengosongan baterai (mode ESS)
  └→ H₂ terakumulasi → Pembangkitan listrik fuel cell (paralel)
       → Energi tersedia 2x+ dibanding baterai saja

[Penghentian darurat]
  └→ Penyimpanan ganda H₂/O₂ → Perpanjangan penunjang kehidupan
```

### Melampaui Penyimpanan Energi

H₂ dan O₂ yang dihasilkan battolyser melampaui penyimpanan energi sederhana dan terintegrasi ke dalam **siklus material keseluruhan modul**:

| Produk | Penggunaan | Keterangan |
|--------|-----------|-----------|
| H₂ | Pengisian bahan bakar kapal tunda NTP | Fluida kerja propulsi termal nuklir |
| H₂ | Reduktor dalam proses peleburan | Oksida logam → logam murni (FeO + H₂ → Fe + H₂O) |
| H₂ | Pembangkitan listrik darurat fuel cell | Daya cadangan saat gerhana/pemeliharaan |
| H₂ | Haber-Bosch → NH₃ → pupuk | Pertanian modul habitat |
| O₂ | Penunjang kehidupan (pernapasan) | Esensial untuk modul habitat |
| O₂ | Oksidator (pengelasan, medis) | Proses manufaktur lokal |

Baterai yang menyimpan energi sekaligus memproduksi propelan, reduktor, dan oksigen pernapasan. Litium-ion hanya menyimpan listrik.

---

## "Kepadatan energi 1/10, bukankah terlalu besar?"

Benar. Untuk menyimpan energi yang sama, nikel-besi memerlukan **5-10 kali volume** litium-ion.

Tapi:

```
Skala modul Dyson:
  Cermin: 1 km × 1 km = 1.000.000 m²
  Struktur: beberapa km di belakang cermin
  Total volume: beberapa juta m³

Kapasitas ESS yang diperlukan (12 jam × 370 MW):
  4.440 MWh = 4.440.000 kWh

Nikel-besi (basis 40 Wh/L):
  111.000 m³ = 111 m × 111 m × 9 m

→ Kurang dari 1% total struktur
```

Dalam beberapa juta m³ struktur di belakang cermin 1 km², 111.000 m³ hanyalah **satu sudut**. Selain itu, massa berat baterai nikel-besi dapat dimanfaatkan sebagai **penyeimbang (counterweight) untuk struktur berputar**. Kekurangan berubah menjadi keunggulan.

Pengosongan sendiri yang tinggi ~1% per hari juga hanya masalah di darat. Karena turbin beroperasi 24 jam sehari, 365 hari setahun, baterai selalu dalam keadaan terisi. Pengosongan sendiri **tidak berarti**.

"Bukankah cukup menaikkan output turbin saja tanpa perlu ESS?" Gerhana dan penghentian darurat adalah situasi di mana turbin **benar-benar berhenti**. Pembangkitan dan penyimpanan adalah masalah yang berbeda.

---

## Desain Adaptasi Lingkungan Luar Angkasa

Baterai nikel-besi darat tidak bisa langsung dibawa ke luar angkasa. Diperlukan tiga adaptasi.

### 1. Pencegahan Penguapan Elektrolit

Larutan KOH kehilangan kelembaban melalui penguapan saat terpapar vakum. **Struktur sel tertutup rapat** wajib. Untungnya, sel baterai pada dasarnya sudah didesain tertutup rapat. Untuk penggunaan luar angkasa, cukup meningkatkan tingkat penyegelan.

### 2. Pemisahan Gas di Tanpa Gravitasi

Dalam mode battolyser, gelembung H₂/O₂ menempel di permukaan elektroda. Di Bumi, gaya apung melepaskan gelembung, tapi di tanpa gravitasi tidak bisa.

**Solusi:** Lapisan hidrofobik pada permukaan elektroda + gaya sentrifugal dari rotasi modul sendiri untuk pemisahan gas. Akselerasi sentrifugal ~0,01G sudah cukup untuk pemisahan gelembung.

### 3. Ketahanan Radiasi

Larutan KOH, tidak seperti elektrolit organik, **sangat stabil terhadap radiasi**. Elektrolit organik terdegradasi oleh radiasi yang memutus rantai molekul. Pada larutan air, dekomposisi air oleh radiasi terjadi dalam jumlah kecil, tetapi dipulihkan secara alami melalui rekombinasi. Dalam lingkungan radiasi, nikel-besi **secara inheren lebih unggul** dibanding litium-ion.

---

## Ringkasan Satu Kalimat

Litium-ion adalah baterai terbaik di Bumi. Tapi di asteroid tidak ada litium, di luar angkasa tidak bisa mengganti setiap 10 tahun, dan di ruang hampa tidak bisa memadamkan api. Baterai nikel-besi bisa dibuat dari produk sampingan peleburan asteroid, bertahan 30-50 tahun tanpa penggantian, tidak terbakar, dan setelah terisi penuh berubah menjadi elektroliser yang memproduksi propelan dan oksigen pernapasan. Kepadatan energi 1/10 tidak berarti pada skala km².

Untuk aplikasi terestrial baterai nikel-besi, lihat [Baterai Nikel-Besi sebagai ESS Off-Grid](https://www.parkjunwoo.com/1/tech/iron-nickel-ess-rural-energy/).

![Baterai nikel-besi yang dikembangkan Edison pada 1901. Photo: z22 / Wikimedia Commons / CC BY-SA 3.0](/images/why-iron-nickel-battery.webp)
