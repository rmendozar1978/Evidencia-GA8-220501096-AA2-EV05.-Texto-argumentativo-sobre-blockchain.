"""
================================================================================
PRUEBAS UNITARIAS AUTOMATIZADAS - SIMULADOR BLOCKCHAIN (SENA ADSO)
EVIDENCIA: GA8-220501096-AA2-EV05
APRENDIZ: RONALD FABIAN MENDOZA RODRIGUEZ
================================================================================
"""

import unittest
from blockchain import Blockchain, Block, Transaction


class TestBlockchain(unittest.TestCase):

    def setUp(self):
        """Inicializa una nueva instancia de blockchain antes de cada prueba."""
        self.blockchain = Blockchain(difficulty=2)

    def test_genesis_block_creation(self):
        """Valida que el bloque génesis sea creado correctamente."""
        self.assertEqual(len(self.blockchain.chain), 1)
        genesis = self.blockchain.chain[0]
        self.assertEqual(genesis.index, 0)
        self.assertEqual(genesis.previous_hash, "0" * 64)
        self.assertTrue(genesis.hash.startswith("00"))

    def test_add_transaction(self):
        """Valida que las transacciones válidas sean agregadas al pool."""
        tx = Transaction("Pepito", "Mario", 1000000.0)
        added = self.blockchain.add_transaction(tx)
        self.assertTrue(added)
        self.assertEqual(len(self.blockchain.unconfirmed_transactions), 1)

    def test_reject_invalid_transaction(self):
        """Valida que transacciones con montos negativos o nulos sean rechazadas."""
        tx_invalid = Transaction("Hacker", "Victima", -500.0)
        added = self.blockchain.add_transaction(tx_invalid)
        self.assertFalse(added)
        self.assertEqual(len(self.blockchain.unconfirmed_transactions), 0)

    def test_mining_and_block_chaining(self):
        """Valida que el minado cree un bloque nuevo y lo enlace al anterior."""
        self.blockchain.add_transaction(Transaction("Alice", "Bob", 10.0))
        new_block = self.blockchain.mine_pending_transactions("Miner_01")

        self.assertIsNotNone(new_block)
        self.assertEqual(len(self.blockchain.chain), 2)
        self.assertEqual(new_block.index, 1)
        self.assertEqual(new_block.previous_hash, self.blockchain.chain[0].hash)
        self.assertTrue(new_block.hash.startswith("00"))

    def test_chain_integrity_valid(self):
        """Valida que una cadena sin alteraciones pase la auditoría criptográfica."""
        self.blockchain.add_transaction(Transaction("Nodo1", "Nodo2", 50.0))
        self.blockchain.mine_pending_transactions("Miner_01")
        self.blockchain.add_transaction(Transaction("Nodo2", "Nodo3", 25.0))
        self.blockchain.mine_pending_transactions("Miner_02")

        validation = self.blockchain.is_chain_valid()
        self.assertTrue(validation["valid"])
        self.assertEqual(validation["total_blocks"], 3)

    def test_tamper_detection_in_transaction_data(self):
        """
        Valida que si un atacante altera un valor en un bloque intermedio,
        la red detecte la inconsistencia de hash de inmediato.
        """
        self.blockchain.add_transaction(Transaction("Pepito", "Mario", 1000000.0))
        self.blockchain.mine_pending_transactions("Miner_01")
        self.blockchain.add_transaction(Transaction("Mario", "Tienda", 200000.0))
        self.blockchain.mine_pending_transactions("Miner_02")

        # Intento de alteración de datos en el Bloque 1
        self.blockchain.chain[1].transactions[1].amount = 999999999.0

        validation = self.blockchain.is_chain_valid()
        self.assertFalse(validation["valid"])
        self.assertIn("Corrupción en Bloque #1", validation["error"])

    def test_tamper_detection_in_previous_hash_link(self):
        """
        Valida que si se altera el enlace previous_hash, la red lo detecte y rechace.
        """
        self.blockchain.add_transaction(Transaction("A", "B", 10.0))
        self.blockchain.mine_pending_transactions("Miner_01")
        self.blockchain.add_transaction(Transaction("B", "C", 5.0))
        self.blockchain.mine_pending_transactions("Miner_02")

        # Forzar un previous_hash alterado
        self.blockchain.chain[2].previous_hash = "abcdef0123456789" * 4
        self.blockchain.chain[2].hash = self.blockchain.chain[2].compute_hash()

        validation = self.blockchain.is_chain_valid()
        self.assertFalse(validation["valid"])
        self.assertIn("Ruptura de enlace en Bloque #2", validation["error"])


if __name__ == "__main__":
    unittest.main()
