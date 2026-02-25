---
title: "Mengapa 28nm"
date: 2026-02-25T12:00:03+09:00
lastmod: 2026-02-25T12:00:03+09:00
tags: ["28nm", "semikonduktor", "TPU", "replikasi-diri", "litografi-ArF"]
image: "/images/why-28nm.webp"
summary: "3nm mutakhir tidak bisa dibuat tanpa EUV monopoli ASML — mustahil di luar angkasa. 28nm bisa dibuat hanya dengan ArF, dan Google TPU v1 membuktikan 92 TOPS secara nyata. Silikon keluar dari slag, dan luar angkasa itu sendiri adalah cleanroom."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Foto die chip gerbang NAND 4-input tipe TTL — 7 transistor, lebar garis minimum 20 um (1968). Photo: Dgarte / Wikimedia Commons / CC BY-SA 3.0"
---

## "Katanya replikasi diri, lalu chip dari mana?"

Artikel-artikel sebelumnya menunjukkan bahwa cermin, struktur, [turbin](/id/why/why-turbines/), [baterai](/id/why/why-iron-nickel-battery/), [manajemen panas](/id/why/heat-flow/) — semuanya bisa dibuat dari Fe-Ni asteroid. Siklus replikasi diri hampir tertutup.

Hampir.

**Chip AI masih diimpor dari Bumi.** Operasi otonom modul Dyson — kontrol robot penambangan, penyesuaian orbit, manajemen proses peleburan, penunjang kehidupan habitat — semuanya dilakukan AI. Tanpa chip, modul adalah buta.

"Tidak ada litium di asteroid" adalah game over bagi baterai litium-ion, sama halnya **"tidak bisa membuat EUV di luar angkasa" adalah game over bagi 3nm mutakhir.**

Lalu proses apa yang digunakan untuk membuat chip?

---

## Mengapa Bukan 3nm Mutakhir

Inti dari proses semikonduktor adalah litografi — proses mencetak pola sirkuit ke wafer menggunakan cahaya.

| Item | 28nm | 3~5nm (mutakhir) |
|------|------|-------------------|
| Litografi | **ArF immersion** (Nikon, Canon, ASML) | **EUV** (monopoli ASML, ribuan miliar won per unit) |
| Ketersediaan peralatan | Pasar matang, bekas melimpah | Sangat terbatas, subjek kontrol ekspor |
| Kompleksitas desain | Single patterning | Multi patterning (sangat kompleks) |
| Biaya konstruksi fab | ~$3~5B | ~$20~30B |
| Yield | Tinggi (terverifikasi 10+ tahun) | Awal rendah |

Scanner EUV (extreme ultraviolet) **hanya dibuat oleh satu perusahaan di seluruh Bumi — ASML.** Satu pabrik di Veldhoven, Belanda. Subjek kontrol ekspor. Peralatan yang aliansi AS-Jepang-Belanda blokir dari penjualan ke China. Mereproduksi ini di luar angkasa? Mustahil.

Proses paling kuat yang tidak memerlukan EUV. Itu adalah **28nm**.

"Bukankah 7nm bisa dengan ArF?" — Bisa. Dengan teknik multi patterning yang menembakkan cahaya ArF berkali-kali untuk membuat pola lebih halus. Tapi kompleksitas desain meledak dan yield anjlok. Sebelum memiliki tenaga dan infrastruktur untuk manajemen yield di luar angkasa, ini tidak realistis.

"Bukankah 65nm lebih mudah dibuat?" — Benar. Tapi performa per chip terlalu rendah. Untuk pekerjaan yang sama, jumlah chip meledak, dan lebih banyak chip berarti wiring, packaging, dan cooling bertambah secara proporsional. Mudah dibuat tapi seluruh sistem jadi lebih sulit.

**28nm = integrasi optimal yang bisa dibuat tanpa EUV.**

---

## Ini Bukan Teori — Google TPU v1

