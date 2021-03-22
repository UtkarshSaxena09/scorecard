import random as r

class Match:

  def __init__(self):
    self.team1=input('Enter first team:')
    print("")
    self.team2=input('Enter second team:')
    print("")
    self.n=11
    self.overs=20
   
    self.player1=['MS Dhoni','Faf du Plessis','Ruturaj Gaikwad','Suresh Raina',
                  'Ambati Rayudu','Robin Uthappa','Ravindra Jadeja',
                  'Sam Curran','Dwayne Bravo','Mitchell Santner','Imran Tahir',
                  'Deepak Chahar','Shardul Thakur','Lungi Ngidi',
                  'Josh Hazlewood','Moeen Ali','Krishnappa Gowtham',
                  'Cheteshwar Pujara'
                  ]
    r.shuffle(self.player1)  
    self.player1=self.player1[:self.n]   # Selection of Playing 11.
   
    self.player2=['Rohit Sharma','Ishan Kishan','Suryakumar Yadav',
                  'Adam Milne','Aditya Tare','Chris Lynn','Dhawal Kulkarni',
                  'Hardik Pandya','Krunal Pandya','Jasprit Bumrah',
                  'James Neesham','Keiron Pollard','Nathan Counternile',
                  'Quinton Decock','Trent Boult','Piyush Chawla','Rahul Chahar',
                  'Arjun Tendulkar'
                  ]
    r.shuffle(self.player2)
    self.player2=self.player2[:self.n]
    self.captain1=r.choice(self.player1)
    self.captain2=r.choice(self.player2)
    self.team={self.team1:self.player1,self.team2:self.player2}
    return

  def toss(self):
    print('Toss is being done between ',self.team1,
          ' and ',self.team2)
         
    print("")
   
    print(self.captain1," is leading ",self.team1,
          " and ",self.team2," is being lead by ",
          self.captain2)
   
    print("")
   
    print("Both the captains are coming for the toss")
   
    print("")
   
    print("Now is the time for toss ",self.captain1,
          " will toss the coin and ",self.captain2,
          " will make the call" )
   
    print("")
       
    winner=r.choice([self.team1,self.team2])
    print(winner+' won the toss!!')
   
    print("")
   
    choose=r.choice(['bat','ball'])
    print(winner+' has chose to '+choose+' first!!')
   
    print("")

    if choose=='bat':
      if winner==self.team1:
        return self.team1,self.team2
      else:
        return self.team2,self.team1
   
    else:
      if winner==self.team1:
        return self.team2,self.team1
      else:
        return self.team1,self.team2

  def innings(self,bat,ball,temp):
    score=0
    wicket=0
   
    batsman_scores={k:0 for k in bat}
    bowler_wickets={k:0 for k in ball}
    bowler_runs={k:0 for k in ball}
    bowler_overs={k:0 for k in ball}
   
    strike=bat[0]    
    non_strike=bat[1]
    j=0
    k=0
   
    while j<(self.overs):
     
      if k==self.n-1:
        k=0
      else:
        k+=1
     
      bowler=ball[k]  
      i=0
     
      while i<6:
        s=r.choices([0,1,2,3,4,6,'W','Wide','No Ball'],
                    [0.45,0.2,0.1,0.01,0.1,0.04,0.02,0.04,0.04])
        t=s[0]

        if str(t).isdigit():
          bowler_runs[bowler]+=t
          i+=1
          if t in [0,2,4,6]:
            batsman_scores[strike]+=t
          else:
            batsman_scores[strike]+=t
            nons=strike
            strike=non_strike
            non_strike=nons
          score+=t
       
        elif t=='W':
          i+=1
          bowler_wickets[bowler]+=1
         
          if wicket>=(self.n-2):
            print(strike,' OUT')
            wicket+=1
            print('ALL OUT!!')
            break
          else:
            print(strike,' OUT')
            strike=bat[wicket+2]
            wicket+=1
       
        else:
          print(t)
          score+=1
          bowler_runs[bowler]+=1
 
        print(j+i/10,' ',score,'/',wicket,' ',strike,'*',batsman_scores[strike],
              non_strike,batsman_scores[non_strike],' ',bowler,
              bowler_runs[bowler],'/',bowler_wickets[bowler])
       
        if score >temp:
          print('BOWLING STATS:')
          for bowl in ball:
            print(bowl,':',bowler_overs[bowl],'/',bowler_runs[bowl],'/',
                  bowler_wickets[bowl])
          print()
          print('BATTING STATS:')
          for bats in bat:
            print(bats,':',batsman_scores[bats])
          print()
          return score,wicket
     
      bowler_overs[bowler]+=1
      ov=strike        
      strike=non_strike
      non_strike=ov
      print()
      j+=1
      if wicket>(self.n-2):
        break
    print("End of innings")
    print("")
    print('Total Score:',score,'/',wicket)
    print()

    print('BOWLING STATS:')
    print("")
    for bowl in ball:
      print(bowl,':',bowler_overs[bowl],'/',bowler_runs[bowl],'/',
            bowler_wickets[bowl])
    print()

    print('BATTING STATS')
    print("")
    for bats in bat:
      print(bats,':',batsman_scores[bats])

    return score,wicket
 
  def play(self):
    first,second=self.toss()
     
    score1,wicket1=self.innings(self.team[first],self.team[second],99999999)
    print("")
    print('Score of ',first,' after first innings: ',score1,'/',wicket1)

    score2,wicket2=self.innings(self.team[second],self.team[first],score1)
    #print('Score of ',first,' after first innings: ',score1,'/',wicket1)
    print("")
    print('Score of '+second+' after second innings: ',score2,'/',wicket2)
    ("")
   
    if score1==score2:
      print('Match Drawn!!')
   
    elif score1>score2:
      print(first+' won by '+str(score1 - score2)+' runs')
      print(r.choice([first]))
   
    else:
      print(second+' won by '+str(10-wicket2)+' wickets')  

m=Match()
m.play()
