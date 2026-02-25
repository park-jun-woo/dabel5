---
title: "Mengapa Panas Tidak Bisa Dialirkan Lewat Pipa"
date: 2026-02-24T12:00:08+09:00
lastmod: 2026-02-24T12:00:08+09:00
tags: ["manajemen-termal", "radiator", "kaskade-panas"]
summary: "Tidak ada fluida yang tahan 1.600°C dalam sirkuit tertutup. Setiap fasilitas menerima cermin sendiri, membuang panas sisa pada suhu tertinggi yang memungkinkan, dan hanya sisa di bawah 100°C yang sampai ke habitat."
image: "/images/post008.webp"
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## PR dari Artikel Sebelumnya

Artikel sebelumnya berargumen bahwa turbin lebih unggul daripada PV untuk replikasi diri. Efisiensi 30%, output listrik 370 MW, sisanya 855 MW adalah panas.

Dan ditulis:

> "70% yang sama melewati peleburan, pabrik, habitat, dan pusat data secara berurutan — semuanya terpakai."

Secara konsep benar. Panas buang turbin jauh lebih berguna daripada panas buang PV di 60°C. **Tapi "lewat berurutan" bukan desain sesungguhnya.** Artikel ini menelusuri aliran panas yang sebenarnya.

---

## Koreksi Dulu: Mengapa "Lewat Berurutan" Tidak Bisa

### Masalah 1: Suhu panas buang turbin

Termodinamika turbin (siklus Brayton):
- Sisi panas: ~1.200°C (fluida kerja dipanaskan oleh cahaya matahari terkonsentrasi)
- Sisi dingin: ~227°C (panas dibuang di sini)
- Efisiensi 30% → 370 MW listrik, **855 MW dibuang pada ~227°C**

Poin kunci: **Seluruh panas buang turbin keluar pada ~227°C.** Peleburan butuh 1.600°C. Anda tidak bisa menjalankan proses 1.600°C dengan panas 227°C — hukum kedua termodinamika. Panas hanya mengalir dari panas ke dingin.

Panah "800–1.000°C → peleburan" di diagram sebelumnya bukan panas buang turbin. Panas peleburan datang **langsung dari cermin**.

### Masalah 2: Tidak ada media yang mampu membawa 1.000°C

Seandainya ada panas 1.600°C di suatu tempat, bisakah disalurkan melalui pipa ke fasilitas lain?

| Media transfer panas | Suhu operasi maks | Batasan |
|---|---|---|
| Air bertekanan | ~340°C | Titik kritis |
| Garam cair | ~565°C | Dekomposisi |
| Natrium cair | ~800°C | Tekanan uap |
| Helium tekanan tinggi | ~950°C | Batas material pipa |
| **Di atas 1.000°C** | **N/A** | **Tidak ada media** |

Tidak ada fluida yang mampu membawa panas 1.600°C. Satu-satunya cara mengirim energi pada suhu ini: **cahaya.** Iradiasi langsung oleh cermin.

### Masalah 3: Jarak antar modul

Dalam klaster terspesialisasi, modul peleburan dan modul pusat data terpisah **50–100 km.** Pemisahan disengaja untuk menghindari getaran, kontaminasi, dan interferensi termal. Pada jarak ini perpipaan panas tidak praktis.

**Kesimpulan: Menyalurkan panas buang turbin ke proses suhu tinggi secara fisika mustahil.**

---

## Desain Sesungguhnya: Setiap Fasilitas Mendapat Cermin Sendiri

Prinsip sejati aliran panas:

1. **Panas masuk diterima langsung dari cermin masing-masing modul** — ditransmisikan sebagai cahaya, tanpa media
2. **Kaskade hanya bekerja di dalam setiap modul** — panas buang proses digunakan ulang pada suhu yang makin rendah
3. **Tidak ada transfer panas antar modul** — batasan jarak dan media
4. **Hanya panas buang di bawah 100°C yang disuplai ke habitat** — perpipaan layak, suhu cocok dengan kebutuhan habitat

### Alokasi Cermin (klaster 10 modul)

| Jenis modul | Jml | Pembagian cermin (panas : daya) | Sumber suhu tinggi |
|---|---|---|---|
| Modul peleburan | 3 | 90 : 10 | Cermin → langsung 1.600°C |
| Modul ingot | 1 | 70 : 30 | Cermin → langsung 1.400°C |
| Modul struktural | 2 | 60 : 40 | Cermin → langsung 800–1.200°C |
| Modul fab | 1 | 20 : 80 | Cermin → langsung 900°C |
| Pusat data | 2 | 5 : 95 | Cermin → turbin → listrik |
| Habitat / logistik | 1 | 30 : 70 | Cermin → turbin → listrik |

**Di atas 1.000°C, cahaya menyampaikan panas secara langsung.** Turbin hanya beroperasi di modul yang utamanya butuh listrik (pusat data, habitat).

---

## Fisika Radiator: Hukum T⁴

Satu-satunya cara membuang panas di ruang angkasa: **radiasi inframerah.** Tidak ada konveksi, tidak ada konduksi.

