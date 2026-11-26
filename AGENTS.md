# Setup de Edição Faceless — Estilo Vox / Netflix *Explained*

Workspace configurado com **Whisper + FFmpeg + HyperFrames** e a skill `vox-true-crime` para produzir vídeos faceless de True Crime / Explicando com a paleta **Acid Lime (`#BBDF32`)**.

## Modo Automático (Novo Caso)

Quando o usuário colocar uma narração em `raw/` e informar o tema/caso (ex.: *"edita esse caso"*), **execute todo o fluxo automaticamente sem perguntar**:
1. Limpar e normalizar a narração de `raw/` para `-14 LUFS` (`scripts/roughcut.py clean-voice`).
2. Transcrever com Whisper palavra por palavra (`scripts/transcribe.py --language pt --model base`).
3. Buscar fotos históricas (Wikimedia Commons) e B-rolls mudos (Internet Archive), garantindo **rostos nunca cortados** (`object-fit: contain`) e **legenda PT-BR obrigatória** se houver vídeo complementar com fala em inglês.
4. Montar novo projeto `<caso>-vox/` seguindo `vox-true-crime` + [VOX_PLAYBOOK.md](VOX_PLAYBOOK.md), com paleta **Acid Lime (`#BBDF32`)** como destaque principal e legendas sincronizadas com nomes corrigidos.
5. Validar com `npm run check` (0 erros), capturar `snapshot` para conferir rostos e abrir `npx hyperframes preview --background`.

## Estrutura do Workspace

- `raw/` — áudios ou gravações brutas de entrada
- `audio/` — narração limpa e normalizada (`-14 LUFS`)
- `transcripts/` — saída do Whisper (`*.json` com timestamps por palavra, `*.srt`, `*.txt`)
- `assets/` — mídias prontas (`broll/`, `images/`, `sfx/`, `music/`)
- `scripts/` — automação em Python (`roughcut.py`, `transcribe.py`)
- `vox-explained-template/` — projeto HyperFrames base com 4 cenas modulares no estilo Vox / *Explained*
- `renders/` — MP4s finais exportados

## Fluxo de Produção (Passo a Passo)

1. **Limpar e normalizar a narração (FFmpeg):**
   ```powershell
   python scripts/roughcut.py clean-voice raw/narracao.mp3 -o audio/voiceover.wav
   ```
   *(Opcional para b-roll 1080p 30fps sem áudio:)*
   ```powershell
   python scripts/roughcut.py prep-broll raw/clipe.mp4 -o assets/broll/clipe-01.mp4
   ```

2. **Transcrever com timestamps por palavra (Whisper):**
   ```powershell
   python scripts/transcribe.py audio/voiceover.wav --language pt --model small
   ```
   Gera `transcripts/voiceover.json`, `.srt` e `.txt`.

3. **Editar / Criar cenas no HyperFrames:**
   Use `vox-explained-template/` (ou crie um novo projeto com `npx hyperframes init <nome>`).
   - **Paleta Vox / Explained:** Papel `#F4F4F9`, Tinta `#1d2a44`, Amarelo Vox `#BBDF32`, Coral `#FF6B00`.
   - **Tipografia:** `Archivo Black` (títulos), `Inter` (corpo/legendas), `Space Mono` (dados/rótulos), `Playfair Display` (citações).
   - **Regra editorial:** 1 ideia por cena (~15–20 palavras faladas), revelar cada dado/destaque no momento exato da narração.
   - **Playbook Completo (True Crime & Explicando):** Leia sempre [VOX_PLAYBOOK.md](VOX_PLAYBOOK.md) antes de criar ou editar cenas — inclui marca-texto em documentos, caixas pretas cinéticas, setas desenhadas à mão, mapas topográficos, grade codificada por cor, enquadramento seguro de rostos e design sonoro.

4. **Validar, visualizar e renderizar:**
   ```powershell
   cd vox-explained-template
   npm run check    # lint + runtime + layout + contraste
   npm run dev      # abre preview ao vivo (Studio)
   npm run render   # gera MP4 determinístico
   ```
