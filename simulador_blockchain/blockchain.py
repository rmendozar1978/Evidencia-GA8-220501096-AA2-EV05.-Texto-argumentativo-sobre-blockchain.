"""
================================================================================
SERVICIO NACIONAL DE APRENDIZAJE - SENA
TECNÓLOGO EN ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO) - FICHA: 3235898
EVIDENCIA: GA8-220501096-AA2-EV05 - TEXTO ARGUMENTATIVO SOBRE BLOCKCHAIN
APRENDIZ: RONALD FABIAN MENDOZA RODRIGUEZ (rmendozar1978@gmail.com)
COMPONENTE PRÁCTICO: SIMULADOR DE BLOCKCHAIN CON HASH CRIPTOGRÁFICO SHA-256
================================================================================
"""

import hashlib
import json
import time
from typing import List, Dict, Any, Optional


class Transaction:
    """
    Representa una transacción individual dentro de la red descentralizada.
    """
    def __init__(self, sender: str, recipient: str, amount: float, timestamp: Optional[float] = None):
        self.sender = sender
        self.recipient = recipient
        self.amount = float(amount)
        self.timestamp = timestamp or time.time()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp
        }

    def __repr__(self) -> str:
        return f"Tx({self.sender} -> {self.recipient}: {self.amount} BTC)"


class Block:
    """
    Representa un bloque dentro de la cadena (Blockchain).
    Contiene un encabezado (Header) y el cuerpo con las transacciones validadas.
    """
    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str, nonce: int = 0, timestamp: Optional[float] = None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Calcula el Hash criptográfico SHA-256 del bloque combinando:
        - Índice
        - Timestamp
        - Transacciones serializadas
        - Previous Hash (Enlace a la cadena anterior)
        - Nonce (Prueba de trabajo)
        """
        block_content = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }
        # JSON ordenado estrictamente para determinismo en el hash
        block_string = json.dumps(block_content, sort_keys=True)
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

    def mine_block(self, difficulty: int) -> str:
        """
        Algoritmo Proof-of-Work (PoW):
        Incrementa el 'nonce' hasta que el hash resultante inicie con 'difficulty' ceros.
        """
        target = "0" * difficulty
        start_time = time.time()
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()
        elapsed = time.time() - start_time
        return f"Bloque #{self.index} minado en {elapsed:.4f}s con Nonce {self.nonce} -> Hash: {self.hash}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash,
            "transactions": [tx.to_dict() for tx in self.transactions]
        }


class Blockchain:
    """
    Administra la estructura completa del Libro Mayor Distribuido (Ledger),
    la piscina de transacciones pendientes y la verificación de inmutabilidad.
    """
    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = []
        self.unconfirmed_transactions: List[Transaction] = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Crea el primer bloque de la cadena (Bloque Génesis),
        cuyo previous_hash es una secuencia inicial de ceros.
        """
        genesis_tx = [Transaction(sender="NETWORK_GENESIS", recipient="Satoshi_Nakamoto", amount=50.0)]
        genesis_block = Block(index=0, transactions=genesis_tx, previous_hash="0" * 64, nonce=0, timestamp=1231006505.0)
        # Minar el bloque génesis con la dificultad fijada
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def add_transaction(self, transaction: Transaction) -> bool:
        """Agrega una transacción válida al pool de espera."""
        if transaction.amount <= 0:
            return False
        self.unconfirmed_transactions.append(transaction)
        return True

    def mine_pending_transactions(self, miner_address: str) -> Optional[Block]:
        """
        Empaqueta las transacciones pendientes en un nuevo bloque,
        asigna la recompensa de minería (Coinbase) y ejecuta Proof-of-Work.
        """
        if not self.unconfirmed_transactions:
            return None

        # Recompensa para el minero (regla de consenso)
        reward_tx = Transaction(sender="NETWORK_REWARD", recipient=miner_address, amount=6.25)
        transactions_to_mine = self.unconfirmed_transactions.copy()
        transactions_to_mine.insert(0, reward_tx)

        new_block = Block(
            index=len(self.chain),
            transactions=transactions_to_mine,
            previous_hash=self.last_block.hash,
            nonce=0
        )

        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.unconfirmed_transactions.clear()
        return new_block

    def is_chain_valid(self) -> Dict[str, Any]:
        """
        Audita criptográficamente toda la cadena de bloques:
        1. Comprueba que el 'previous_hash' apunte exactamente al hash del bloque anterior.
        2. Verifica que el hash registrado coincida con el contenido computado (inmutabilidad).
        3. Verifica que el hash cumpla con el target de dificultad Proof-of-Work.
        """
        target = "0" * self.difficulty
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # 1. Enlace criptográfico secuencial
            if current_block.previous_hash != previous_block.hash:
                return {
                    "valid": False,
                    "error": f"Ruptura de enlace en Bloque #{current_block.index}: previous_hash no coincide con el hash del Bloque #{previous_block.index}.",
                    "block_index": current_block.index
                }

            # 2. Integridad del hash propio (detección de alteración de transacciones)
            if current_block.hash != current_block.compute_hash():
                return {
                    "valid": False,
                    "error": f"Corrupción en Bloque #{current_block.index}: el hash registrado no coincide con el contenido computado.",
                    "block_index": current_block.index
                }

            # 3. Cumplimiento de prueba de trabajo
            if not current_block.hash.startswith(target):
                return {
                    "valid": False,
                    "error": f"Fallo de PoW en Bloque #{current_block.index}: no cumple la dificultad requerida ({self.difficulty} ceros).",
                    "block_index": current_block.index
                }

        return {
            "valid": True,
            "message": "Cadena 100% íntegra, inmutable y verificada por consenso criptográfico SHA-256.",
            "total_blocks": len(self.chain)
        }