Hukum Stefan-Boltzmann:

**Daya radiasi = ε × σ × A × T⁴**

(ε: emisivitas, σ: konstanta Stefan-Boltzmann, A: luas, T: suhu absolut)

Kuncinya **T⁴**. Suhu 2× lipat, daya radiasi 16× lipat. Sebaliknya, luas yang dibutuhkan untuk beban panas sama menyusut jadi 1/16.

| Suhu radiator | Luas per MW | Analogi |
|---|---|---|
| 800°C (1.073K) | **8 m²** | Satu slot parkir |
| 400°C (673K) | **50 m²** | Satu apartemen |
| 227°C (500K) | **166 m²** | Lapangan tenis |
| 100°C (373K) | **535 m²** | Tiga lapangan basket |
| 60°C (333K) | **844 m²** | 1/8 lapangan sepak bola |

(Radiasi dua sisi, emisivitas ε = 0,85, lembaran Fe-Ni tanpa pelapis)

**Pelajaran: Panas yang butuh 8 m² untuk dibuang pada 800°C membutuhkan 844 m² pada 60°C. Lebih dari 100×.**

Maka prinsip inti manajemen termal: **"Buang panas yang tak bisa digunakan pada suhu tertinggi yang mungkin, segera."**

### Material Radiator

Radiator berada dalam loop replikasi diri:
- **Material:** Lembaran tipis Fe-Ni dari asteroid
- **Permukaan:** Tanpa pelapis aluminium (kebalikan cermin) — Fe-Ni tanpa pelapis memiliki emisivitas inframerah tinggi, ideal untuk radiasi
- **Fabrikasi:** Jalur lembaran logam yang sama dengan bingkai cermin. Hanya langkah pelapis yang dilewati
- **Sumber daya tambahan:** Nol. Material sama, proses sama, produk berbeda

---

## Aliran Panas per Fasilitas

### Modul Peleburan — Panas Jadi Bintang (90% panas, 10% daya)

Modul peleburan menerima 90% energi cermin sebagai panas langsung. Turbin kecil (10%) menghasilkan listrik untuk motor dan robot.

```
☀️ Cermin khusus (90% → iradiasi langsung, 10% → turbin kecil)
 │
 ▼
Tungku peleburan (1.600°C) ← Dipanaskan langsung oleh cahaya cermin, tanpa media
 │
 │ Panas buang ~800°C ← Dari sini media (He / logam cair) bisa membawa
 ├→ Perlakuan panas paduan, anil (pakai 800°C)
 ├→ Surplus → ★ Radiator A (800°C) — 8 m²/MW, kompak
 │
 │ Panas buang ~400°C
 ├→ Pemanasan awal, pemanasan bantu (pakai 400°C)
 ├→ Surplus → ★ Radiator B (400°C) — 50 m²/MW, sedang
 │
 │ Panas buang ~200°C
 ├→ ★ Radiator C (200°C) — sebagian besar dibuang di sini
 │
 │ Sisa <100°C
 └→ Bisa disalurkan ke habitat melalui pipa

Panas buang turbin kecil (~227°C) → ★ Radiator D
```

Modul peleburan menggunakan panas dari atas ke bawah, **meradiasikan surplus di setiap tahap.** Radiator suhu tinggi berukuran kecil sehingga bebannya ringan. Hanya sisa di bawah 100°C yang dikirim ke habitat.

### Modul Pusat Data — Listrik Jadi Bintang (5% panas, 95% daya)

Pusat data adalah modul tersulit untuk didinginkan. 95% energi cermin melewati turbin → listrik → chip → panas, semuanya keluar pada ~60°C.

```
☀️ Cermin khusus (95% → turbin besar, 5% → panas bantu)
 │
 ▼
Turbin besar → listrik kelas ~370 MW
 │
 │ Panas buang turbin ~227°C (~855 MW)
 └→ ★ Radiator A (227°C) — 166 m²/MW
     Sebagian besar panas buang turbin dibuang di sini

Operasi chip → seluruh listrik menjadi panas
 │
 │ Panas chip ~60°C
 │  Radiasi langsung pada 60°C: 844 m²/MW → 111 MW butuh ~94.000 m²
 │
 ├→ [Pompa panas] 60°C → 200°C (COP ~3, daya ~37 MW)
 │   └→ ★ Radiator B (200°C) — luas menyusut ~1/4
 │
 └→ Sisa <100°C → bisa disuplai ke habitat
```

**Pompa panas adalah teknologi kunci.** Menaikkan panas 60°C ke 200°C memangkas luas radiator secara drastis. Daya pompa (~37 MW) berasal dari output turbin sendiri. Turbin maupun pompa panas bisa dibuat di tempat dari Fe-Ni + Ti.

### Modul Struktural (60% panas, 40% daya)

