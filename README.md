# Evidencia GA8-220501096-AA2-EV05: Texto Argumentativo sobre Blockchain
> **Programa:** Tecnólogo en Análisis y Desarrollo de Software (ADSO)  
> **Ficha:** 3235898 | **Centro:** Centro de Servicios de Salud - Regional Antioquia  
> **Aprendiz:** Ronald Fabian Mendoza Rodriguez ([rmendozar1978@gmail.com](mailto:rmendozar1978@gmail.com))  
> **Actividad:** GA8-220501096-AA2 - Incorporar tecnologías emergentes y disruptivas, de acuerdo con el diseño establecido.  
> **Resultado de Aprendizaje:** 220501096-04 - Codificar el software de acuerdo con el diseño establecido.

---

## 📋 Resumen de la Evidencia

Esta evidencia presenta un **texto argumentativo riguroso (de más de 3 páginas)** sobre la tecnología **Blockchain**, estructurado con base en premisas lógicas, argumentación técnica y conclusiones fundamentadas. Demuestra cómo la cadena de bloques representa un cambio paradigmático frente a los sistemas centralizados tradicionales mediante la descentralización, la inmutabilidad y la confianza algorítmica.

Adicionalmente, para dar cumplimiento integral al resultado de aprendizaje de codificación de software, el repositorio incorpora un **simulador algorítmico funcional en Python** con criptografía SHA-256, algoritmo Proof-of-Work y detección automatizada de intentos de alteración fraudulenta, respaldado por **pruebas unitarias automatizadas con 100% de aprobación**.

---

## 🗂️ Estructura del Repositorio

```text
texto_argumentativo_blockchain/
├── diagramas/
│   ├── red_blockchain_vs_centralizada.svg    # Diagrama vectorial: Sistema Centralizado vs Red P2P
│   └── anatomia_bloque_y_cadena.svg          # Diagrama vectorial: Estructura del Bloque y enlace SHA-256
├── docs/
│   ├── Texto_Argumentativo_Blockchain_GA8_220501096_AA2_EV05.md   # Ensayo formal completo (> 3 páginas)
│   ├── Texto_Argumentativo_Blockchain_GA8_220501096_AA2_EV05.html # Versión editorial imprimible (Ctrl+P -> PDF)
│   └── Prompt_Maestro_Ingenieria_EV05.md     # Prompt estructurado CO-STAR de ingeniería avanzada
├── simulador_blockchain/
│   ├── blockchain.py                         # Motor funcional en Python (SHA-256, PoW, Ledger)
│   ├── test_blockchain.py                    # Suite de 7 pruebas unitarias automatizadas
│   └── README.md                             # Documentación técnica del simulador
├── README.md                                 # Documentación general del proyecto
└── Repositorio_GitHub.txt                    # Ficha técnica institucional para entrega en plataforma SENA
```

---

## 📑 Contenido del Texto Argumentativo (13 Requerimientos SENA)

El texto argumentativo ubicado en [`docs/Texto_Argumentativo_Blockchain_GA8_220501096_AA2_EV05.md`](docs/Texto_Argumentativo_Blockchain_GA8_220501096_AA2_EV05.md) cubre con exhaustividad cada punto de la guía:

1. **Marco Conceptual:** Estudio de conceptos y características del componente formativo ("Tecnologías emergentes y disruptivas").
2. **Definición de Tecnología:** Concepto de tecnología y delimitación de la disrupción tecnológica.
3. **Objetivos de Blockchain:** Eliminación de intermediarios, descentralización, inmutabilidad y soberanía de datos.
4. **Antecedentes Históricos:** 1991 Haber & Stornetta, Merkle Trees, Cypherpunks, Whitepaper Bitcoin 2008 de Satoshi Nakamoto, Bloque Génesis 2009, Ethereum 2013-2015 con Vitalik Buterin y Smart Contracts, y redes 3.0 (IOTA, NEO).
5. **¿En qué consiste Blockchain?:** Arquitectura DLT (Distributed Ledger Technology), redes P2P y registro solo-anexar (`APPEND-ONLY`).
6. **Criptografía:** Claves asimétricas (Pública y Privada), firmas digitales ECDSA, autenticidad y no repudio.
7. **Función Hash:** Algoritmo SHA-256, determinismo, unidireccionalidad, efecto avalancha y resistencia a colisiones.
8. **Concepto de Bloque:** Header (versión, prev_hash, merkle_root, timestamp, bits, nonce) y cuerpo con 2.000 a 2.400 transacciones.
9. **Relación entre Bloques:** Enlace criptográfico mediante `previous_hash`, efecto dominó e inmutabilidad matemática.
10. **Gráfico de Red:** Representación visual comparativa entre arquitectura centralizada y red P2P distribuida.
11. **Productos y Desarrollos Reales:** IBM Food Trust, Pylon Network, Steemit, Koibanx, tokenización inmobiliaria y votación digital.
12. **Criptomonedas:** Activo digital nativo sin intermediación estatal, emisión matemática y escasez digital (21 millones BTC).
13. **Minería de Criptomonedas:** Consenso Proof-of-Work, cálculo del nonce, ajuste dinámico de dificultad, halving y recompensas.

---

## 💻 Ejecución del Simulador Funcional de Blockchain

El simulador implementa los principios matemáticos exactos explicados en el texto.

### 1. Ejecutar Demostración Interactiva
```bash
python simulador_blockchain/blockchain.py
```
*Muestra en consola la creación del Bloque Génesis, el minado de bloques con transacciones, la verificación de integridad y la detección inmediata de un intento de fraude al alterar montos.*

### 2. Ejecutar Pruebas Unitarias Automatizadas
```bash
python -m unittest discover -s simulador_blockchain -v
```
**Resultado:** 7 de 7 pruebas unitarias aprobadas (100% éxito, 0 errores).

---

## 🖨️ Generación de la Versión Impresa / PDF

Para generar el documento formal en PDF para entrega al instructor:
1. Abrir [`docs/Texto_Argumentativo_Blockchain_GA8_220501096_AA2_EV05.html`](docs/Texto_Argumentativo_Blockchain_GA8_220501096_AA2_EV05.html) en cualquier navegador (Google Chrome, Edge, Firefox).
2. Presionar `Ctrl + P` (Imprimir).
3. Seleccionar destino: **"Guardar como PDF"**.
4. Ajustar márgenes a "Predeterminado" y marcar "Gráficos de fondo".
5. Guardar como `Evidencia_GA8-220501096-AA2-EV05_Ronald_Mendoza.pdf`.

---

## 👤 Información del Aprendiz
- **Nombre:** Ronald Fabian Mendoza Rodriguez
- **Ficha:** 3235898 - ADSO
- **Correo:** rmendozar1978@gmail.com
- **Repositorio Oficial:** [https://github.com/rmendozar1978/Evidencia-GA8-220501096-AA2-EV05.-Texto-argumentativo-sobre-blockchain..git](https://github.com/rmendozar1978/Evidencia-GA8-220501096-AA2-EV05.-Texto-argumentativo-sobre-blockchain..git)
