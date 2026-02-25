---
title: "Por que metal fundido, nao baterias"
date: 2026-02-25T12:00:02+09:00
lastmod: 2026-02-25T12:00:02+09:00
tags: ["metal-fundido-termico", "ESS", "levitacao-eletromagnetica", "armazenamento-termico", "autorreplicacao"]
image: "/images/molten-metal-thermal-ess.webp"
summary: "Um modulo Dyson e uma usina solar termica — armazenar calor diretamente como Fe-Ni fundido em gravidade zero. ~145 Wh/kg com calor latente, ciclos infinitos, tudo de minerio de asteroide."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Massa de Fe-Ni fundido em levitacao eletromagnetica no vacuo de gravidade zero — mantém forma esferica pela tensao superficial. Image: Gemini"
---

## O que faltou no artigo anterior

No [artigo anterior](/pt/why/why-iron-nickel-battery/) mostramos por que as baterias de ferro-niquel superam as de litio-ion. Nao ha litio nos asteroides, nao se pode apagar incendio no vacuo, ferro-niquel dura 30~50 anos e a sobrecarga produz hidrogenio.

Tudo correto. **Mas faltava algo.**

Um modulo Dyson e uma usina solar termica. Espelhos concentram a luz e o calor move as turbinas. Quando e preciso armazenar energia para o eclipse, o design atual funciona assim:

```
Calor solar (1,600°C) → Turbina → Eletricidade (370 MW)
                              → Excedente (~50 MW)
                                   → Bateria (energia quimica)      ← 2 conversoes
                                   → Durante eclipse → Eletricidade  ← 3 conversoes
```

Calor → eletricidade → quimica → eletricidade. **3 conversoes.** Perda de 20~30% em cada etapa.

E se armazenarmos o calor diretamente?

```
Calor solar (1,600°C) → Parte armazenada diretamente no deposito termico  ← 0 conversoes
                     → Durante eclipse → Deposito → Turbina → Eletricidade ← 1 conversao
```

**1 conversao.** A diferenca de eficiencia e esmagadora.

Converter o excedente de uma usina solar termica em eletricidade, depois em quimica e de volta em eletricidade e como converter agua em vapor, decompô-la em hidrogenio e oxigenio, e depois sintetiza-la de volta em agua. **Pode ser feito, mas por que?**

O armazenamento termico e a resposta. Entao por que nao se faz isso na Terra?

---

## Por que nao funciona na Terra, por que funciona no espaco

Armazenar calor em metal fundido na Terra e um tema de pesquisa academica, nao uma realidade industrial. Ha razoes:

| Problema | Terra | Espaco (gravidade zero, vacuo) |
|----------|-------|-------------------------------|
| Recipiente | Deve suportar milhares de toneladas de material fundido → enorme e caro | **Sem peso proprio** — paredes finas ou totalmente sem contato |
| Isolamento | Precisa bloquear conveccao + conducao + radiacao | **So bloquear radiacao** — dezenas de camadas de MLI bastam |
| Perda termica | Alta — conveccao do ar e a causa principal | **Extremamente baixa** — conveccao zero no vacuo |
| Corrosao | Material fundido a 1,500°C ataca as paredes | **Levitacao eletromagnetica sem contato** → corrosao zero |
| Seguranca | Vazamento = acidente grave | Sem fogo no vacuo, sem meio de propagacao |

**As fraquezas terrestres desaparecem ou se invertem no espaco.** Exatamente o mesmo padrao repetido nos artigos anteriores — [turbinas vs PV](/pt/why/why-turbines/), ferro-niquel vs litio-ion.

---

## Armazenamento termico por levitacao eletromagnetica

O Fe-Ni fundido e condutor eletrico mesmo a 1,500°C (perde o magnetismo acima do ponto de Curie do niquel, mas mantem a condutividade). Ao aplicar um campo eletromagnetico alternado, correntes parasitas (eddy currents) sao induzidas, e a forca de repulsao entre essas correntes e o campo permite a **levitacao sem contato**.