```
☀️ Cermin khusus (60% → pemanasan langsung, 40% → turbin)
 │
 ▼
Pengelasan / perlakuan panas (800–1.200°C) ← Pemanasan langsung cermin
 │ Panas buang ~400°C
 ├→ Pemanasan awal pembentukan / tekuk (pakai 400°C)
 ├→ Surplus → ★ Radiator (400°C)
 │ Panas buang ~200°C
 ├→ ★ Radiator (200°C)
 │ Sisa <100°C
 └→ Bisa disuplai ke habitat

Turbin (40%) → listrik (robot, CNC, mesin las)
 └→ Panas buang turbin → ★ Radiator (227°C)
```

### Modul Habitat / Logistik — Konsumen Panas Buang di Bawah 100°C

Habitat adalah penyerap panas terakhir. Turbinnya sendiri menghasilkan listrik untuk penunjang hidup, pencahayaan, dan pertanian, sambil **menerima panas buang di bawah 100°C dari modul terdekat.**

```
☀️ Cermin khusus (30% → panas, 70% → turbin)
 │
 ├→ Turbin → listrik (penunjang hidup, pencahayaan, LED pertanian)
 │   Panas buang (~227°C) → ★ Radiator
 │
 └→ Panas → air panas, pemanasan bantu
     └→ Sisa → ★ Radiator

Panas buang <100°C dari modul terdekat (peleburan, struktural)
 │
 └→ Pemanasan habitat, air panas, pemanasan tanah pertanian
     └→ Sisa → diradiasikan dari lambung luar habitat (struktur itu sendiri berfungsi sebagai radiator)
```

Kebutuhan panas habitat (pemanasan, air panas) sederhana dibanding volume panas buang industri. Sisa di bawah 100°C dari modul terdekat sudah lebih dari cukup. **Habitat menerima pemanasan gratis — modul industri tidak memproduksi panas demi habitat.**

---

## Radiasi Terdistribusi: Gambaran Besar

Ringkasan aliran panas seluruh klaster:

```
☀️ Cahaya matahari → Cermin → Didistribusikan langsung ke setiap modul
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
[Peleburan]    [Struktural]    [Pusat data]
 Cermin→1.600°C Cermin→1.200°C  Cermin→Turbin→Listrik
    │               │               │
    ▼               ▼               ▼
 ★Rad.(800°C)   ★Rad.(400°C)   ★Rad.(227°C) ← buang turbin
 ★Rad.(400°C)   ★Rad.(200°C)   ★Rad.(200°C) ← setelah pompa panas
 ★Rad.(200°C)       │               │
    │               ▼               ▼
    └──── <100°C ──→ [Habitat] ←── <100°C
                      Pemanasan & air panas
                         │
                    ★Rad.(lambung, ~30°C)
```

**Bukan "lewat berurutan" melainkan "distribusi paralel + radiasi individual + hanya suhu rendah yang dibagi".** Setiap modul menerima panas dari cerminnya, membuangnya via radiatornya, dan hanya meneruskan ampas ke habitat.

### Mengapa Ini Lebih Baik

1. **Radiator suhu tinggi kecil** — 8 m² untuk membuang 1 MW pada 800°C. Cukup sirip kecil di sebelah proses
2. **Tanpa perpipaan antar modul** — menghindari mimpi buruk 50 km pipa suhu tinggi
3. **Setiap modul mandiri secara termal** — pemeliharaan satu modul tak memengaruhi yang lain
4. **Habitat aman** — tidak ada pipa 1.600°C melewati area hunian

---

## Koreksi Artikel Sebelumnya: Ke Mana 70% Itu Sebenarnya?

Artikel sebelumnya bilang "PV membuang 70%, turbin memakainya". Masih benar?

**Ya.** Tapi mekanismenya berbeda:

| | PV | Sistem turbin |
|---|---|---|
| 30% | Listrik | Listrik |
| 70% sisanya | Panas buang 60–80°C → **tak terpakai** | Didistribusikan sebagai pemanasan langsung cermin ke setiap proses → **dipakai untuk peleburan, pembentukan, perlakuan panas** |
| Beban radiasi | Seluruh 70% diradiasikan pada suhu rendah (radiator raksasa) | Radiasi bertahap pada suhu tinggi (radiator kecil terdistribusi) |

70% PV semuanya 60–80°C — suhu terburuk baik untuk industri maupun radiasi. Dalam sistem turbin, 70% itu dikirim lewat cermin ke setiap proses pada suhu yang tepat dibutuhkan, dan panas buang diradiasikan pada suhu setinggi mungkin.

**Arti sesungguhnya dari "memakai 70% sisanya": bukan panas buang turbin, melainkan energi panas cermin yang dikonsumsi langsung oleh setiap proses.**

---

## Rangkuman Satu Baris

Tidak ada media yang bisa membawa 1.600°C. Maka setiap fasilitas menerima cerminnya sendiri. Panas berkaskade di dalam setiap proses, dan surplus diradiasikan pada suhu tertinggi yang bisa dicapai. Hanya sisa di bawah 100°C yang sampai ke habitat. Panel radiator adalah lembaran Fe-Ni yang sama dengan bingkai cermin — lewatkan pelapis dan jadilah radiator.