"Bisakah AI benar-benar berjalan di 28nm?"

Google memberikan jawabannya pada 2015. **[TPU v1](https://arxiv.org/abs/1704.04760).** Diproduksi dengan proses 28nm, lebih dari 100.000 unit diterapkan di pusat data mereka sendiri sebagai akselerator AI produksi.

| Item | Google TPU v1 (pengukuran aktual) |
|------|-----------------------------------|
| Proses | 28nm |
| Arsitektur | Systolic array 256 x 256 |
| Komputasi | 92 TOPS (INT8) ≈ 23 TFLOPS (FP16) |
| Konsumsi daya | ~75W operasi nyata |
| Pemanfaatan silikon | **90%+** |

Arsitektur systolic array adalah kuncinya. GPU adalah chip serbaguna sehingga 70% silikonnya digunakan untuk logika kontrol, cache, dan scheduler. Yang benar-benar melakukan operasi matriks hanya 30%. Systolic array adalah arsitektur yang dirancang khusus untuk perkalian matriks, sehingga **90%+ silikon digunakan untuk komputasi aktual.**

Jika hanya menjalankan AI, overhead serbaguna GPU semuanya pemborosan. TPU adalah chip yang menghilangkan pemborosan itu.

Dan ini bukan proposal di dalam paper. **Ini chip yang menjalankan AlphaGo.** Hardware yang benar-benar diterapkan dalam layanan nyata di pusat data Google selama bertahun-tahun.

---

## "4,6 kali konsumsi listrik?"

Chip AI performa tertinggi di Bumi saat ini: NVIDIA H100. Proses 4nm, 990 TFLOPS, konsumsi daya 700W.

Satu TPU v1 menghasilkan 23 TFLOPS. Untuk menyamai komputasi satu H100?

```
990 TFLOPS ÷ 23 TFLOPS = 43 kartu

43 kartu x 75W = 3.225W ≈ 3,2 kW
```

| | TPU v1 x 43 kartu | H100 x 1 kartu |
|---|---|---|
| FP16 gabungan | ~990 TFLOPS | ~990 TFLOPS |
| Total daya | **3,2 kW** | 700W |
| Rasio daya | **4,6x** | Acuan |

4,6 kali. Di Bumi, ini adalah kesenjangan fatal. Di dunia di mana biaya listrik adalah 30-40% dari biaya operasional pusat data, perbedaan daya 4,6 kali berarti kebangkrutan.

**Di luar angkasa?**

1 modul Dyson = 370 MW. 3,2 kW adalah **0,00086%** dari 370 MW. Dalam luas cermin, itu 2,4 m² — setara satu piksel dari cermin Dyson 1 km².

Di Bumi, daya adalah uang. **Di luar angkasa, daya adalah luas cermin.** Cermin dibuat dari Fe-Ni asteroid yang dipipihkan.

Struktur logika yang sama seperti ketika [turbin mengalahkan panel surya di artikel sebelumnya](/id/why/why-turbines/). Pilihan yang inferior menurut standar Bumi terbalik menjadi satu-satunya pilihan menurut standar luar angkasa. **Ketika standar berubah, jawaban berubah.**

---

## 1 Modul = Pusat Data Setara 30.000 H100

Jika 30% dari 370 MW modul dialokasikan untuk komputasi AI:

```
111 MW ÷ 75W/chip = ~1.480.000 kartu (1,48 juta TPU v1)

1,48 juta ÷ 43 kartu/H100 setara = ~34.000 H100

Overhead interconnect dan cooling 20-30% → secara konservatif setara ~25.000-30.000 H100
```

Setara dengan kluster AI terbesar di Bumi tahun 2026. **Itu satu modul.**

Jika 270.000 modul bereplikasi? Setara miliaran H100. Kapasitas komputasi yang melampaui seluruh kemampuan komputasi umat manusia saat ini — dari satu asteroid.

---

## Bahan Baku: Chip AI dari Slag

Di sinilah bagian paling indah dari desain ini. Tidak perlu tambang semikonduktor terpisah.

Saat bijih asteroid dilebur, Fe-Ni (90%+) adalah produk utama, dan **sisanya adalah slag**. Komponen utama slag adalah SiO₂ — silikat. Ini tidak dibuang.

```
Bijih asteroid → Peleburan vakum
  ├→ Fe-Ni (90%+) → Cermin, struktur, baterai, turbin
  └→ Slag (komponen utama SiO₂)
       ├→ Sebagian besar → Perisai radiasi
       └→ Sebagian → Reduksi karbon (SiO₂ + 2C → Si + 2CO)
            → Silikon logam
            → Zone refining (panas matahari + vakum + mikrogravitasi)
            → Ingot kristal tunggal kelas semikonduktor (kemurnian 9N+)
            → Wafer 300mm
            → TPU 28nm
```

**Chip AI keluar dari limbah peleburan.**

[Zone refining](https://en.wikipedia.org/wiki/Zone_melting) menguntungkan di luar angkasa karena alasan tertentu. Ini adalah metode pemurnian yang melewatkan zona cair sempit (molten zone) melalui ingot silikon untuk mendorong keluar pengotor:

- **Energi:** Pemanasan langsung panas matahari. Biaya nol
- **Vakum:** Luar angkasa sudah vakum. Pengotor menguap otomatis
- **Mikrogravitasi:** Zona cair tidak mengalir ke bawah. Metode FZ (Float Zone) di Bumi terbatas pada diameter ingot 200mm — lebih besar dari itu silikon cair runtuh karena gravitasi. **Tanpa gravitasi, 300mm ke atas juga bisa**
- **Pengulangan:** Cukup sesuaikan sudut cermin untuk mengulang pass pemurnian tanpa batas. Biaya tambahan nol

Di Bumi, zone refining adalah proses premium yang mahal dan berskala kecil. Di luar angkasa, ia menjadi **proses standar**.

---

## Fab: Luar Angkasa Adalah Cleanroom

Salah satu item biaya terbesar fab 28nm di Bumi: cleanroom Kelas 1-10. Partikel berdiameter 0,5 um atau lebih tidak boleh lebih dari 10 per kaki kubik udara. Untuk mempertahankan ini diperlukan sistem filter HEPA raksasa, air handling unit, dan manajemen tekanan positif. Sebagian besar biaya konstruksi fab masuk ke sini.

Luar angkasa **tidak ada udara.** Sumber kontaminasi partikel tidak ada. Vakum adalah **cleanroom sempurna**.

Kesesuaian luar angkasa per tahap dari 7 proses utama:

| Proses | Kesesuaian Luar Angkasa | Alasan |
|--------|------------------------|--------|
| Pertumbuhan ingot | **Keunggulan luar angkasa** | Metode FZ mikrogravitasi, ingot berdiameter besar |
| Slicing wafer | Bisa | Proses mekanis, tidak tergantung lingkungan |
| Oksidasi/deposisi (CVD, PVD) | **Vakum menguntungkan** | Di Bumi harus membuat vakum di chamber — luar angkasa sudah vakum |
| Fotolitografi | Bottleneck | Scanner ArF dan photoresist tergantung Bumi |
| Etching | **Vakum menguntungkan** | Penyederhanaan chamber plasma etching |
| Implantasi ion | **Vakum menguntungkan** | Pengurangan hamburan beam, tidak perlu pompa vakum tinggi |
| Wiring/packaging | Bisa | Cu diperoleh dari asteroid/Bulan |

**6 dari 7 tahap menguntungkan atau setara di luar angkasa.** Satu-satunya bottleneck adalah fotolitografi — scanner ArF sendiri tidak bisa dibuat di luar angkasa. Tapi sekali dibawa, bisa dipakai puluhan tahun.

---

## Manajemen Panas Fab: "Membuat Semikonduktor di Luar Angkasa?"

"Sisi menghadap matahari ratusan derajat, sisi membelakangi minus 100 derajat, dan bisa mengontrol ±0,01°C?"

Benar. Dan **lebih mudah dari di Bumi.**

### Inti Masalah

Sistem lensa proyeksi scanner litografi ArF sangat sensitif terhadap ekspansi termal. Variasi suhu 0,01°C mengubah kelengkungan lensa, menciptakan error overlay, dan menurunkan yield. Toleransi overlay proses 28nm adalah beberapa nm.

Bagaimana fab di Bumi menyelesaikan ini:
- Seluruh cleanroom dijaga konstan 23,00 ± 0,1°C
- Di dalam scanner, sirkuit pendingin terpisah mengontrol ±0,01°C
- **Masalah:** Gangguan eksternal terus-menerus masuk — variasi suhu luar, musim, siang-malam, cuaca, gempa, getaran jalan, panas peralatan sekitar

### Desain Termal Fab Luar Angkasa

```
[Penampang Modul Fab]

Luar: Vakum luar angkasa (konduksi nol, konveksi nol)
  │
  ├─ Dinding reflektor MLI (insulasi reflektif multilayer, puluhan lapis)
  │    → Tingkat blokir radiasi matahari 99,5%+
  │    → Juga memblokir kehilangan radiasi dalam→luar
  │
  ├─ Dinding struktur luar (Fe-Ni)
  │
  ├─ Lapisan sirkulasi cairan aktif
  │    → Sirkulasi mikro air ultramurni (UPW)
  │    → Kontrol aktif dengan pompa + heater + valve radiasi
  │    → Dinding dalam seragam 23,00 ± 0,05°C
  │
  └─ Interior fab (atmosfer N₂ 1 atm)
       → Panas peralatan → diserap pendingin sirkulasi
       → Di dalam scanner: loop pendingin khusus ±0,01°C
```

### Mengapa Lebih Mudah dari di Bumi

| Item | Fab Bumi | Modul Fab Luar Angkasa |
|------|----------|------------------------|
| Gangguan suhu eksternal | Terus-menerus (cuaca, musim, siang-malam) | **Tidak ada** — insulasi vakum |
| Getaran eksternal | Jalan, gempa, pabrik sekitar | **Tidak ada** — luar angkasa tanpa getaran |
| Biaya insulasi | HVAC mengonsumsi 30-40% daya fab | **Vakum adalah insulator gratis** |
| Prediktabilitas sumber panas | Gangguan eksternal + peralatan internal | **Hanya peralatan internal** (sepenuhnya dapat diprediksi) |
| Pembuangan panas | Menara pendingin, chiller (konsumsi air dan listrik besar) | **Radiator** (radiasi vakum) |

Paradoks kunci: lingkungan termal ekstrem luar angkasa (ratusan derajat vs minus 100 derajat) **tidak sampai ke interior fab.** Vakum adalah insulator terbaik, dan jika MLI memblokir radiasi, interior fab terisolasi secara termal sepenuhnya dari luar. Setelah itu tinggal mengelola panas peralatan internal saja, dan ini lebih mudah dari di Bumi — karena gangguan eksternal nol.

Alasan fab Bumi menggunakan 30-40% total dayanya untuk HVAC adalah karena **terus-menerus melawan lingkungan luar**. Fab luar angkasa tidak memiliki pertarungan itu sama sekali.

### UPW — Dari Battolyser

Air ultramurni (UPW) yang digunakan untuk sirkulasi termal fab bukan dari pabrik pengolahan air terpisah melainkan dari output battolyser:

```
Battolyser: H₂O → H₂ + O₂ (elektrolisis)
Reaksi balik: H₂ + O₂ → H₂O (sel bahan bakar)

Produk sampingan H₂O → pemurnian → UPW
  ├→ Pendingin sirkulasi termal fab
  ├→ Pembersihan wafer
  └→ Cairan litografi immersion
```

### Kompartemen Gravitasi Buatan

Litografi immersion memerlukan film tipis air ultramurni di atas wafer — memerlukan gravitasi. Modul fab dibagi dua kompartemen:

```
Kompartemen vakum (0G):
  ├→ Deposisi CVD/PVD (memerlukan vakum)
  ├→ Implantasi ion (memerlukan vakum)
  └→ Plasma etching (memerlukan vakum)

Kompartemen gravitasi buatan (~1G rotasi):
  ├→ Litografi ArF immersion (memerlukan gravitasi untuk manajemen cairan)
  ├→ Pembersihan basah (memerlukan gravitasi untuk pembersihan UPW)
  └→ Penanganan wafer (transfer robotik)
```

Wafer berpindah antara kompartemen vakum dan gravitasi buatan melalui airlock. Kompartemen rotasi tidak memiliki sumber getaran eksternal sehingga **hanya perlu mengelola keseragaman rotasi itu sendiri** — jauh lebih sederhana dari mempertahankan diri melawan gempa dan getaran jalan di Bumi.

---

## Ketergantungan Eksternal: 5%

| Kategori | Sumber | Keterangan |
|----------|--------|------------|
| Silikon | Lokal (slag → Si) | |
| Energi | Lokal (panas matahari) | |
| Cleanroom | Lokal (vakum luar angkasa) | |
| Air ultramurni | Lokal (H₂O battolyser → pemurnian) | |
| Wiring tembaga | Lokal (asteroid/Bulan) | |
| Scanner ArF | **Bumi 1 kali** | Umur puluhan tahun |
| Photoresist | **Bumi 1 kali/tahun** | Ratusan kg per tahun |
| Gas etching | **Bumi 1 kali/tahun** | Didaur ulang, jumlah kecil |
| Elemen doping (B, As) | **Bumi 1 kali/tahun** | Puluhan kg |

95% diperoleh di luar angkasa. Sisa 5% — scanner ArF (1 kali pertama) + bahan habis pakai (beberapa ton per tahun) — bisa dimuat puluhan tahun sekaligus dalam satu peluncuran Starship.

"Photoresist adalah kimia organik presisi, bukan?" — Benar. Ini sulit diproduksi lokal. Tapi konsumsi tahunannya ratusan kg. Satu Starship bisa membawa puluhan tahun persediaan. Bukan swasembada penuh tapi **swasembada de facto**.

---

## Siklus Replikasi Diri Tertutup

```
Sebelumnya:
  Bijih asteroid → Peleburan → Fe-Ni → Cermin, struktur, baterai → Replikasi diri
                                                                    ↑
                                                            Chip AI impor dari Bumi ❌

Sekarang:
  Bijih asteroid → Peleburan → Fe-Ni → Cermin, struktur, baterai, turbin
                             → Slag → Ingot Si → TPU 28nm → Kontrol otonom AI
                                                            ↓
                                                    Siklus replikasi diri tertutup penuh ✅
```

Cermin membuat cermin. Baterai membuat propelan. **Slag membuat chip AI.** Tidak ada yang terbuang.

---

## Ringkasan Satu Kalimat

3nm mutakhir tidak bisa dibuat tanpa EUV monopoli ASML — mustahil di luar angkasa. 28nm bisa dibuat hanya dengan ArF, dan Google TPU v1 membuktikan 92 TOPS secara nyata. Kerugian daya 4,6 kali hanyalah selisih 2,4 m² cermin pada modul 370 MW. Silikon keluar dari slag, luar angkasa itu sendiri adalah cleanroom, dan insulasi vakum membuat manajemen termal ±0,01°C lebih mudah dari di Bumi. Mata rantai terakhir siklus replikasi diri.

![Foto die chip gerbang NAND 4-input tipe TTL. Photo: Dgarte / Wikimedia Commons / CC BY-SA 3.0](/images/why-28nm.webp)
