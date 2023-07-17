from AI.simple_player import SimpleAgent 
from AI.probability_player import ProbAgent
from AI.simple_player_memory import ModelAgent
from AI.Learning_player import LearningAgent

import unittest

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

    def test_ModelAgent(self):
        testAgent = ModelAgent(name = "Model", brisChance=0.2,chance=0.5)
        testAgent.PotentialCards = [1,2,3,4,5,6]
        self.assertEqual(testAgent.createHands(),[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 3, 4), (1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (1, 5, 6), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6), (2, 5, 6), (3, 4, 5), (3, 4, 6), (3, 5, 6), (4, 5, 6)])

    def test_ProbAgentDeck(self):
        testAgent = ModelAgent(name = "Model", brisChance=0.2,chance=0.5)
        testAgent.deal_hand([('4', 'Cups'),('2', 'Swords'),('1', 'Cups')])
        self.assertEqual(len(testAgent.createHands()),7770)

    def test_LearningAgent(self):
        chances = {"pointless":{0.50:0.5},"brispointless":{0.50:0.50},"Jack":{0.50:0.50},"Knight":{0.50:0.25},'King':{0.50:0.25},"3":{0.50:0.25},
                   '1':{0.50:0.25},'brisJack':{0.50:0.25},'brisKnight':{0.50:0.25},"brisKing":{0.50:0.25},"bris3":{0.50:0.25},"bris1":{0.50:0.25}}
        testAgent = LearningAgent(name = "Model", brisChance=0.2,chance=chances)
        testAgent.hand = [("4","Swords"),("4","Suns"),("Jack","Clubs")]
        self.assertEqual(testAgent.choose_card("Suns",True,None),("4","Suns"))

    def test_LearningAgent(self):
        tmpdict = {}
        i = 1
        while i > 0:
            i = round(i - 0.01,2)
            tmpdict.update({i:0.9}) 

        chances = {"pointless":tmpdict,"brispointless":tmpdict,"Jack":tmpdict,"Knight":tmpdict,'King':tmpdict,"3":tmpdict,
                   '1':tmpdict,'brisJack':tmpdict,'brisKnight':tmpdict,"brisKing":tmpdict,"bris3":tmpdict,"bris1":tmpdict}
        testAgent = LearningAgent(name = "Model", brisChance=0.2,chance=chances)
        testAgent.hand = [("4","Swords"),("4","Suns"),("Jack","Clubs")]
        self.assertEqual(testAgent.choose_card("Suns",True,None),[0.33,0.66,1])
        print(testAgent.cardChances["brisJack"])
if __name__ == '__main__':
    unittest.main()
