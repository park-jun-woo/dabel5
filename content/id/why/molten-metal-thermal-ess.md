---
title: "Mengapa Logam Cair, Bukan Baterai"
date: 2026-02-25T12:00:02+09:00
lastmod: 2026-02-25T12:00:02+09:00
tags: ["penyimpanan-panas-logam-cair", "ESS", "levitasi-elektromagnetik", "penyimpanan-panas", "replikasi-diri"]
image: "/images/molten-metal-thermal-ess.webp"
summary: "Modul Dyson adalah pembangkit surya termal — simpan panas langsung sebagai Fe-Ni cair di tanpa gravitasi. ~145 Wh/kg dengan panas laten, siklus tanpa batas, semua dari bijih asteroid. 58 unit radius 3 m menyelesaikan bottleneck pelepasan."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Penyimpan panas Fe-Ni cair yang melayang secara elektromagnetik di vakum tanpa gravitasi — mempertahankan bentuk bola karena tegangan permukaan. Image: Gemini"
---

## Yang Terlewat di Artikel Sebelumnya

[Artikel sebelumnya](/id/why/why-iron-nickel-battery/) menunjukkan mengapa baterai nikel-besi mengalahkan litium-ion. Tidak ada litium di asteroid, kebakaran tidak bisa dipadamkan di vakum, nikel-besi bertahan 30-50 tahun, dan pengisian berlebih menghasilkan hidrogen.

Semuanya benar. **Tapi ada satu hal yang terlewat.**

Modul Dyson adalah pembangkit listrik tenaga surya termal. Cermin mengumpulkan cahaya, panas memutar turbin. Saat harus menyimpan energi untuk menghadapi eclipse, desain saat ini berjalan seperti ini:

```
Panas matahari (1.600°C) → Turbin → Listrik (370 MW)
                                  → Daya berlebih (~50 MW)
                                       → Baterai (energi kimia)    ← 2 kali konversi
                                       → Saat eclipse → kembali ke listrik  ← 3 kali konversi
```

Panas → listrik → kimia → listrik. **3 kali konversi.** Setiap tahap kehilangan 20-30%.

Bagaimana jika menyimpan panas langsung?

```
Panas matahari (1.600°C) → Sebagian disimpan langsung di tangki panas  ← 0 kali konversi
                         → Saat eclipse → tangki panas → turbin → listrik  ← 1 kali konversi
```

**1 kali konversi.** Perbedaan efisiensi sangat mencolok.

Mengonversi energi berlebih dari pembangkit surya termal ke listrik lalu ke kimia lalu kembali ke listrik — itu seperti mengubah air menjadi uap, memisahkannya menjadi hidrogen dan oksigen, lalu menggabungkannya kembali menjadi air. **Bisa, tapi kenapa?**

Penyimpanan panas adalah jawabannya. Tapi mengapa di Bumi tidak dilakukan?

---

## Mengapa Tidak Bisa di Bumi, Mengapa Bisa di Luar Angkasa

Menyimpan panas dalam logam cair di Bumi adalah topik penelitian akademis, bukan realitas industri. Ada alasannya:

| Masalah | Bumi | Luar Angkasa (vakum tanpa gravitasi) |
|---------|------|--------------------------------------|
| Wadah | Harus menopang berat ribuan ton bahan cair → besar dan mahal | **Tanpa berat sendiri** — dinding tipis, atau tanpa kontak sama sekali |
| Insulasi | Harus memblokir konveksi + konduksi + radiasi semuanya | **Hanya blokir radiasi** — cukup beberapa lapis MLI |
| Kehilangan panas | Tinggi — konveksi udara penyebab utama | **Sangat rendah** — konveksi nol di vakum |
| Korosi | Bahan cair 1.500°C mengikis dinding | **Levitasi elektromagnetik tanpa kontak** → korosi nol |
| Keamanan | Kebocoran = kecelakaan besar | Vakum jadi tidak ada kebakaran, tidak ada medium untuk menyebar |

**Kelemahan di Bumi semuanya hilang atau terbalik di luar angkasa.** Pola yang sama yang berulang dari artikel-artikel sebelumnya — [turbin vs PV](/id/why/why-turbines/), nikel-besi vs litium-ion — struktur yang persis sama.

