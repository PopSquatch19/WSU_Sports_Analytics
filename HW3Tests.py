#------------------------------------------------------
#-- INCLUDE YOUR OWN TESTS IN THIS FILE
#------------------------------------------------------
import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    def setUp(self):
        self.barca_games = {
            2000: { "MADRID":(2,0), "NAPOLI":(6,2), "CHELSEA":(1,2), "JUVENTUS":(6,1), "MILAN":(2,0), "MCC":(5,3), "TOTTENHAM":(3,2),
                    "CRYSTALPALACE":(1,0)},
            2001: {"LIVERPOOL":(1,2), "LEICESTER":(4,3), "SOCIEDAD":(1,0), "MADRID":(3,0), "CHELSEA":(1,0),
                    "MCU":(3,2),"MCC":(2,3),"JUVENTUS":(1,0)},
            2002: {"LEVANTE":(3,0), "MCU":(1,0), "ARSENAL":(5,3), "EVERTON":(2,1), "JUVENTUS":(4,3), "LIVERPOOL":(2,3), "CHELSEA":(2,0), 
                    "MADRID":(3,2), "MILAN":(2,3), "LEICESTER":(2,1), "CRYSTALPALACE":(2,1)} }

        self.happyMeal = """ 
            hamburger 
            hamburger fries 
            hamburger fries milk  
            hamburger fries milk toy
           """
        self.myGraph = {'A':{'B','C','D'},'B':{'C','D'},'C':{'B','D'},'D':{}}
        
    
    #--- Problem 1----------------------------------
    
    def test_all_games(self):
        output = { 'MADRID': {2000: (2,0), 2001: (3,0), 2002: (3,2)},
                   'NAPOLI': {2000: (6,2)},
                   'CHELSEA': {2000: (1,2), 2001: (1,0), 2002: (2,0)},
                   'JUVENTUS': {2000: (6,1), 2001: (1,0), 2002: (4,3)},
                   'MILAN': {2000: (2,0), 2002: (2,3)},
                   'MCC': {2000:(5,3), 2001: (2,3)},
                   'TOTTENHAM': {2000: (3,2)},
                   'CRYSTALPALACE': {2000: (1,0), 2002: (2,1)},
                   'LIVERPOOL': {2001: (1,2), 2002: (2,3)},
                   'LEICESTER': {2001: (4,3), 2002: (2,1)},
                   'SOCIEDAD': {2001: (1,0)},
                   'MCU': {2001:(3,2), 2002: (1,0)},
                   'LEVANTE': {2002: (3,0)},
                   "ARSENAL":{2002: (5,3)},
                   'EVERTON': {2002: (2,1)}
                    }

        self.assertDictEqual(all_games(self.barca_games),output)

        # Provide your own test here. Create your own input dictionary for this test (similar to self.wsu_games).
    
    #--- Problem 2----------------------------------
    def test_common_teams(self):
        output = {'MADRID':[(2 , 0), (3, 0), (3, 2)],'CHELSEA': [(1, 2), (1, 0), (2, 0)], 'JUVENTUS': [(6, 1), (1, 0), (4, 3)]}

        self.assertDictEqual(common_teams(self.barca_games),output)
        # Provide your own test here. Create your own input dictionary for this test (similar to self.my_cats_log). 
        # You can re-use the data dictionary you created for all_games test.

    #--- Problem 3 ----------------------------------
    def test_get_wins(self):
        
        output1 = [(2001, (1, 0))]

        self.assertListEqual(get_wins(self.barca_games,'SOCIEDAD'),output1 )


        output2 = [(2000, (2, 0)), (2001, (3, 0)), (2002, (3, 2))]

        self.assertListEqual(get_wins(self.barca_games,'MADRID'),output2 )
        # Provide your own test here. Create your own input dictionary for this test (similar to self.wsu_games).
        # You can re-use the data dictionary you created for all_games test.

    #--- Problem 4----------------------------------
    def test_wins_by_year(self):
        
        output = [(2000, 7), (2001, 6), (2002, 9)]

        self.assertListEqual(wins_by_year(self.barca_games),output )
        # Provide your own test here. Create your own input dictionary for this test (similar to self.wsu_games).
        # You can re-use the data dictionary you created for all_games test.
    
    #--- Problem 5 ----------------------------------
    def test_longest_path(self):

        self.assertEqual(longest_path(self.myGraph,'A'),4)
    
    
    
        # Provide your own test here. Create your own graph dictionary for this test (similar to self.graph). 

    #--- Problem 6----------------------------------
    def test_counter(self):
        
        self.tokens = [('fries', 1), ('hamburger', 3), ('fries', 2), ('milk', 1), ('hamburger', 4), ('fries', 3), ('milk', 2), ('toy', 1)]
        mywords = counter(self.happyMeal)
        mywords.__next__()   # skip first tuple ('hamburger',1)
        mywords.__next__()   # skip first tuple ('hamburger',2)


        rest = []
        for word in mywords:  
            rest.append(word)
        self.assertListEqual(rest,self.tokens)
        # Provide your own test here. Initialize the iterator with your own input
    
if __name__ == '__main__':
    unittest.main()

