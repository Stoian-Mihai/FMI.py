import queue
from collections import defaultdict
class automaton:
    def __init__(self, type, input):
        self.states_count = int(input[0])
        self.letters_count = int(input[2])
        self.initial_state = int(input[4])
        self.final_state_count = int(input[5])
        final_states = input[6].split(" ")
        self.final_states = []
        for state in final_states:
            self.final_states.append(state)
        self.edges_count = int(input[7])
        self.edges=defaultdict(list)
        self.allStates = set()
        #for i in range(0, self.edges_count + 1):
            #self.edges.append([])
        for i in range(8,8 + self.edges_count):
            edge_string = input[i].split(" ")
            self.edges[int(edge_string[0])].append((edge_string[1],edge_string[2]))
            self.allStates.add(int(edge_string[0]))
            self.allStates.add(int(edge_string[2]))

class lNFA(automaton):
    def check_word(self, string):
        q = queue.Queue()
        q.put((self.initial_state,string))
        while q.empty() == False:
            pop = q.get()
            curent_state = int(pop[0])
            curent_string = str(pop[1])
            if self.__check_if_completed(curent_state,curent_string):
                return 1

            if len(self.edges[curent_state]) != 0:
                for edge in self.edges[curent_state]:
                    next_word = edge[0]
                    next_state = edge[1]
                    if next_word == '.':
                        a = (next_state,curent_string)
                        q.put(a)
                    else:
                        if next_word == curent_string[:1]:
                            a = (next_state,curent_string[1:])
                            q.put(a)
        return 0


    def __check_if_completed(self, curent_state, curent_string):
        for state in self.final_states:
            if state != '':
                if curent_state == int(state):
                    if curent_string == '' or curent_string == ' ':
                        return 1
        return 0

class DFA(automaton):
    def addNewFinalState(self):
        #Getting a new state number that is not used
        newFinalState = self.__getUnusedState()
        for finalState in self.final_states:
            self.edges[int(finalState)].append(('.',newFinalState))
            self.edges_count = self.edges_count + 1
        self.final_state_count = 1
        self.allStates.add(newFinalState)
        self.final_states = [newFinalState]

    def addNewInitialState(self):
        newInitialState = self.__getUnusedState()
        self.edges[newInitialState].append(('.',self.initial_state))
        self.initial_state = newInitialState
        self.edges_count = self.edges_count + 1

    def removeState(self, toRemoveState):
        newEdges = defaultdict(list)
        for key in list(self.edges):
            if key == toRemoveState:
                continue
            addIfStar = self.__getStar(toRemoveState)
            for edge in self.edges[key]:
                if int(edge[1]) == toRemoveState:
                    for nextEdge in self.edges[toRemoveState]:
                        if int(nextEdge[1]) != toRemoveState:
                            newEdges[key].append((edge[0]+addIfStar+nextEdge[0],nextEdge[1]))
        return newEdges
    def __getStar(self,state):
        starString = ""
        for edge in self.edges[state]:
            if int(edge[1]) == state:
                starString = starString + edge[0] + "*"
        return starString
    def __getUnusedState(self):
        newState = 1
        while (True):
            if newState in self.allStates:
                newState = newState + 1
            else:
                break
        return newState

    def getRegex(self):
        statesToRemove = []
        for state in self.allStates:
            statesToRemove.append(state)
        #print(statesToRemove)
        self.addNewFinalState()
        self.addNewInitialState()
        for toRemove in statesToRemove:
            newEdges = self.removeState(toRemove)
            self.deleteState(toRemove)
            for s in newEdges:
                for updateEdge in newEdges[s]:
                    self.edges[s].append(updateEdge)
            print(newEdges)
            self.concate()
            #print(self.edges)

    def deleteState(self,toRemove):
        del self.edges[toRemove]
        self.allStates.remove(toRemove)
        for key in self.edges:
            for edge in self.edges[key]:
                if int(edge[1]) == toRemove:
                    self.edges[key].remove(edge)
    def concate(self):
        for a in self.edges:
            for b in self.allStates:
                concat = ""
                edgesToRemove = []
                for edge in self.edges[a]:
                    if edge[1] == b:
                        concat = concat + edge[0] + "|"
                        #self.edges[a].remove(edge)
                        edgesToRemove.append(edge)
                if concat != "":
                    for toRm in edgesToRemove:
                        self.edges[a].remove(toRm)
                    self.edges[a].append((concat[:-1],b))


F = open("nfa.txt","r")
s = F.read()
s = s.split("\n")
dfa = DFA('nfa',s)
a = dfa.edges[1]
#a = a[0]
i = 8 + int(s[7])
n = int(s[i])
i+=1

#dfa.final_states.remove('')
#print(dfa.removeState(1))
print(dfa.final_states)
print(dfa.initial_state)
dfa.getRegex()
er = ""
print(dfa.edges)
for i in dfa.edges:
    for j in dfa.edges[i]:
        er = j[0]
print(er.replace('.',''))