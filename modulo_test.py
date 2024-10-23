import unittest
from modulo import BinaryFA

class TestBinaryFA(unittest.TestCase):
    def setUp(self):
        self.fa = BinaryFA()

    def test_initial_state(self):
        self.assertEqual(self.fa.curState, "S0", "Initial state should be S0")

    def test_process_input_110(self):
        self.fa.ProcessInput("110")
        self.assertEqual(self.fa.curState, "S0", "Output should be in state S0 for input '110'")

    def test_process_input_101(self):
        self.fa.ProcessInput("101")
        self.assertEqual(self.fa.curState, "S2", "Output should be in state S2 for input '101'")

    def test_process_input_000(self):
        self.fa.ProcessInput("000")
        self.assertEqual(self.fa.curState, "S0", "Output should be in state S0 for input '000'")

    def test_process_input_111(self):
        self.fa.ProcessInput("111")
        self.assertEqual(self.fa.curState, "S1", "Output should be in state S1 for input '111'")

    def test_process_input_1100(self):
        self.fa.ProcessInput("1100")
        self.assertEqual(self.fa.curState, "S0", "Output should be in state S0 for input '1100'")

    def test_process_input_1001(self):
        self.fa.ProcessInput("1001")
        self.assertEqual(self.fa.curState, "S0", "Output should be in state S0 for input '1001'")

    def test_process_input_empty(self):
        self.fa.ProcessInput("")
        self.assertEqual(self.fa.curState, "S0", "Output should be in state S0 for empty input")

    def test_process_input_101010(self):
        self.fa.ProcessInput("101010")
        self.assertEqual(self.fa.curState, "S0", "Output should be in state S0 for input '101010'")

    def test_process_input_1101(self):
        self.fa.ProcessInput("1101")
        self.assertEqual(self.fa.curState, "S1", "Output should be in state S1 for input '1101'")

if __name__ == '__main__':
    unittest.main()