E uma tecnica ja usada em laboratorios terrestres. Chama-se fusao por [EML (Electromagnetic Levitation)](https://en.wikipedia.org/wiki/Electromagnetic_levitation). Amostras de metal de alguns gramas a alguns quilogramas sao suspensas no ar e fundidas. A unica razao pela qual nao se pode escalar mais na Terra e a **gravidade**. Vencer a gravidade exige campos magneticos fortes, e campos fortes consomem energia. Alguns quilogramas e o limite.

Em gravidade zero? **Nao ha gravidade para vencer.** So e necessario o campo magnetico minimo para estabilizar a posicao. Toneladas, centenas de toneladas, dezenas de milhares de toneladas.

```
[Secao do deposito termico]

        +--- Parede refletora MLI (isolamento multicamada) ---+
        |                                                      |
        |    +-- Bobina eletromagnetica (refrigerada) --+      |
        |    |                                          |      |
        |    |   @@@@@@@@@@@@@@@@                       |      |
        |    |   @ Massa de Fe-Ni fundido @             |      |
        |    |   @ (1,200~1,500°C)        @             |      |
        |    |   @@@@@@@@@@@@@@@@                       |      |
        |    |                                          |      |
        |    +------------------------------------------+      |
        |                                                      |
        +------------------------------------------------------+
```

Em gravidade zero, o metal fundido assume **naturalmente uma forma esferica** pela tensao superficial. A esfera tem a menor relacao superficie/volume — perda termica por radiacao minima. A parede refletora MLI aprisiona o calor radiante, o campo eletromagnetico mantem a posicao e nao ha contato com as paredes, entao a corrosao e zero.

**Fundir o Fe-Ni extraido do asteroide e deixa-lo flutuando: isso e um deposito termico.**

---

## Carga e descarga

```
[Carga — operacao normal]
Concentracao solar → Abertura do obturador radiante → Aquecimento da massa metalica → 1,200°C → 1,500°C

[Descarga — durante eclipse]
Abertura do obturador radiante → Calor radiante da massa metalica aquece o trocador → Fluido de trabalho → Turbina
1,500°C → 1,200°C (aproveitando ΔT=300°C)
```

Carga: basta direcionar parte do calor solar coletado pelos espelhos para o deposito termico. Abre-se o obturador e a luz aquece a massa metalica.

Descarga: quando chega o eclipse, abre-se o obturador e o trocador de calor recebe a radiacao da massa metalica. O trocador aquece o fluido de trabalho e move a turbina. Usa-se a mesma turbina — em operacao normal os espelhos sao a fonte de calor, durante o eclipse e o deposito termico. **Para a turbina, so muda a fonte de calor; o resto e identico.**

O meio de troca termica e a radiacao. Nao se pode inserir tubulacao numa massa fundida sem contato, entao a transferencia de calor por obturador radiante e o mecanismo basico. A energia radiante do metal fundido a 1,500°C e proporcional a T⁴ pela lei de Stefan-Boltzmann — suficientemente potente.

---

## Densidade energetica: calor especifico + calor latente

Calor especifico da liga Fe-Ni: ~0.5 kJ/(kg·K) = ~0.14 Wh/(kg·K). Calculando apenas o **calor sensivel (sensible heat)** proporcional a variacao de temperatura (ΔT):

| Faixa de temperatura (ΔT) | Calor sensivel | Nota |
|----------------------------|----------------|------|
| 300°C (1,200→1,500°C) | ~42 Wh/kg | Conservador |
| 500°C (1,000→1,500°C) | ~70 Wh/kg | Intermediario |
| 1,000°C (500→1,500°C) | ~140 Wh/kg | Agressivo |

Mas nao termina aqui.

### Bonus do calor latente

O ponto de fusao da liga Fe-Ni e ~1,430~1,450°C. A faixa operacional 1,000~1,500°C **atravessa esse ponto de fusao.** Na carga, o metal funde; na descarga, solidifica — mudanca de fase (phase change).

Quando um material funde, sua temperatura nao sobe mas absorve uma enorme quantidade de calor. Esse e o **calor latente de fusao (latent heat of fusion).**

```
Calor latente de fusao do ferro (Fe): ~270 kJ/kg ≈ 75 Wh/kg
Liga Fe-Ni: faixa similar
```

Somando calor sensivel e calor latente:

| Faixa de temperatura | Sensivel | Latente | **Total** |
|----------------------|----------|---------|-----------|
| 300°C (1,200→1,500°C) | ~42 | ~75 | **~117 Wh/kg** |
| 500°C (1,000→1,500°C) | ~70 | ~75 | **~145 Wh/kg** |
| 1,000°C (500→1,500°C) | ~140 | ~75 | **~215 Wh/kg** |

**So o calor latente duplica a densidade energetica.** Um pedaco de ferro fundindo e solidificando ja se sobrepoe ao extremo inferior das baterias de litio-ion (150~270 Wh/kg).

### Comparacao de ESS (incluindo calor latente)

| Metodo | Densidade energetica | Vida ciclica | Fornecimento de materiais |
|--------|---------------------|--------------|---------------------------|
| Litio-ion | 150~270 Wh/kg | 3,000~10,000 ciclos | Impossivel (sem Li nos asteroides) |
| Bateria ferro-niquel | 30~50 Wh/kg | Praticamente infinita | Asteroide Fe-Ni |
| **Armazenamento termico Fe-Ni fundido** | **117~215 Wh/kg** | **Praticamente infinita** | **Asteroide Fe-Ni** |

Densidade energetica equivalente ao litio-ion, vida ciclica infinita e os materiais estao por toda parte nos asteroides. Alem disso, a conversao calor → eletricidade e de apenas 1 passo, tornando a eficiencia do sistema esmagadora.

Por que a vida ciclica e infinita: esquenta-se e esfria-se um pedaco de metal. Sem reacao quimica. Sem eletrodos. Sem eletrolito. Nao ha nada que se degrade.

---

## Escala: por que nao uma esfera gigante, mas sim 60 unidades pequenas

Eclipse maximo de 12 horas, potencia da turbina 370 MW. Nao e preciso cobrir tudo com armazenamento termico — celulas de combustivel H₂ e baterias dividem a carga.

### Calculo hibrido

```
Das 12 horas de eclipse:
  Deposito termico: 6 horas
  Celula de combustivel H₂: 4 horas (acumulo anual do batolizador)
  Bateria ferro-niquel: 2 horas (acompanhamento de carga instantanea + backup)
```

Deposito termico para 6 horas (incluindo calor latente):

```
370 MW ÷ 0.30 (eficiencia da turbina) = ~1,233 MW(th) × 6h = ~7,400 MWh(th)

Base ΔT=500°C + calor latente (145 Wh/kg):
  Massa necessaria = 7,400,000 kWh ÷ 0.145 kWh/kg = ~51,000 toneladas

(Sem calor latente: 105,000 toneladas → o bonus do calor latente reduz a massa pela metade)
```

Colocar 51,000 toneladas numa unica esfera da um raio de ~12 m. Intuitivamente simples. **Mas nao funciona.** Ha tres razoes de engenharia.

### Razao 1: superficie insuficiente para a descarga

Durante o eclipse, o deposito termico transfere calor ao trocador **apenas por radiacao**. A potencia radiante e proporcional a superficie (P = ε σ A T⁴).

A esfera e a forma com menor relacao superficie/volume. Otima para **conservar** calor, mas um gargalo para **libera-lo** rapidamente.

```
Potencia termica necessaria: ~1,233 MW(th)

Radiacao a 1,500°C (1,773K) (ε=0.5):
  P/A = ε × σ × T⁴ = 0.5 × 5.67e-8 × 1,773⁴ ≈ 280 kW/m²

Superficie necessaria: 1,233,000 kW ÷ 280 kW/m² ≈ 4,400 m²

Superficie de uma esfera de raio 12 m: 4π(12)² ≈ 1,810 m² → Insuficiente (41% do necessario)
```

**Uma unica esfera nao consegue fisicamente liberar o calor necessario.** A superficie nao chega a metade.

Dividindo em ~58 unidades de raio 3 m:

```
Superficie por unidade: 4π(3)² ≈ 113 m²
Superficie total de 58 unidades: 113 × 58 ≈ 6,560 m² → 149% do necessario (com margem)
Massa por unidade: (4/3)π(3)³ × 7,800 ≈ 880 toneladas
```

**Ao armazenar, cada unidade mantem sua forma esferica para minimizar perdas; ao descarregar, a superficie total de multiplas unidades fornece potencia termica suficiente.** O defeito da esfera e resolvido pelo numero de unidades.

### Razao 2: sloshing — uma bola de demolicao de 100,000 toneladas de lava

Quando 51,000 toneladas de metal liquido flutuam como uma unica esfera, se o modulo rotacionar ou vibrar minimamente para controle de atitude, ondas enormes **(sloshing)** surgem no interior. Somada a instabilidade magnetohidrodinamica (MHD), ha risco de que essa massa de lava oscile ate romper o confinamento eletromagnetico.

Com unidades de raio 3 m e 880 toneladas? A energia de fluxo e proporcional ao cubo do tamanho da unidade, entao **a energia de sloshing de cada unidade e menos de 1/10,000 em relacao a esfera unica**. O risco de escape do confinamento e virtualmente eliminado.

### Razao 3: expansao volumetrica durante a mudanca de fase

Ao alternar entre 1,200°C (solido) e 1,500°C (liquido), o Fe-Ni se expande e contrai repetidamente. Se uma esfera de raio 12 m esfriar a partir da superficie, forma-se uma crosta solida, e ao contrair o liquido interior ha risco de que **a crosta se frature e fragmentos sejam lancados ao vacuo**. Unidades pequenas permitem gerenciar uniformemente o gradiente de temperatura interior-exterior, eliminando esse problema.

### Conclusao do design

```
Especificacoes da unidade termica:
  Forma: esferica (formacao natural por tensao superficial)
  Raio: ~3 m
  Massa: ~880 toneladas/unidade
  Numero de unidades: ~58 (por modulo)
  Massa total: ~51,000 toneladas
  Disposicao: distribuida na estrutura atras dos espelhos (tambem como contrapeso)

Desempenho de descarga:
  Superficie total: ~6,560 m² (149% dos 4,400 m² necessarios)
  Margem de 1,233 MW(th) de potencia assegurada
```

As 51,000 toneladas nao sao obtidas separadamente. O Fe-Ni refinado do asteroide e **mantido fundido sem deixar solidificar** e ja e uma unidade termica. Distribuido na estrutura do modulo, **tambem serve como contrapeso**.

---

## ESS de 3 niveis: separacao de papeis

As baterias nao precisam mais assumir o ESS massivo. A tecnologia otima e atribuida a cada nivel:

```
Nivel 1 — Massivo (escala de horas)
  └→ Deposito termico de metal fundido
       Carga: calor solar direto
       Descarga: deposito termico → turbina → eletricidade
       Papel: resposta ao eclipse, perda de conversao minima

Nivel 2 — Buffer (escala de segundos~minutos)
  └→ Bateria ferro-niquel
       Carga: excedente eletrico
       Descarga: eletroquimica (resposta em ms)
       Papel: acompanhamento de carga instantanea, energia de arranque

Nivel 3 — Emergencia + producao quimica
  └→ H₂/O₂ (produto do batolizador)
       Celula de combustivel para geracao de emergencia
       Propelente · agente redutor · oxigenio respiravel
       Backup secundario em caso de eclipse prolongado
```

### O que essa estrutura proporciona

**O banco de baterias e drasticamente reduzido.** No design anterior, cobrir 12 horas de eclipse so com baterias exigia 111,000 m³. Com o deposito termico assumindo a carga massiva, as baterias cobrem apenas 2 horas — reduzidas a poucos milhares de m³.

**O papel do batolizador fica claro.** O artigo anterior descrevia o batolizador (eletrolise da agua por sobrecarga) como uma funcao que combina ESS e producao quimica. Com o deposito termico assumindo o ESS massivo, o batolizador se posiciona como **planta quimica** — a producao de propelente de hidrogenio, oxigenio e agentes redutores e sua funcao principal; a geracao de emergencia e secundaria.

**Os materiais sao os mesmos.** Deposito termico = Fe-Ni fundido. Bateria = eletrodos de Fe-Ni. Batolizador = a mesma bateria com sobrecarga. Os 3 niveis vem do Fe-Ni de asteroides. Nenhuma materia-prima nova e adicionada ao loop de autorreplicacao.

---

## Relacao com o artigo anterior (bateria ferro-niquel)

Os argumentos centrais do artigo anterior **continuam todos validos:**

- Nao ha litio nos asteroides → sem mudanca
- Vida util de 30~50 anos da bateria ferro-niquel → sem mudanca
- Risco de incendio no vacuo → sem mudanca
- Producao de H₂/O₂ do batolizador → sem mudanca
- Fabricacao local possivel → sem mudanca

**O que e complementado:** o artigo anterior poderia ser lido como se a bateria ferro-niquel assumisse sozinha todo o ESS massivo (12 horas de eclipse). Na realidade, para armazenamento massivo de energia, o armazenamento termico e esmagadoramente superior, e a bateria brilha no seu proprio dominio: a resposta instantanea.

**Cada um faz o que faz melhor.** O deposito termico para armazenamento de horas. A bateria para resposta eletrica em milissegundos. A celula de combustivel para emergencias e producao quimica. Nao e necessario que um so faca tudo.

---

## Resumo em uma linha

Um modulo Dyson e uma usina solar termica, mas converter calor em eletricidade, depois em quimica e de volta e uma tripla perda de conversao. Fundir Fe-Ni de asteroides e deixa-lo flutuando em gravidade zero da um deposito termico com 0 conversoes para carregar e 1 para descarregar. Somando o calor latente da mudanca de fase, a densidade energetica e ~145 Wh/kg — equivalente ao litio-ion. 58 unidades de raio 3 m em configuracao distribuida resolvem o gargalo de superficie na descarga, sloshing e expansao por mudanca de fase. Tudo com o mesmo Fe-Ni de asteroides.

![Massa de Fe-Ni fundido em levitacao eletromagnetica no vacuo de gravidade zero. Image: Gemini](/images/molten-metal-thermal-ess.webp)
