---
title: "Mengapa Cermin Dyson Mati di Orbit Merkurius"
date: 2026-02-24T12:00:02+09:00
lastmod: 2026-02-24T12:00:02+09:00
tags: ["swarm-dyson", "merkurius", "pelarian-termal", "cermin"]
image: "/images/post002.webp"
summary: "Di orbit Merkurius (0,39 AU), penurunan reflektivitas 5% bukan sekadar pengurangan output — melainkan memicu umpan balik positif thermal runaway yang membunuh cermin. Di L5 (1 AU), degradasi yang sama hanya kesalahan pembulatan."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Keuntungan 6,6x Tidak Gratis

Orbit Merkurius (0,39 AU) menerima fluks matahari 6,6 kali lebih kuat dibanding 1 AU. Efisiensi per satuan luas sangat dominan. Namun cermin tidak memiliki reflektivitas 100% — energi yang diserap itulah yang membunuhnya.

---

## Panas Terserap dan Suhu Kesetimbangan

Energi terserap dan suhu kesetimbangan untuk cermin dengan reflektivitas 90% (Stefan-Boltzmann, emisivitas sisi belakang ε=0,5 — untuk permukaan radiator tanpa lapisan, bukan sisi reflektif berlapis Al. Jika emisivitas radiator lebih rendah, suhunya bahkan lebih tinggi):

| | L5 (1 AU) | Orbit Merkurius (0,39 AU) |
|---|---|---|
| Fluks datang | 1.361 W/m² | 8.940 W/m² |
| Terserap (10%) | 136 W/m² | **894 W/m²** |
| Suhu kesetimbangan | ~−10°C | **~150°C** |

90–150°C sendiri merupakan suhu yang mampu ditahan oleh logam. **Tetapi masalahnya ada pada apa yang terjadi selanjutnya.**

---

## Umpan Balik Positif (Thermal Runaway)

Pada 150°C, degradasi lapisan pelindung mengalami percepatan. Interdifusi Al-substrat mengikuti hukum Arrhenius — meningkat secara eksponensial terhadap suhu.

```
Reflektivitas 90% → 894 W/m² terserap → 150°C
  ↓ Degradasi lapisan
Reflektivitas 85% → 1.341 W/m² terserap → ~190°C
  ↓ Degradasi makin cepat
Reflektivitas 80% → 1.788 W/m² terserap → ~230°C
  ↓ Ambang batas interdifusi Al-substrat terlampaui
Reflektivitas anjlok → Cermin mati
```

**Bagaimana jika penurunan 5% yang sama terjadi di L5?** Penyerapan tambahan: 68 W/m². Perubahan suhu dapat diabaikan. Umpan balik tidak pernah aktif.

---

## CME Menarik Pelatuk

Kepadatan angin matahari berbanding terbalik dengan kuadrat jarak. Pada 0,39 AU, kepadatannya ~6,6 kali lipat dibanding 1 AU.

Ancaman yang lebih besar adalah CME (coronal mass ejection). Pada 0,39 AU, CME belum sempat menyebar — menghantam cermin dengan kepadatan energi terkonsentrasi. Satu CME kuat saja dapat melontarkan permukaan pelapis → reflektivitas menurun → thermal runaway dimulai.

Sebagai acuan: wahana MESSENGER tidak akan bertahan di orbit Merkurius tanpa pelindung matahari keramik.

---

## Perbandingan Realitas Operasional

| | L5 (1 AU) | Orbit Merkurius (0,39 AU) |
|---|---|---|
| Suhu kesetimbangan | −10°C (aman) | 150°C (zona degradasi) |
| Dampak kehilangan 5% reflektivitas | +68 W/m² (dapat diabaikan) | **+447 W/m² (awal thermal runaway)** |
| Toleransi CME | Tinggi | Rendah (kepadatan 6,6x) |
| Siklus penggantian perkiraan | Puluhan tahun+ | Tahun hingga ~satu dekade |
| Logistik pemeliharaan | Tepat di sebelah klaster industri L5 | Membutuhkan infrastruktur layanan terpisah |

---

## Ringkasan Satu Baris

Di orbit Merkurius, kehilangan reflektivitas 5% bukan pengurangan output 5% — melainkan sinyal bahwa cermin mulai sekarat. Di L5, itu hanya kesalahan pembulatan.