def run_demonstration():
    print("=" * 75)
    print("DEMOSTRACIÓN INTERACTIVA: BLOCKCHAIN CRIPTOGRÁFICO EDUCATIVO (SENA ADSO)")
    print("=" * 75)
    
    # 1. Inicialización
    print("\n[PASO 1] Inicializando Blockchain con dificultad PoW = 3...")
    bc = Blockchain(difficulty=3)
    print(f"-> Bloque Génesis creado: Hash={bc.chain[0].hash}")

    # 2. Agregar transacciones simulando el ejemplo del componente SENA (Pepito a Mario)
    print("\n[PASO 2] Registrando transacciones en el pool...")
    bc.add_transaction(Transaction(sender="Pepito", recipient="Mario", amount=1000000.0))
    bc.add_transaction(Transaction(sender="Mario", recipient="Distribuidor_Cafe", amount=450000.0))
    print("-> 2 transacciones agregadas.")

    # 3. Minar el Bloque 1
    print("\n[PASO 3] Minando Bloque #1 con algoritmo Proof-of-Work...")
    mined_1 = bc.mine_pending_transactions(miner_address="Minero_SENA_01")
    print(f"-> {mined_1.hash} (Nonce: {mined_1.nonce})")

    # 4. Agregar más transacciones y minar Bloque 2
    print("\n[PASO 4] Registrando lote 2 y minando Bloque #2...")
    bc.add_transaction(Transaction(sender="IBM_Food_Trust", recipient="Logistica_SENA", amount=12.5))
    bc.add_transaction(Transaction(sender="Koibanx_Pay", recipient="Cooperativa_Financiera", amount=8900.0))
    mined_2 = bc.mine_pending_transactions(miner_address="Minero_SENA_02")
    print(f"-> {mined_2.hash} (Nonce: {mined_2.nonce})")

    # 5. Verificación de integridad
    print("\n[PASO 5] Verificando validez e inmutabilidad de la cadena...")
    audit_ok = bc.is_chain_valid()
    print(f"-> Estado: {'VÁLIDA' if audit_ok['valid'] else 'INVÁLIDA'}")
    print(f"   Detalle: {audit_ok['message']}")

    # 6. Demostración del Principio de Inmutabilidad (Intento de Fraude)
    print("\n[PASO 6] DEMOSTRACIÓN DE SEGURIDAD: INTENTO DE ALTERACIÓN MALICIOSA")
    print("-> Atacante altera la transacción de Pepito a Mario en el Bloque #1 de $1'000.000 a $99'000.000...")
    bc.chain[1].transactions[1].amount = 99000000.0

    print("-> Ejecutando auditoría de la red tras la alteración...")
    audit_fraud = bc.is_chain_valid()
    print(f"-> Resultado de la red: {'VÁLIDA' if audit_fraud['valid'] else 'FRAUDE DETECTADO'}")
    print(f"   Alerta de Consenso: {audit_fraud['error']}")
    print("=" * 75)


if __name__ == "__main__":
    run_demonstration()
