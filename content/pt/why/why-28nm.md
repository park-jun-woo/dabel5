---
title: "Por que 28nm"
date: 2026-02-25T12:00:03+09:00
lastmod: 2026-02-25T12:00:03+09:00
tags: ["28nm", "semicondutor", "TPU", "autorreplicacao", "litografia-ArF"]
image: "/images/why-28nm.webp"
summary: "O processo de ponta de 3nm nao pode ser fabricado sem o EUV monopolizado pela ASML — impossivel no espaco. 28nm e possivel apenas com ArF, e o Google TPU v1 provou com 92 TOPS medidos. O silicio sai da escoria de fundicao e o proprio espaco e uma sala limpa."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Foto do die de um chip NAND de 4 entradas TTL — 7 transistores, largura minima de linha 20μm (1968). Photo: Dgarte / Wikimedia Commons / CC BY-SA 3.0"
---

## "Se e autorreplicante, de onde vem os chips?"

Os artigos anteriores mostraram que espelhos, estruturas, [turbinas](/pt/why/why-turbines/), [baterias](/pt/why/why-iron-nickel-battery/) e [gestao termica](/pt/why/heat-flow/) — tudo pode ser fabricado com Fe-Ni de asteroides. O loop de autorreplicacao quase se fechou.

Quase.

**Os chips de IA ainda sao importados da Terra.** A operacao autonoma do modulo Dyson — controle de robos de mineracao, ajuste orbital, gestao de processos de fundicao, suporte vital do habitat — tudo e feito pela IA. Sem chips, o modulo esta cego.

"Nao ha litio nos asteroides" foi o fim para as baterias de litio-ion. Da mesma forma, **"nao se pode fabricar EUV no espaco" e o fim para o processo de ponta de 3nm.**

Entao com que processo se fabricam os chips?

---

## Por que nao o processo de ponta de 3nm

O nucleo do processo de semicondutores e a litografia — gravar padroes de circuitos em wafers com luz.

| Item | 28nm | 3~5nm (ponta) |
|------|------|--------------|
| Litografia | **ArF imersao** (Nikon, Canon, ASML) | **EUV** (monopolio ASML, bilhoes por unidade) |
| Disponibilidade de equipamentos | Mercado maduro, usado abundante | Extremamente limitado, sujeito a controle de exportacao |
| Complexidade de design | Padrao unico | Padrao multiplo (extremamente complexo) |
| Custo da fab | ~$3~5B | ~$20~30B |
| Rendimento | Alto (10+ anos de validacao) | Baixo inicialmente |

O scanner EUV (ultravioleta extremo) e fabricado por **uma unica empresa no planeta inteiro: ASML.** Uma unica fabrica em Eindhoven, Paises Baixos. Sujeito a controle de exportacao. O equipamento que a alianca EUA-Japao-Paises Baixos proibe a venda para a China. Reproduzi-lo no espaco? Impossivel.

O processo mais potente que nao requer EUV. Esse e o **28nm**.

"7nm nao e possivel com ArF?" — Sim. Usando uma tecnica chamada padrao multiplo, dispara-se a luz ArF varias vezes para criar padroes mais finos. Mas a complexidade de design explode e o rendimento despenca. Sem mao de obra e infraestrutura para gerenciar o rendimento no espaco, nao e realista.

"65nm nao seria mais facil de fabricar?" — Correto. Mas o desempenho por chip e muito baixo. Para a mesma tarefa sao necessarios muito mais chips, e mais chips significam fiacao, encapsulamento e refrigeracao proporcionalmente mais complexos. Fabricar mais facil, mas o sistema completo fica mais dificil.

**28nm = a integracao otima alcancavel sem EUV.**

---

## Isso nao e teoria — Google TPU v1

"E possivel rodar IA com 28nm?"

