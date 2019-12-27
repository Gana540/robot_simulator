#  Class to store the colors - am using this for better visual represenetation of the messages and the board.
class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Class that created the default Table where the Toy Robot can move in different directions.    
class Table(list):

    def __str__(self):
        return "\n ".join(" ".join(row) for row in self)

# The main class where the Game starts
    # initialises a default table and a Toy Robot (X)
    # takes input commands and processes it.
        # Place will be the first command that can be executed - example - place 1,2,EAST
        # After Place - there are multiple options to proceed - example - left , right , move or report
            # Left or Right  - will rotate the robot 90 degrees left or right to the current placed direction
            # Move - will move the robot toy towards the current placed or rotated direction (this can be executed post Place or left/right rotate commands).
            # report - this will output the current coordinates and direction of the Robot Toy.
class Robot_Game(object):
    MARKER_X = "X"
    MARKER__ = "_"
    CTRLS = [
        "west", 
        None,
        "east", 
        "south",    
        None,
        "north",  
    ]
    DIR_DICT = {'north':'west', 'west':'south', 'south':'east', 'east':'north'}
    EXIT = "stop"
    START = [0, 0]
    DEFAULT = [["_"] * 5 for _ in range(5)]
    
    # initialise the table
    def __init__(self):
        self.flag = True
        self.table = Table(Robot_Game.DEFAULT)
    # move the robot toy based on its previous position, it doesn't allow you to move outside the table(5 * 5) dimenstions
    def move_toy(self):
        px, py = self.prev_pos
        cx, cy = self.curr_pos
        if (-1 < cx < 5) and (-1 < cy < 5):
            self.table[4-px][py] = Robot_Game.MARKER__
            self.table[4-cx][cy] = Robot_Game.MARKER_X
        else:
            print(bcolors().FAIL, "Please MOVE in a direction within the table(5 X 5)", bcolors().ENDC)
            self.curr_pos = self.prev_pos[:]
            self.move_toy()
    # alter the current position before moving the Toy. This just orchstrates the Movement of the toy.
    def moveCommand(self):
      if(hasattr(self,'curr_pos')):  
        d = Robot_Game.CTRLS.index(self.direction)
        self.prev_pos = self.curr_pos[:]
        self.curr_pos[d > 2] += d - (1 if d < 3 else 4)
        self.move_toy()
      else:
        print(bcolors().FAIL, "Plase Place the toy in the table(5 X 5) before you can move it", bcolors().ENDC)
    # Rotate the toy 90 degrees left from the current position.
    def rotateToyLeft(self):
        if(hasattr(self,'direction')):
            for key, value in Robot_Game.DIR_DICT.items():
                if key == self.direction:
                    self.direction = value
                    break
        else:
          print(bcolors().FAIL, "Plase Place the toy in the table(5 X 5) before you can move it", bcolors().ENDC)
    # Rotate the toy 90 degrees right from the current position.
    def rotateToyRight(self):
        if(hasattr(self,'direction')):
            for key, value in Robot_Game.DIR_DICT.items():
                if value == self.direction:
                    self.direction = key
                    break
        else:
          print(bcolors().FAIL, "Plase Place the toy in the table(5 X 5) before you can move it", bcolors().ENDC)
    # Place the toy in the mentioned X & Y coordinates and direction.
        # This assumes 0,0 as the South West most corner
    def placeTheToy(self,ctrl):
        try:
            list = ctrl.replace(" ",",").split(",")
            self.prev_pos =  self.curr_pos if hasattr(self,'curr_pos') else Robot_Game.START[:]
            self.curr_pos = [int(list[1]),int(list[2])]
            self.direction = list[3]
            self.move_toy()
        except:
             print(bcolors().FAIL, "Please follow the standard PLACE X,Y,F format (example - Place 1,2,EAST)", bcolors().ENDC)    
    # Main method thats called when the program starts - This just orchestrates the methods based on the input command.
        # Prints the default Table. 
        # Gets Input commands 
        # orchstrates the methods based on the input command.
    def play(self):
        print(bcolors().OKBLUE, "Robot Toy : X",bcolors.ENDC)
        while self.flag:
            print (bcolors().OKBLUE, "\n*****TABLE*****",bcolors.ENDC)
            print(bcolors().OKBLUE,str(self.table),bcolors.ENDC)
            print (bcolors().OKBLUE,"\n****************",bcolors.ENDC)
            ctrl = input("Place(X,Y,F), left, right, Move, or Report ?").lower()
            if "move" in ctrl:
                self.moveCommand()
            elif "left" in ctrl:
                self.rotateToyLeft()
            elif "right" in ctrl:
                self.rotateToyRight()
            elif "report" in ctrl :
              try:
                print(bcolors().OKGREEN , "Output:", self.curr_pos[0],",",self.curr_pos[1] ,",",self.direction.upper(), bcolors().ENDC)
              except:
                print(bcolors().FAIL, "Nothing to Report - Please place the Toy on the table to report its coordinates and direction", bcolors().ENDC ) 
            elif "place" in ctrl :
                self.placeTheToy(ctrl)
            elif ctrl == Robot_Game.EXIT:
                self.flag = False
            else:
                print(bcolors().FAIL, "Invalid Input, Please use the standard set of commands inside the boundaries(5 X 5) of the table.", bcolors().ENDC )      
toy_robot = Robot_Game()
toy_robot.play()
