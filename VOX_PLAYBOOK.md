# Playbook Visual & Sonoro — Estilo Vox / Netflix *Explained* (True Crime)

Base permanente para todas as edições faceless deste workspace, inspirada na linguagem documental da Vox (ref. `43BDpdMq_Ag`) e da série *Explicando* (*Explained*, Netflix).

## 1. Paleta Oficial — PANTONE 14-0340 TCX Acid Lime (`#BBDF32`)

- **Destaque principal (substitui o amarelo/verde da Vox):** **Acid Lime** `#BBDF32`
- **Escala Acid Limes:** `#566810`, `#7A9417`, `#9EC01E`, `#BBDF32`, `#CAE65E`, `#D8ED8A`, `#E7F4B6`
- **Base Editorial:** Midnight Blue `#1D2A44`, Charcoal `#2B2B2B`, Off-White `#F4F4F9`, Lavender Mist `#CFD5E6`, Dark Eggplant Purple `#330814`
- **Acentos Complementares:** Electric Orange `#FF6B00`, Electric Teal `#00F5D4`, Vivid Violet `#763F8C`, Indigo `#4B0082`, Terracotta `#DF5632`, Amber `#DFAD32`, Cyan `#32BBDF`, Magenta `#DF32BB`, Crimson `#DF3264`

## 2. Gráficos, Tipografia e Marcações

- **Efeito Marca-Texto & Recorte de Documentos (`Highlighter Effect`)**: exibir documentos, laudos ou manchetes com faixas amarelas (`#BBDF32`, `scaleX: 0 -> 1`) destacando frases-chave em sincronia com a fala.
- **Tipografia Cinética com Máscara (`Masked Text Reveal / Boxed Captions`)**: textos curtos em branco (`#F4F4F9`) sobre caixas pretas sólidas (`#1d2a44`) com sublinhado vermelho (`#FF6B00`) ou amarelo (`#BBDF32`), revelados por recorte/deslizamento.
- **Montagem Tipográfica Rápida (`Rapid-Fire Text Montage`)**: sequência veloz de palavras/teorias no centro da tela sobre fundo de mapa topográfico escuro.
- **Anotações e Setas Desenhadas à Mão (`Hand-Drawn Callouts`)**: setas e círculos finos em SVG (`stroke-dashoffset` animado) em vermelho, branco ou preto guiando o olhar sobre fotos antigas.
- **Terços Inferiores & Créditos de Fonte (`Lower Thirds & Source Tags`)**: tarjas retangulares pretas no canto inferior esquerdo para identificação e créditos fixos no canto superior esquerdo (ex.: `FONTE: WIKIMEDIA COMMONS`).

## 2. Mapas, Diagramas e Animações

- **Mapas Topográficos Vetoriais (`Topographic Infographics`)**: curvas de nível 2D minimalistas, réguas de distância, trajetos tracejados animados e marcadores "X" vermelhos.
- **Grade de Retratos Codificada por Cor (`Color-Coded Portrait Grid`)**: grade de retratos com bordas coloridas por categoria (ex.: azul/amarelo/vermelho) e **enquadramento seguro para rostos** (nunca cortar testa, olhos ou queixo — usar `object-fit: contain` ou `object-position: center 20%` com proporção compatível).
- **Diagramas em Corte / Fluxo (`Cross-Section & Connection Web`)**: ilustrações didáticas e teias de conexão reveladas passo a passo conforme a narração.
- **Mídia Mista / Colagem em Papel (`Paper Collage / Cutout`)**: recortes sobre fundo de papel (`#F4F4F9`) com sombras sólidas e movimento levemente "picotado" (`steps(12)` opcional para estética *Explained*).

## 3. Montagem, Câmera e Arquivo

- **Efeito Ken Burns**: push-in / pan contínuo e suave (`scale: 1 -> 1.07`) sobre fotos estáticas.
- **Tela Dividida (`Split Screen`)**: divisão em dois quadros para cruzar mapa + grade, teoria A vs. B ou paralelos históricos.
- **Imagens de Arquivo (`Archival Footage & B-Roll`)**: filmagens antigas sem áudio (`muted`) em baixa opacidade de fundo ou tela cheia com grão/vinheta, sem competir com a narração.
- **Entrevistas**: apenas gravações de arquivo históricas (quando aplicável), nunca webcam moderna.
- **Vídeos complementares em inglês**: sempre que houver trecho/áudio de arquivo com fala em inglês, **incluir legenda traduzida em PT-BR** na tela.

## 4. Áudio e Sound Design

- **Narração em Voice-Over (`-14 LUFS`)**: dita o ritmo exato da edição; cada elemento visual entra na palavra correspondente.
- **Trilha Sonora Modular (`Ambient Underscore`)**: base minimalista sob a voz (com ducking).
- **SFX e Foley**: cliques sutis, *whooshes* na entrada de setas/mapas/textos e ambiência discreta.
