import sys

class Result:
    def __init__(self):
        self.no_of_teams = 0
        self.team_score_1 = []
        self.team_score_2 = []
        self.final_score = []
        self.games_played_each = 0

    # Calcute the wins and loss of each team.
    def wins_loss(self):
        for items in self.team_score_1:
            if items[1] == items[3]:
                for i in range(self.no_of_teams):
                    if items[0] == self.final_score[i][0]:
                        self.final_score[i][5]+=1
                    if items[2] == self.final_score[i][0]:
                        self.final_score[i][5]+=1
            if items[1] > items[3]:
                for i in range(self.no_of_teams):
                    if items[0] == self.final_score[i][0]:
                        self.final_score[i][3]+=1
                    if items[2] == self.final_score[i][0]:
                        self.final_score[i][4]+=1
            if items[1] < items[3]:
                for i in range(self.no_of_teams):
                    if items[0] == self.final_score[i][0]:
                        self.final_score[i][4]+=1
                    if items[2] == self.final_score[i][0]:
                        self.final_score[i][3]+=1

    # Calculate the goal scored for and against each team.      
    def for_against(self):
        for i in range(0,len(self.team_score_2),self.games_played_each):
            for j in range(1,self.games_played_each):
                self.team_score_2[i][1] += self.team_score_2[i+j][1]
                self.team_score_2[i][2] += self.team_score_2[i+j][2]
            self.final_score.append(self.team_score_2[i])

    # Calculate the total points accumulated.
    def points_count(self):
        for i in range(self.no_of_teams):
            self.final_score[i][6] = self.final_score[i][3] * 3 + self.final_score[i][5] * 1

    # Used to display the Final result.
    def final_output(self):

        # Printing final output when command line argument is given 
        if len(sys.argv) != 1:  
        
            print(sys.argv[1])
            print(len(sys.argv[1])*"=")
        
        self.final_score.sort(key=lambda x: (x[6], (x[1]-x[2])), reverse=True)
        print("\n")
        print("Team \t\t P \t W \t L \t D \t F \t A \t Diff \t Pts")
        for i in range(5):
            print(self.final_score[i][0] ,"\t",self.games_played_each,"\t", self.final_score[i][3] ,"\t", self.final_score[i][4] ,"\t", self.final_score[i][5] ,"\t", self.final_score[i][1] ,"\t", self.final_score[i][2],"\t",self.final_score[i][1]-self.final_score[i][2],"\t", self.final_score[i][6])

    # This function is used to read from the csv file and store it in a list
    def initialize(self):
        # Open file for calcutating the final result and store the values in a list
        f=open("Team.csv","r") 
        for country in f.readlines():  
            self.no_of_teams += 1
        f.close()

        # Open file for calcutating the final result and store the values in a list (TeamAndScore1)
        f=open("Score.csv","r")
        for lines in f.readlines():
            list=lines.split(",")
            self.team_score_1.append(list)

        # Store the no of goals for and againts and store it in list team_score_2.
        # Store goals for and against
        for items in self.team_score_1:
            items[1]=int(items[1])
            items[3]=int(items[3])
            self.team_score_2.append([items[0],items[1],items[3],0,0,0,0])
            self.team_score_2.append([items[2],items[3],items[1],0,0,0,0])

        self.games_played_each=int(len(self.team_score_2)/self.no_of_teams)
        self.team_score_2.sort()

        self.for_against()
        self.wins_loss()
        self.points_count()
        self.final_output()

        f.close()

r = Result()
r.initialize()