# CptS 355 - Spring 2022 - Assignment 3 - Python

# Please include your name and the names of the students with whom you discussed any of the problems in this homework
# Name: #Aviv Y
# Collaborators: 

# wsu_games = {

#             2018: { "WYO":(41,19), "SJSU":(31,0),  "EWU":(59,24), "USC":(36,39), "UTAH":(28,24), 

#                    "ORST":(56,37), "ORE":(34,20), "STAN":(41,38), "CAL":(19,13), "COLO":(31,7), 

#                    "ARIZ":(69,28), "WASH":(15,28), "ISU":(28,26)},

#             2019: {"NMSU":(58,7), "UNCO":(59,17), "HOU":(31,24), "UCLA":(63,67), "UTAH":(13,38), 

#                     "ASU":(34,38), "COLO":(41,10), "ORE":(35,37), "CAL":(20,33), "STAN":(49,22), 

#                    "ORST":(54,53), "WASH":(13,31), "AFA":(21,31) },

#             2020: {"ORST":(38,28), "ORE":(29,43), "USC":(13,38), "UTAH":(28,45)},

#             2021: { "USU":(23,26), "PORT ST.":(44,24), "USC":(14,45), "UTAH":(13,24), "CAL":(21,6),

#                    "ORST":(31,24), "STAN":(34,31), "BYU":(19,21), "ASU":(34,21), "ORE":(24,38), 

#                    "ARIZ":(44,18), "WASH":(40,13), "CMU":(21,24)} }


debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1 - all_games - 8%


from functools import reduce






def all_games(wsu_games):

     new_dict = {}

     for year in wsu_games.keys():
          for school in wsu_games.get(year,{}).keys():
               if school in new_dict.keys():
                    new_dict[school][year] = wsu_games.get(year).get(school)
               else:
                    new_dict[school] = {}
                    new_dict[school][year] = wsu_games.get(year).get(school)
     return new_dict


## problem 2 - common_teams - 15%


def common_teams(wsu_games):
     
     team = ""
     allTeams = False
     new_dict = {}
     trash_teams = []


     while not allTeams:

          firstYear = list(wsu_games.keys())[0]
          for school in wsu_games[firstYear].keys():
               if school in new_dict.keys() or school in trash_teams:
                    allTeams = True
               else:
                    allTeams = False
                    break
          if allTeams:
               break
          
          for year in wsu_games.keys():
               for school in wsu_games[year].keys():
                    if school in trash_teams or school in new_dict.keys():
                         continue
                    if team == "":
                         team = school 
                         break
               
               if team != "":
                    if team in wsu_games[year].keys():
                         continue
                    else:
                         trash_teams.append(team)
                         #print(f"added {team} to trash team")
                         team = ""
                         break
          
          if team == "":
               
               continue
          else:
               new_dict[team] = []

               for year in wsu_games.keys():
                    new_dict[team].append(wsu_games[year][team])

               #print(f"added {team} to new team")   
               team = ""
               

          firstYear = list(wsu_games.keys())[0]
          for school in wsu_games[firstYear].keys():
               if school in new_dict.keys() or school in trash_teams:
                    allTeams = True
                    
               else:
                    allTeams = False
                    break
                    
                    
     return new_dict


     


## problem 3 - get_wins - 16%


def mapHelper(tuple,team):         #defined a helper 

     score = tuple[1].get(team)

     if score[0] > score[1]:
          return (tuple[0],score)
     else:
          return None


def get_wins(wsu_games,team):

     filterYear = dict(filter(lambda tuple: team in tuple[1].keys(),wsu_games.items()))     #.items() test after, .items was needed

     retList = filterYear.items()
     mapper = map(lambda tuple: mapHelper(tuple,team) ,retList)

     encloser = list(filter(lambda x: x != None, list(mapper)))

     return encloser




## problem 4 - wins_by_year - 16%




def wins_by_year (wsu_games):

    winCounter = 0

    getWins = lambda wsu_games: list(map(lambda score: 1 if score[0] > score[1] else 0, wsu_games.values()))

    

    getWin = list(map(lambda tuple: (tuple[0],getWins(tuple[1])) ,wsu_games.items())) # this gets the score tuple =   in tuple[1].keys()


    #print(getWin)
    
    sumTuple = lambda sum: (reduce(lambda val,val2: val+val2,sum))


    checkScore = lambda tuple: (tuple[0],sumTuple(tuple[1]))
    

    mapItr = map(checkScore, getWin)

    #print(list(mapItr))

    

    return list(mapItr)



    

    
#     winCheck = dict(filter(lambda tuple: 1 if tuple[0] > tuple[1] else 0, wsu_games.items()))

#     if getWin == 1:
#          winCounter += 1
#          return ((count(winCheck)))
#     else:
#          return None


    
    
    

#     returnList = getWin.items()

#     print("CHECK")
    

    


#     winMap = map(getWin,returnList)

#     return list((getWin,winMap))

    #retList = winCheck.items()

    #winMap = map(winCheck,wsu_games.items())

   # encloser = list(winMap)

    #if winCheck == 1:         
         #winCounter += 1
        # return # (###, ###) ??
    #else:
          #return None
          
       
     #winCheck = filter(lambda tuple: 1 if tuple[0] > tuple[1] else 0, wsu_games.items())


## problem 5 - longest_path - 16% 

def longestHelper(graph,node,path):

     path = path + [node]

     if graph[node] =={}:
          return path
     else:
          longest_path = None


          for edgeNode in graph[node]:
                    if edgeNode not in path:
                         tempPath = longestHelper(graph,edgeNode,path)

                         if tempPath:
                              if not longest_path or len(longest_path) < len(tempPath):
                                   longest_path = tempPath
          return longest_path


def longest_path(graph,node):
     return len(longestHelper(graph,node,[]))




## problem 6 - counter - 20% 

class counter(object):

     def __init__(self,str):

          self.input = iter(str)
          self.current = self._getNextWord()
          while self.current == '':
               self.current = self._getNextWord()
          self.d ={}


     def _getNextWord(self):

          word = []

          try:
               for nxt in self.input:
                    if nxt == " " or nxt=="\n":
                         return ''.join(word).lower()
                    else:
                         word.append(nxt)
               current = None

          except:
               current = None
          #current = ''.join(word).lower()
          return current


     def __next__(self):

          

          if self.current is None:
               raise StopIteration

          word = self.current
          self.current = self._getNextWord() 

          while self.current == "":
               self.current = self._getNextWord()

          if word in self.d.keys():
               self.d[word] = self.d[word] + 1

          else:
               self.d[word] = 1 

          
          # return (word, self.d[word]) 
          return (word, self.d[word])

          #update the dict d with the wordcount after I get word, if valid

       
     def __iter__(self):
          return self

# test_text = "  CptS 355  EE 415 "
# it = counter(test_text)
# for i in it:
#      print(i)