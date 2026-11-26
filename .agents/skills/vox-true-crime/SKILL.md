---
name: vox-true-crime
description: Produz e edita vídeos faceless de True Crime e documentários no estilo Vox / Netflix Explicando (Explained) usando Whisper + FFmpeg + HyperFrames, com a paleta Acid Lime Combination (#BBDF32, #FF6B00, #00F5D4, #1D2A44, #2B2B2B, #F4F4F9), enquadramento seguro de rostos e recursos visuais/sonoros documentais. Use sempre que criar ou editar vídeos narrados de crimes reais, mistérios ou explicadores neste estilo.
---

# Vox True Crime — Skill de Edição Faceless

Skill oficial para transformar uma narração em `raw/` em vídeo documental estilo **Vox / Netflix *Explained*** usando **FFmpeg + Whisper + HyperFrames**.

> **Gatilho padrão:** quando o usuário colocar a narração em `raw/` e disser qual é o caso, execute todo o pipeline abaixo automaticamente (limpeza de áudio → transcrição → busca de fotos/B-roll → montagem das cenas + legendas → `npm run check` → `snapshot` visual dos rostos → `preview --background`).

## 1. Paleta Oficial — PANTONE 14-0340 TCX Acid Lime

- **Acid Lime (Destaque principal / Marca-texto — SEMPRE a cor de destaque):** `#BBDF32` (escala: `#566810`, `#7A9417`, `#9EC01E`, `#CAE65E`, `#D8ED8A`, `#E7F4B6`)
- **Bases Editoriais:** Midnight Blue `#1D2A44`, Charcoal `#2B2B2B`, Off-White `#F4F4F9`, Lavender Mist `#CFD5E6`, Dark Eggplant Purple `#330814`
- **Complementares:** Electric Orange `#FF6B00` *(use `#C24400` para texto pequeno sobre Off-White)*, Electric Teal `#00F5D4`, Vivid Violet `#763F8C`, Indigo `#4B0082`, Terracotta `#DF5632`, Amber `#DFAD32`, Cyan `#32BBDF`, Magenta `#DF32BB`, Crimson `#DF3264`

## 2. Tipografia Bundled (HyperFrames)

- **Display / Títulos:** `Archivo Black`
- **Corpo / Legendas:** `Inter` (mínimo `28px` para leitura confortável em celular)
- **Dados / Datas / Source Tags:** `Space Mono` (`tabular-nums`)
- **Citações:** `Playfair Display` (itálico)

## 3. Regras de Ouro de Enquadramento e Composição

1. **Rostos nunca cortados:** Todo retrato humano usa `object-fit: contain; object-position: center center;` dentro de passe-partout escuro (`#141518` ou `#2B2B2B`) — nunca cortar testa, olhos ou queixo.
2. **Zona segura para legendas:** Conteúdo principal respeita `bottom >= 190px` para nunca colidir com a faixa de legendas (`captions.html`).
3. **1 ideia por cena / troca visual frequente:** Sincronizar revelações com os timestamps do Whisper (`transcripts/*.json`) e alternar entre fotos históricas, mapas e gráficos.
4. **Entrevistas:** Apenas gravações de arquivo históricas (nunca webcam moderna).
5. **Vídeos complementares em inglês:** Se qualquer vídeo/áudio de arquivo tiver narração ou fala em inglês, **sempre adicionar legenda em PT-BR**.
6. **B-roll em vídeo:** Sempre `muted` (ou `-an` via `roughcut.py prep-broll`) em baixa opacidade ou tela cheia sem competir com a narração (`-14 LUFS`).

## 4. Recursos Visuais e Sonoros Obrigatórios

- **Efeito Marca-Texto (`Highlighter Effect`):** Faixa `#BBDF32` (`scaleX: 0 -> 1`) destacando frases-chave em documentos, manchetes e títulos.
- **Tipografia Cinética em Caixa (`Boxed Captions`):** Texto branco sobre caixa sólida escura com borda inferior `#FF6B00` ou `#BBDF32`.
- **Setas Desenhadas à Mão (`Hand-Drawn Callouts`):** SVG fino animado (`stroke-dashoffset`) apontando para detalhes em fotos e mapas.
- **Source Tags:** Tarja discreta no canto superior esquerdo (`FONTE: WIKIMEDIA COMMONS · ARQUIVO`).
- **Mapas Topográficos Vetoriais:** Curvas de nível 2D, trajetos tracejados e marcadores `"X"` em `#FF6B00`.
- **Grade de Retratos Codificada por Cor:** Bordas em `#FF6B00`, `#BBDF32` ou `#00F5D4` por categoria do caso.
- **Ken Burns & Tela Dividida:** Push-in suave (`scale: 1 -> 1.07`) em fotos estáticas e *split screen* para cruzar mapa + evidências.
- **Sound Design:** Narração limpa (`-14 LUFS`), trilha modular com ducking e SFX sutis (whoosh/clique) nas transições.

## 5. Pipeline de Execução

1. **Limpar e normalizar áudio:**
   `python scripts/roughcut.py clean-voice raw/<arquivo> -o audio/<nome>.wav`
2. **Transcrever com timestamps por palavra:**
   `python scripts/transcribe.py audio/<nome>.wav --language pt --model base`
3. **Montar projeto HyperFrames:**
   Copiar estrutura de `vox-explained-template/`, criar `compositions/*.html` e `captions.html`, e anexar `<audio class="clip" src="assets/audio/voiceover.wav" ...>`.
4. **Validar e inspecionar antes de renderizar:**
   - `npm run check` (obrigatório **0 erros** e **100% WCAG AA**)
   - `npx hyperframes snapshot --at <tempos>` + leitura visual do `contact-sheet.jpg` para confirmar rostos alinhados e zero sobreposição.
   - `npx hyperframes preview --background` para revisão no Studio.
