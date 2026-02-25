---
title: "Mengapa Transmisi Daya Nirkabel Tidak Praktis"
date: 2026-02-24T12:00:06+09:00
lastmod: 2026-02-24T12:00:06+09:00
tags: ["transmisi-daya", "daya-nirkabel", "konsumsi-lokal"]
summary: "Dyson swarm standar mengumpulkan energi di tempat tak berpenghuni dan harus mengirimkannya ke tempat manusia berada — kehilangan 75-90% dalam transmisi. Di L5, pabrik ditempatkan di sebelah cermin dan langsung disambungkan."
image: "/images/power-transmission-local.webp"
author: "PARK JUN WOO"
imageCaption: "Teleskop radio Arecibo (diameter 305 m). Menerima transmisi daya laser nirkabel memerlukan penerima berskala seperti ini. Foto: Mariordo / Wikimedia Commons / CC BY-SA 4.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## Mengumpulkan Itu Mudah — Tapi Digunakan di Mana?

Skenario Dyson swarm standar: bongkar Merkurius, tempatkan cermin/panel di dekat Matahari. Pengumpulan energi — selesai. Tapi **di mana energi itu dikonsumsi?** Tidak ada apa-apa di dekat Matahari.

Jika harus dikirim ke Bumi — mari periksa fisika transmisi daya nirkabel (WPT).

---

## Berkas Gelombang Mikro: Batas Difraksi

Frekuensi 2,45 GHz (λ = 0,122 m), orbit Merkurius → Bumi (rata-rata ~1 AU = 1,5×10¹¹ m):

**Diameter spot ≈ 2,44 × λ × jarak / diameter antena pemancar**

| Diameter antena pemancar | Diameter spot di Bumi | Kelayakan |
|---|---|---|
| 1 km | 44.600 km | 3,5× diameter Bumi |
| 10 km | 4.460 km | Skala radius Bumi |
| 100 km | 446 km | Rectenna seukuran Semenanjung Korea |

Sebaliknya — untuk menerima dengan rectenna 10 km di Bumi:

```
Antena pemancar yang dibutuhkan = 2,44 × 0,122 × 1,5×10¹¹ / 10.000
                                = 4.460 km diameter
```

**Diameter Merkurius adalah 4.880 km. Anda membutuhkan antena seukuran Merkurius.**

---

## Bagaimana dengan Laser?

Dengan λ = 1 μm, masalah difraksi sangat berkurang:

| Diameter cermin pemancar | Diameter spot di Bumi |
|---|---|
| 10 m | 36,6 km |
| 100 m | 3,7 km |

Ukuran spot cukup realistis. **Tapi rantai efisiensi konversi sangat fatal:**

| Tahap | Efisiensi |
|---|---|
| Listrik → Laser | ~40–50% |
| Transmisi atmosfer (tergantung cuaca) | ~50–80% |
| Penerima PV → Listrik | ~50–60% |
| **Total** | **~10–24%** |

75–90% listrik yang dihasilkan hilang selama transmisi. Keunggulan fluks 6,6× sepenuhnya terhapus di sini.

---

## Masalah Tambahan di Orbit Merkurius: Okultasi Matahari

Periode orbit Merkurius adalah 88 hari. Selama bagian signifikan dari orbit, **Matahari berada di antara Merkurius dan Bumi** — membuat transmisi berkas secara fisik tidak mungkin selama interval tersebut. Tanpa satelit relay, transmisi berkelanjutan tidak dapat dicapai.

---

## L5: Produksi Lokal, Konsumsi Lokal

Di L5, masalah transmisi sama sekali tidak ada.

| | Transmisi Merkurius → Bumi | Konsumsi lokal L5 |
|---|---|---|
| Jarak transmisi | 0,5–1,5 AU | **Beberapa km hingga puluhan km** |
| Metode transmisi | Gelombang mikro/Laser (nirkabel) | **Kabel berkawat** |
| Efisiensi total | 10–24% (laser) | **~95%+** |
| Okultasi Matahari | Ya (siklus 88 hari) | **Tidak** |
| Infrastruktur penerima | Rectenna ribuan km atau antena seukuran Merkurius | **Tidak diperlukan** |
| Konsumen | Bumi (150 juta km jauhnya) | **Silinder O'Neill berdekatan + pusat data** |

Catatan: Di ruang hampa, pendinginan kabel superkonduktor hampir gratis. Radiasi latar belakang kosmik pada 2,7 K berfungsi sebagai pendingin.

---

## Pertanyaan Sebenarnya: Adakah Alasan Mengirim Listrik ke Bumi?

Jika L5 memiliki fasilitas industri, habitat, dan pusat data:

- **Hasil komputasi** (inferensi AI, simulasi) ditransmisikan via komunikasi optik — bit itu ringan
- **Barang manufaktur** dikirim secara fisik
- **Tidak perlu mengirim listrik itu sendiri ke Bumi**

Yang ditransmisikan bukan energi — **melainkan produk dari energi.** Inilah inti model konsumsi lokal L5.

---

## Ringkasan Satu Baris

Konsep Dyson swarm standar memiliki kontradiksi mendasar: "mengumpulkan energi di tempat tak berpenghuni, lalu mengirimkannya ke tempat manusia berada." Di L5, pabrik dan habitat ditempatkan di sebelah cermin dan langsung disambungkan.
