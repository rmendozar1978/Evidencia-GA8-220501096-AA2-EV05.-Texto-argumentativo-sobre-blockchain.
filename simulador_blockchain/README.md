# Simulador Educativo de Blockchain Criptográfico (SHA-256 & Proof-of-Work)
**Evidencia:** GA8-220501096-AA2-EV05 - Texto argumentativo sobre blockchain  
**Programa:** Tecnólogo en Análisis y Desarrollo de Software (ADSO) - Ficha 3235898  
**Aprendiz:** Ronald Fabian Mendoza Rodriguez (<rmendozar1978@gmail.com>)

---

## 📌 Descripción del Módulo
Este módulo de software implementa de forma nativa en Python los principios algorítmicos fundamentales que sustentan la tecnología **Blockchain**, dando soporte técnico y práctico al texto argumentativo y cumpliendo el Resultado de Aprendizaje **220501096-04: Codificar el software de acuerdo con el diseño establecido**.

### Componentes Clave:
1. **Hashing Criptográfico SHA-256 (`hashlib`)**: Generación determinista del identificador de cada bloque a partir de su contenido (`index`, `timestamp`, `transactions`, `previous_hash`, `nonce`).
2. **Encadenamiento Secuencial (`previous_hash`)**: Cada bloque almacena la huella digital criptográfica exacta del bloque predecesor.
3. **Consenso Proof-of-Work (PoW)**: Algoritmo de minería que exige encontrar un valor `nonce` que satisfaga una dificultad preestablecida (prefijo de ceros).
4. **Verificación de Inmutabilidad y Detección de Fraude (`is_chain_valid`)**: Algoritmo de auditoría que detecta inmediatamente alteraciones en transacciones o rupturas en los enlaces de la cadena.

---

## 🚀 Ejecución del Demostrador

Para ejecutar la demostración interactiva en consola:

```bash
python simulador_blockchain/blockchain.py
```

---

## 🧪 Ejecución de Pruebas Unitarias Automatizadas

El proyecto cuenta con un conjunto de 7 pruebas unitarias con cobertura total de los mecanismos de seguridad:

```bash
python -m unittest discover -s simulador_blockchain -v
```

### Resultados de las Pruebas:
- `test_genesis_block_creation`: Creación correcta del bloque de origen (Bloque Génesis).
- `test_add_transaction`: Inserción válida de transacciones al pool de memoria.
- `test_reject_invalid_transaction`: Rechazo de transacciones anómalas (montos negativos o cero).
- `test_mining_and_block_chaining`: Minado y enlace secuencial de bloques.
- `test_chain_integrity_valid`: Validación exitosa de una cadena no alterada.
- `test_tamper_detection_in_transaction_data`: Detección inmediata ante alteración de datos de transacciones.
- `test_tamper_detection_in_previous_hash_link`: Detección de ruptura forzada en el enlace hash.