---

## Penyimpanan Panas dengan Levitasi Elektromagnetik

Fe-Ni cair tetap konduktor listrik pada 1.500°C (kehilangan sifat magnetik di atas titik Curie nikel, tapi konduktivitas tetap ada). Jika medan elektromagnetik bolak-balik diterapkan, arus eddy terinduksi, dan gaya tolak antara arus eddy dan medan magnet memungkinkan **levitasi tanpa kontak**.

Ini adalah teknologi yang digunakan di laboratorium di Bumi. Disebut peleburan [EML (Electromagnetic Levitation)](https://en.wikipedia.org/wiki/Electromagnetic_levitation). Sampel logam beberapa gram hingga beberapa kilogram dilevitasikan di udara dan dilelehkan. Alasan tidak bisa lebih besar di Bumi hanya satu — **gravitasi**. Untuk melawan gravitasi, medan magnet harus kuat, dan medan magnet kuat memakan energi. Beberapa kilogram adalah batasnya.

Di tanpa gravitasi? **Tidak ada gravitasi yang harus dilawan.** Hanya butuh medan magnet minimum untuk stabilisasi posisi. Berapapun — beberapa ton, ratusan ton, puluhan ribu ton.

```
[Penampang Unit Penyimpan Panas]

        ┌─── Dinding Reflektor MLI (insulasi reflektif multilayer) ───┐
        │                                                              │
        │    ┌── Kumparan Elektromagnetik (berpendingin) ──┐          │
        │    │                                              │          │
        │    │   ●●●●●●●●●●●●●●●                          │          │
        │    │   ● Gumpalan Fe-Ni cair  ●                  │          │
        │    │   ● (1.200~1.500°C)      ●                  │          │
        │    │   ●●●●●●●●●●●●●●●                          │          │
        │    │                                              │          │
        │    └──────────────────────────────────────────────┘          │
        │                                                              │
        └──────────────────────────────────────────────────────────────┘
```

Logam cair di tanpa gravitasi secara alami menjadi **bola** karena tegangan permukaan. Bola memiliki rasio luas permukaan terhadap volume minimum — kehilangan panas radiasi minimum. Dinding reflektor MLI memerangkap panas radiasi, medan elektromagnetik menstabilkan posisi, dan tanpa kontak dengan dinding berarti korosi nol.

**Lelehkan Fe-Ni yang ditambang dari asteroid dan biarkan mengambang — itulah tangki penyimpan panas.**

---

## Pengisian dan Pelepasan

```
[Pengisian — Operasi Normal]
Konsentrasi panas matahari → Buka shutter radiasi → Panaskan gumpalan logam → 1.200°C → 1.500°C

[Pelepasan — Saat Eclipse]
Buka shutter radiasi → Panas radiasi gumpalan logam memanaskan heat exchanger → Fluida kerja → Turbin
1.500°C → 1.200°C (memanfaatkan ΔT=300°C)
```

Pengisian: cukup arahkan sebagian panas matahari yang dikumpulkan cermin ke arah tangki penyimpan panas. Buka shutter dan cahaya memanaskan gumpalan logam.

Pelepasan: saat eclipse tiba, buka shutter agar panas radiasi gumpalan logam diterima heat exchanger. Heat exchanger memanaskan fluida kerja dan memutar turbin. Menggunakan turbin yang sama — saat normal cermin adalah sumber panas, saat eclipse tangki penyimpan panas adalah sumber panas. **Dari sudut pandang turbin, hanya sumber panas yang berubah, sisanya sama.**

Media pertukaran panas adalah radiasi. Tidak bisa menancapkan pipa ke benda cair yang melayang tanpa kontak, jadi transfer panas melalui shutter radiasi adalah mekanisme dasarnya. Energi radiasi logam cair 1.500°C sebanding dengan T⁴ menurut hukum Stefan-Boltzmann — cukup kuat.

---

## Kepadatan Energi: Panas Jenis + Panas Laten

Panas jenis paduan Fe-Ni: ~0,5 kJ/(kg·K) = ~0,14 Wh/(kg·K). Jika hanya menghitung **panas sensibel (sensible heat)** yang sebanding dengan perubahan suhu (ΔT):

| Rentang Suhu (ΔT) | Panas Sensibel | Keterangan |
|--------------------|----------------|------------|
| 300°C (1.200→1.500°C) | ~42 Wh/kg | Konservatif |
| 500°C (1.000→1.500°C) | ~70 Wh/kg | Menengah |
| 1.000°C (500→1.500°C) | ~140 Wh/kg | Agresif |

Tapi bukan itu saja.

### Bonus Panas Laten

Titik leleh paduan Fe-Ni adalah ~1.430-1.450°C. Rentang operasi 1.000-1.500°C **melewati** titik leleh ini. Saat pengisian logam meleleh, saat pelepasan logam membeku — perubahan fase (phase change).

Saat material meleleh, suhu tidak naik tapi menyerap panas dalam jumlah besar. Inilah **panas laten peleburan (latent heat of fusion).**

```
Panas laten peleburan besi (Fe): ~270 kJ/kg ≈ 75 Wh/kg
Paduan Fe-Ni: rentang serupa
```

Menggabungkan panas sensibel dan panas laten:

| Rentang Suhu | Panas Sensibel | Panas Laten | **Total** |
|-------------|----------------|-------------|-----------|
| 300°C (1.200→1.500°C) | ~42 | ~75 | **~117 Wh/kg** |
| 500°C (1.000→1.500°C) | ~70 | ~75 | **~145 Wh/kg** |
| 1.000°C (500→1.500°C) | ~140 | ~75 | **~215 Wh/kg** |

**Panas laten saja menggandakan kepadatan energi.** Hanya dengan logam yang meleleh dan membeku, kepadatan energi sudah tumpang tindih dengan batas bawah litium-ion (150-270 Wh/kg).

### Perbandingan ESS (termasuk panas laten)

| Metode | Kepadatan Energi | Umur Siklus | Pengadaan Material |
|--------|-----------------|-------------|-------------------|
| Litium-ion | 150~270 Wh/kg | 3.000~10.000 siklus | Tidak mungkin (tidak ada Li di asteroid) |
| Baterai nikel-besi | 30~50 Wh/kg | Praktis tak terbatas | Fe-Ni asteroid |
| **Penyimpanan panas Fe-Ni cair** | **117~215 Wh/kg** | **Praktis tak terbatas** | **Fe-Ni asteroid** |

Kepadatan energi setara litium-ion, umur siklus tak terbatas, dan materialnya berserakan di asteroid. Dan karena konversi panas → listrik hanya 1 kali, efisiensi sistem juga jauh lebih unggul.

Mengapa umur siklus tak terbatas: ini hanya memanaskan dan mendinginkan gumpalan logam. Tidak ada reaksi kimia. Tidak ada elektroda. Tidak ada elektrolit. Tidak ada yang bisa terdegradasi.

---

## Skala: Mengapa Bukan Satu Bola Raksasa tapi 60 Unit Kecil

Eclipse maksimal 12 jam, output turbin 370 MW. Tidak perlu semuanya ditanggung penyimpanan panas — sel bahan bakar H₂ dan baterai berbagi beban.

### Perhitungan Hibrida

```
Eclipse 12 jam:
  Tangki penyimpan panas: 6 jam
  Sel bahan bakar H₂: 4 jam (akumulasi battolyser tahunan)
  Baterai nikel-besi: 2 jam (respons beban sesaat + cadangan)
```

Tangki penyimpan panas 6 jam (termasuk panas laten):

```
370 MW ÷ 0,30 (efisiensi turbin) = ~1.233 MW(th) × 6h = ~7.400 MWh(th)

ΔT=500°C + basis panas laten (145 Wh/kg):
  Massa diperlukan = 7.400.000 kWh ÷ 0,145 kWh/kg = ~51.000 ton

(Tanpa panas laten 105.000 ton → bonus panas laten memotong massa setengah)
```

Jika 51.000 ton dimasukkan dalam satu bola, radiusnya ~12 m. Secara intuitif sederhana. **Tapi ini tidak bisa dilakukan.** Ada tiga alasan teknis.

### Alasan 1: Luas Permukaan Tidak Cukup saat Pelepasan

Saat eclipse, penyimpan panas mentransfer panas ke heat exchanger **hanya melalui radiasi**. Output radiasi sebanding dengan luas permukaan (P = epsilon sigma A T⁴).

Bola adalah bentuk dengan rasio luas permukaan terhadap volume minimum. Optimal untuk **menyimpan** panas, tapi menjadi bottleneck saat harus **melepaskan** panas dengan cepat.

```
Output panas diperlukan: ~1.233 MW(th)

Output radiasi 1.500°C (1.773K) (epsilon=0,5):
  P/A = epsilon x sigma x T⁴ = 0,5 x 5,67e-8 x 1.773⁴ ≈ 280 kW/m²

Luas permukaan diperlukan: 1.233.000 kW ÷ 280 kW/m² ≈ 4.400 m²

Luas permukaan bola tunggal radius 12 m: 4pi(12)² ≈ 1.810 m² → tidak cukup (41% dari kebutuhan)
```

**Bola tunggal secara fisik tidak bisa melepaskan panas yang diperlukan.** Luas permukaannya bahkan kurang dari setengah.

Dipecah menjadi ~58 unit radius 3 m:

```
Luas permukaan 1 unit: 4pi(3)² ≈ 113 m²
Total luas 58 unit: 113 x 58 ≈ 6.560 m² → cukup, 149% dari kebutuhan (ada margin)
Massa 1 unit: (4/3)pi(3)³ x 7.800 ≈ 880 ton
```

**Saat menyimpan, setiap unit mempertahankan bentuk bola untuk meminimalkan kehilangan, dan saat melepaskan, total luas permukaan banyak unit menjamin output panas yang memadai.** Kelemahan bentuk bola diatasi dengan jumlah unit.

### Alasan 2: Sloshing — Bola Wrecking 100.000 Ton Lava

Saat 51.000 ton logam cair melayang sebagai satu bola, jika modul sedikit saja berotasi atau bergetar untuk kontrol sikap, **gelombang besar (sloshing)** terjadi di dalamnya. Ditambah ketidakstabilan magnetohidrodinamika (MHD), gumpalan lava ini bisa bergoyang-goyang dan menembus kurungan medan elektromagnetik.

Dengan unit radius 3 m, 880 ton? Energi fluida sebanding dengan pangkat tiga ukuran unit sehingga **energi sloshing setiap unit kurang dari 1/10.000 dibanding bola tunggal**. Risiko pelepasan kurungan praktis tereliminasi.

### Alasan 3: Ekspansi Volume saat Perubahan Fase

Berpindah antara 1.200°C (padat) dan 1.500°C (cair), Fe-Ni mengalami ekspansi dan kontraksi berulang. Jika bola radius 12 m mendingin dari luar, cangkang padat terbentuk, dan saat cairan internal menyusut, **cangkang bisa pecah dan serpihan terpental ke vakum**. Unit kecil memiliki gradien suhu internal-eksternal yang seragam sehingga masalah ini teratasi.

### Kesimpulan Desain

```
Spesifikasi Unit Penyimpan Panas:
  Bentuk: Bola (terbentuk alami oleh tegangan permukaan)
  Radius: ~3 m
  Massa: ~880 ton/unit
  Jumlah unit: ~58 (per modul)
  Total massa: ~51.000 ton
  Penempatan: Didistribusikan di struktur belakang cermin (berfungsi juga sebagai counterweight)

Performa Pelepasan:
  Total luas permukaan: ~6.560 m² (149% dari kebutuhan 4.400 m²)
  Margin output 1.233 MW(th) terjamin
```

51.000 ton tidak perlu diadakan secara terpisah. Fe-Ni yang dilebur dari asteroid **dibiarkan cair tanpa dipadatkan dan jadilah unit penyimpan panas**. Didistribusikan di struktur modul juga berfungsi sebagai **counterweight**.

---

## ESS 3 Tier: Pemisahan Peran

Baterai tidak perlu lagi menanggung bulk ESS. Teknologi optimal ditempatkan di setiap tier:

```
Tier 1 — Bulk (skala jam)
  └→ Tangki penyimpan panas logam cair
       Pengisian: Panas matahari langsung
       Pelepasan: Penyimpan panas → turbin → listrik
       Peran: Respons eclipse, kehilangan konversi minimum

Tier 2 — Buffer (skala detik~menit)
  └→ Baterai nikel-besi
       Pengisian: Daya berlebih
       Pelepasan: Elektrokimia (respons ms)
       Peran: Respons beban sesaat, daya start-up

Tier 3 — Darurat + Produksi Kimia
  └→ H₂/O₂ (output battolyser)
       Pembangkitan darurat sel bahan bakar
       Propelan, reduktor, oksigen pernapasan
       Cadangan sekunder saat eclipse berkepanjangan
```

### Yang Diberikan Struktur Ini

**Bank baterai berkurang drastis.** Dalam desain sebelumnya, menanggung eclipse 12 jam hanya dengan baterai memerlukan 111.000 m³. Jika penyimpan panas menanggung bulk, baterai hanya 2 jam — berkurang ke beberapa ribu m³.

**Peran battolyser menjadi jelas.** Artikel sebelumnya menjelaskan battolyser (elektrolisis air saat pengisian berlebih) sebagai menggabungkan fungsi ESS dan produksi kimia. Jika penyimpan panas menanggung bulk ESS, battolyser diposisikan sebagai **pabrik kimia** — produksi propelan hidrogen, oksigen, dan reduktor adalah tugas utamanya, dan pembangkitan darurat adalah tugas sampingan.

**Materialnya sama.** Penyimpan panas = Fe-Ni cair. Baterai = elektroda Fe-Ni. Battolyser = baterai yang sama dengan pengisian berlebih. Ketiga tier semuanya berasal dari Fe-Ni asteroid. Tidak ada bahan baku baru yang ditambahkan ke siklus replikasi diri.

---

## Hubungan dengan Artikel Sebelumnya (Baterai Nikel-Besi)

Tesis utama artikel sebelumnya **semuanya tetap valid:**

- Tidak ada litium di asteroid → tetap berlaku
- Umur 30-50 tahun baterai nikel-besi → tetap berlaku
- Risiko kebakaran di vakum → tetap berlaku
- Produksi H₂/O₂ battolyser → tetap berlaku
- Dapat diproduksi lokal → tetap berlaku

**Yang dilengkapi:** Artikel sebelumnya bisa terbaca seolah baterai nikel-besi sendirian menanggung bulk ESS (respons eclipse 12 jam). Kenyataannya, untuk penyimpanan energi bulk, penyimpanan panas jauh lebih unggul, dan baterai bersinar di domainnya sendiri yaitu respons sesaat.

**Masing-masing melakukan yang terbaik.** Tungku penyimpan panas untuk penyimpanan panas berjam-jam. Baterai untuk respons daya dalam milidetik. Sel bahan bakar untuk respons darurat + produksi kimia. Tidak perlu satu teknologi menanggung semuanya.

---

## Ringkasan Satu Kalimat

Modul Dyson adalah pembangkit surya termal, tapi mengonversi panas ke listrik lalu ke kimia lalu kembali ke listrik adalah kehilangan konversi tiga kali lipat. Melelehkan Fe-Ni asteroid dan melevitasikannya di tanpa gravitasi menjadi tangki penyimpan panas dengan 0 kali konversi pengisian, 1 kali konversi pelepasan. Dengan panas laten perubahan fase, kepadatan energi ~145 Wh/kg — setara litium-ion. 58 unit radius 3 m yang didistribusikan menyelesaikan bottleneck luas permukaan pelepasan, sloshing, dan ekspansi perubahan fase. Semua material dari Fe-Ni asteroid yang sama.

![Penyimpan panas Fe-Ni cair yang melayang secara elektromagnetik di vakum tanpa gravitasi. Image: Gemini](/images/molten-metal-thermal-ess.webp)