O Google deu a resposta em 2015. **[TPU v1](https://arxiv.org/abs/1704.04760).** Fabricado em processo de 28nm, mais de 100,000 unidades implantadas nos proprios data centers. Um acelerador de IA testado em combate.

| Item | Google TPU v1 (medido) |
|------|----------------------|
| Processo | 28nm |
| Arquitetura | Array sistolico 256 × 256 |
| Desempenho | 92 TOPS (INT8) ≈ 23 TFLOPS (FP16) |
| Consumo | ~75W em operacao real |
| Utilizacao do silicio | **90%+** |

A chave e a arquitetura de array sistolico (systolic array). Uma GPU e um chip de proposito geral — 70% do silicio e dedicado a logica de controle, cache e escalonador. Apenas 30% faz multiplicacao de matrizes de fato. O array sistolico e projetado exclusivamente para multiplicacao de matrizes, entao **mais de 90% do silicio e usado em computacao real.**

Se o objetivo e rodar apenas IA, toda a sobrecarga de proposito geral da GPU e desperdicio. O TPU e o chip que elimina esse desperdicio.

E isto nao e uma proposta teorica. **E o chip que rodou o AlphaGo.** Hardware em servico real durante anos nos data centers do Google.

---

## "4.6 vezes mais consumo de energia?"

O chip de IA de maior desempenho atual, NVIDIA H100. Processo de 4nm, 990 TFLOPS, consumo de 700W.

Um TPU v1 entrega 23 TFLOPS. Quantos sao necessarios para igualar um H100?

```
990 TFLOPS ÷ 23 TFLOPS = 43 unidades

43 unidades × 75W = 3,225W ≈ 3.2 kW
```

| | TPU v1 × 43 | H100 × 1 |
|---|---|---|
| FP16 total | ~990 TFLOPS | ~990 TFLOPS |
| Potencia total | **3.2 kW** | 700W |
| Proporcao de potencia | **4.6x** | Referencia |

4.6 vezes. Na Terra e uma diferenca fatal. Num mundo em que a eletricidade e 30~40% do custo operacional de um data center, 4.6 vezes mais consumo equivale a falencia.

**No espaco?**

Um modulo Dyson = 370 MW. 3.2 kW e **0.00086%** de 370 MW. Em area de espelho, 2.4 m² — um pixel do espelho Dyson de 1 km².

Na Terra, eletricidade e dinheiro. **No espaco, eletricidade e area de espelho.** Os espelhos sao feitos achatando Fe-Ni de asteroides.

A mesma estrutura logica de quando [a turbina superou o painel solar](/pt/why/why-turbines/) nos artigos anteriores. Uma escolha inferior pelos padroes terrestres se inverte como unica opcao pelos padroes espaciais. **Se os padroes mudam, as respostas mudam.**

---

## 1 modulo = data center de 30,000 H100

Alocando 30% dos 370 MW do modulo para computacao de IA:

```
111 MW ÷ 75W/chip = ~1,480,000 unidades (1.48 milhao de TPU v1)

1.48 milhao ÷ 43 unidades/H100 equivalente = ~34,000 H100

Sobrecarga de interconexao e refrigeracao 20~30% → conservadoramente H100 ~25,000~30,000 equivalentes
```

Equivalente ao maior cluster de IA do planeta em 2026. **Com um unico modulo.**

Quando os modulos se autorreplicarem para 270,000? Equivalente a bilhoes de H100. Uma escala que supera a capacidade computacional atual de toda a humanidade, surgida de um unico asteroide.

---

## Materia-prima: chips de IA a partir de escoria

Aqui esta a peca-chave deste design. Nao e necessaria uma mina de semicondutores dedicada.

Ao refinar o minerio do asteroide, o Fe-Ni (90%+) e o produto principal e **o restante e escoria (slag)**. O componente principal da escoria e SiO₂ — silicato. Nao se descarta.

```
Minerio do asteroide → Fundicao a vacuo
  +→ Fe-Ni (90%+) → Espelhos, estruturas, baterias, turbinas
  +→ Escoria (SiO₂ como componente principal)
       +→ A maior parte → Material de blindagem contra radiacao
       +→ Uma parte → Reducao com carbono (SiO₂ + 2C → Si + 2CO)
            → Silicio metalico
            → Refino zonal (calor solar + vacuo + microgravidade)
            → Lingote monocristalino de grau semicondutor (pureza 9N+)
            → Wafer de 300mm
            → TPU de 28nm
```

**Dos residuos de fundicao saem chips de IA.**

O [refino zonal (zone refining)](https://en.wikipedia.org/wiki/Zone_melting) e mais vantajoso no espaco. E um metodo de purificacao que faz passar uma zona fundida estreita ao longo do lingote de silicio para expulsar impurezas:

- **Energia:** Aquecimento direto com calor solar. Custo zero
- **Vacuo:** O espaco ja e vacuo. As impurezas evaporam automaticamente
- **Microgravidade:** A zona fundida nao desaba. O metodo FZ (Float Zone) terrestre tem limite de 200mm de diametro — acima disso, o silicio fundido colapsa pela gravidade. **Em gravidade zero, 300mm ou mais e possivel**
- **Repeticao:** Basta ajustar o angulo do espelho para repetir passes de refino infinitamente. Custo adicional zero

Na Terra, o refino zonal e um processo premium caro e de pequena escala. No espaco se torna o **processo padrao**.

---

## A fab: o espaco e a sala limpa

Um dos maiores custos de uma fab terrestre de 28nm: sala limpa Classe 1~10. Menos de 10 particulas de 0.5μm ou mais por pe cubico de ar. Manter isso requer enormes sistemas de filtros HEPA, unidades de tratamento de ar e gestao de pressao positiva. Uma parte consideravel do custo de construcao da fab vai para isso.

No espaco **nao ha ar.** A fonte de contaminacao por particulas simplesmente nao existe. O vacuo e a **sala limpa perfeita**.

Aptidao espacial das 7 etapas principais do processo:

| Processo | Aptidao espacial | Razao |
|----------|-----------------|-------|
| Crescimento do lingote | **Vantagem espacial** | Metodo FZ em microgravidade, lingotes de grande diametro |
| Corte de wafers | Possivel | Processo mecanico, independente do ambiente |
| Oxidacao/deposicao (CVD, PVD) | **Vantagem do vacuo** | Na Terra e preciso fazer vacuo na camara — o espaco ja e vacuo |
| Fotolitografia | Gargalo | Scanner ArF e fotorresiste dependem da Terra |
| Corrosao (etching) | **Vantagem do vacuo** | Simplificacao da camara de corrosao por plasma |
| Implantacao ionica | **Vantagem do vacuo** | Menor dispersao do feixe, sem necessidade de bombas de alto vacuo |
| Fiacao/encapsulamento | Possivel | Cu obtido de asteroides/Lua |

**6 de 7 etapas sao favoraveis ou equivalentes no espaco.** O unico gargalo e a fotolitografia — o scanner ArF em si nao pode ser fabricado no espaco. Mas uma vez levado, dura decadas.

---

## Gestao termica da fab: "Semicondutores no espaco?"

"O lado voltado para o Sol a centenas de graus, o lado oposto a -100°C, e e possivel controlar a ±0.01°C?"

Sim. E **e mais facil do que na Terra.**

### O nucleo do problema

O sistema de lentes de projecao do scanner de litografia ArF e extremamente sensivel a expansao termica. Uma flutuacao de 0.01°C altera a curvatura das lentes, gera erro de overlay e reduz o rendimento. A tolerancia de overlay para o processo de 28nm e de poucos nm.

Como se resolve nas fabs terrestres:
- Toda a sala limpa mantida a 23.00 ± 0.1°C
- Interior do scanner com circuito de refrigeracao independente a ±0.01°C
- **Problema:** As perturbacoes externas sao incessantes — variacoes de temperatura externa, estacoes, dia/noite, clima, terremotos, vibracoes do trafego, calor de equipamentos adjacentes

### Design termico da fab espacial

```
[Secao do modulo fab]

Exterior: Vacuo espacial (conducao zero, conveccao zero)
  |
  +- Parede refletora MLI (isolamento multicamada, dezenas de camadas)
  |    → Bloqueio de 99.5%+ da radiacao solar
  |    → Tambem bloqueia a perda por radiacao interior→exterior
  |
  +- Parede exterior estrutural (Fe-Ni)
  |
  +- Camada de circulacao ativa de liquido
  |    → Microcirculacao de agua ultrapura (UPW)
  |    → Bomba + aquecedor + valvula de dissipacao para controle ativo
  |    → Parede interior uniforme a 23.00 ± 0.05°C
  |
  +- Interior da fab (atmosfera de 1 atm N₂)
       → Calor dos equipamentos → absorvido por refrigerante em circulacao
       → Interior do scanner: loop de refrigeracao dedicado ±0.01°C
```

### Por que e mais facil do que na Terra

| Item | Fab terrestre | Modulo fab espacial |
|------|--------------|---------------------|
| Perturbacao termica externa | Incessante (clima, estacoes, dia/noite) | **Nenhuma** — isolamento por vacuo |
| Vibracao externa | Trafego, terremotos, fabricas adjacentes | **Nenhuma** — espaco sem vibracoes |
| Custo de isolamento | HVAC consome 30~40% da energia da fab | **O vacuo e isolante gratuito** |
| Previsibilidade de fontes de calor | Perturbacoes externas + equipamentos internos | **Apenas equipamentos internos** (completamente previsivel) |
| Dissipacao de calor | Torres de refrigeracao, chillers (alto consumo de agua e eletricidade) | **Paineis radiantes** (radiacao no vacuo) |

O paradoxo central: o ambiente termico extremo do espaco (centenas de graus vs -100°C) **nao chega ao interior da fab.** O vacuo e o melhor isolante, e uma vez que o MLI bloqueia a radiacao, o interior da fab fica completamente isolado termicamente do exterior. A partir dai so e preciso gerenciar o calor gerado pelos equipamentos internos, e isso e mais facil do que na Terra — porque as perturbacoes externas sao zero.

As fabs terrestres gastam 30~40% da energia total em HVAC porque **lutam constantemente contra o exterior**. A fab espacial nao tem essa batalha.

### UPW — vem do batolizador

A agua ultrapura (UPW) usada na circulacao de temperatura constante da fab vem do produto do batolizador, nao de uma planta de purificacao dedicada:

```
Batolizador: H₂O → H₂ + O₂ (eletrolise)
Reacao inversa: H₂ + O₂ → H₂O (celula de combustivel)

Subproduto H₂O → Purificacao → UPW
  +→ Refrigerante de circulacao de temperatura da fab
  +→ Limpeza de wafers
  +→ Liquido para litografia de imersao
```

### Secao de gravidade artificial

A litografia de imersao requer um filme de agua ultrapura sobre o wafer — precisa de gravidade. O modulo fab se divide em duas secoes:

```
Secao de vacuo (0G):
  +→ Deposicao CVD/PVD (requer vacuo)
  +→ Implantacao ionica (requer vacuo)
  +→ Corrosao por plasma (requer vacuo)

Secao de gravidade artificial (~1G por rotacao):
  +→ Litografia de imersao ArF (gestao de liquidos requer gravidade)
  +→ Limpeza umida (limpeza UPW requer gravidade)
  +→ Manuseio de wafers (transporte robotizado)
```

Os wafers se movem entre a secao de vacuo e a de gravidade artificial atraves de camaras de ar (airlocks). A secao rotativa nao tem fontes externas de vibracao, entao **so e preciso gerenciar a uniformidade da propria rotacao** — muito mais simples do que se defender contra terremotos e vibracoes do trafego na Terra.

---

## Dependencia externa: 5%

| Categoria | Fornecimento | Nota |
|-----------|-------------|------|
| Silicio | Local (escoria → Si) | |
| Energia | Local (calor solar) | |
| Sala limpa | Local (vacuo espacial) | |
| Agua ultrapura | Local (batolizador H₂O → purificacao) | |
| Fiacao de cobre | Local (asteroides/Lua) | |
| Scanner ArF | **Terra 1 vez** | Vida util de decadas |
| Fotorresiste | **Terra 1 vez/ano** | Centenas de kg/ano |
| Gas de corrosao | **Terra 1 vez/ano** | Reciclavel, pequenas quantidades |
| Elementos dopantes (B, As) | **Terra 1 vez/ano** | Dezenas de kg |

95% obtido no espaco. Os 5% restantes — scanner ArF (unica vez) + consumiveis (algumas toneladas/ano) — cabem em um lancamento de Starship para decadas.

"Fotorresiste nao e quimica organica de precisao?" — Correto. Isso e dificil de fabricar localmente. Mas o consumo anual e de algumas centenas de kg. Um lancamento de Starship pode levar suprimento para decadas. Nao e autossuficiencia total, mas sim **autossuficiencia de facto**.

---

## O loop de autorreplicacao se fecha

```
Antes:
  Minerio do asteroide → Fundicao → Fe-Ni → Espelhos · Estruturas · Baterias → Autorreplicacao
                                                                                ↑
                                                                    Chips de IA importados da Terra

Agora:
  Minerio do asteroide → Fundicao → Fe-Ni → Espelhos · Estruturas · Baterias · Turbinas
                                  → Escoria → Lingote Si → TPU 28nm → Controle autonomo por IA
                                                                                ↓
                                                                    Loop de autorreplicacao completamente fechado
```

Os espelhos fabricam espelhos. As baterias fabricam propelente. **A escoria fabrica chips de IA.** Nada e descartado.

---

## Resumo em uma linha

O processo de ponta de 3nm nao pode ser fabricado sem o EUV monopolizado pela ASML — impossivel no espaco. 28nm e possivel apenas com ArF, e o Google TPU v1 provou com 92 TOPS medidos. A desvantagem de 4.6x no consumo equivale a 2.4 m² de espelho num modulo de 370 MW. O silicio sai da escoria, o proprio espaco e a sala limpa e o isolamento a vacuo torna a gestao termica de ±0.01°C mais facil do que na Terra. O ultimo elo do loop de autorreplicacao.

![Foto do die de um chip NAND de 4 entradas TTL. Photo: Dgarte / Wikimedia Commons / CC BY-SA 3.0](/images/why-28nm.webp)
