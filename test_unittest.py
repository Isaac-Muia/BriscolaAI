from simple_player import SimpleAgent  # The code to test
from probability_player import ProbAgent

import unittest   # The test framework

class Test_agents(unittest.TestCase):
    def test_SimpleAgent(self):

        testAgent = SimpleAgent(name = "Simple")
        testAgent.deal_hand([('4', 'Cups'),('2', 'Swords'),('1', 'Cups')])
        self.assertEqual(testAgent.choose_card('Cups', False, ('1', 'Swords')),('4', 'Cups'))

        testAgent.deal_hand([('1', 'Cups'),('King', 'Swords'),('4', 'Cups')])
        self.assertEqual(testAgent.choose_card('Cups', True, None), ('King', 'Swords'))

        testAgent.deal_hand([('1', 'Cups'),('King', 'Swords'),('4', 'Cups')])
        self.assertEqual(testAgent.choose_card('Cups', False, ('5', 'Swords')), ('King', 'Swords'))

        testAgent.deal_hand([('1', 'Cups'),('King', 'Swords'),('4', 'Cups')])
        self.assertEqual(testAgent.choose_card('Cups', False, ('4', 'Suns')), ('King', 'Swords'))

        testAgent.deal_hand([('1', 'Cups'),('King', 'Swords'),('4', 'Cups')])
        self.assertEqual(testAgent.choose_card('Cups', False, ('2', 'Cups')), ('King', 'Swords'))

        testAgent.deal_hand([('1', 'Cups'),('1', 'Swords'),('4', 'Cups')])
        self.assertEqual(testAgent.choose_card('Cups', False,  ('3', 'Swords')), ('1', 'Swords'))

    def test_ProbAgent(self):
        testAgent = ProbAgent(name = "Prob")
        testAgent.PotentialCards = [1,2,3,4,5,6]
        self.assertEqual(testAgent.createHands(),[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 3, 4), (1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (1, 5, 6), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6), (2, 5, 6), (3, 4, 5), (3, 4, 6), (3, 5, 6), (4, 5, 6)])
    
    def test_ProbAgentDeck(self):
        testAgent = ProbAgent(name = "Prob")
        testAgent.deal_hand([('4', 'Cups'),('2', 'Swords'),('1', 'Cups')])
        self.assertEqual(len(testAgent.createHands()),7770)



if __name__ == '__main__':
    unittest.main()