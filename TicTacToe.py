name_X = input("Who is player X? ")
name_O = input("Who is player O? ")
score_player_X = 0
score_player_O = 0

def display_board( b ):
    print( "  1 2 3" )
    for row in range( 3 ):
        print( row+1, end=" ")
        for col in range( 3 ):
            print( b[row][col], end=" " )
        print()

def winnertictactoe(a):
    try:
    	#rows
        for row in a:
            if row[0] == row[1] == row[2]:
                if str(row[0]) != "-":
                    return True

        #diagonal
        if a[0][0] == a[1][1] == a[2][2] or a[2][0] == a[1][1] == a[0][2]:
            if str(a[1][1]) != "-":
                return True

        #columns
        for i in range(3):
            if a[0][i] == a[1][i] == a[2][i]:
                if str(a[0][i]) != "-":
                    return True
    except:
        return False

def tictactoe_input():
    b = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ] 
    global score_player_X
    global score_player_O
    move_count = 0
    print ("A new game of tic tac toe! When you want to stop, type \" stop \" ")
    
    (display_board(b))

    for move in range(10):
    	# player O
        if move_count <9 and move_count%2 == 0:
            coordinate = input(name_X.title() + ", where do you want to place your X? Please insert \"row number , column number\": ")
            if coordinate == "stop":
            	print ("The game has ended. ")
            	break
            coor_strip = coordinate.strip()
            coor_split = coor_strip.split(",")
            row_coor = (int(coor_split[0])-1)
            col_coor = (int(coor_split[1])-1)

            if b[row_coor][col_coor] == "-":
            	b[row_coor][col_coor] = "X"
            	move_count +=1

            else:
            	print ("Sorry, this tile is not empty anymore. Please try again. ")
            	continue
            
            board = display_board(b)   

            if (winnertictactoe(b)) == True:
            	print ("Congratulations! " + name_X.title() + " has won!")
            	score_player_X += 1
            	move_count = 0
            	round_count += 1            	
            	b = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ] 
            	print ("Score is " + name_X + " : " + str(score_player_X) + " - " + name_O + " : " + str(score_player_O))
            	print ("\n")
            else:
            	continue

        #player X
        elif move_count <9 and move_count%2 == 1:
            coordinate = input(name_O.title() + ", where  do you want to place your O? Please insert \"row number , column number\": ")
            if coordinate == "stop":
            	break
            coor_strip = coordinate.strip()
            coor_split = coor_strip.split(",")
            row_coor = (int(coor_split[0])-1)
            col_coor = (int(coor_split[1])-1)

            if b[row_coor][col_coor] == "-":
            	b[row_coor][col_coor] = "O"
            	move_count +=1
            else:
            	print ("Sorry, this tile is not empty anymore. Please try again.")
            	continue

            board = display_board(b)

            if (winnertictactoe(b)) == True:
            	print ("Congratulations! " + name_O.title() + " has won!")
            	score_player_O += 1
            	move_count = 0             	
            	b = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ] 
            	print ("Score is " + name_X + " : " + str(score_player_X) + " - " + name_O + " : " + str(score_player_O))
            	print ("\n")
            else:
            	continue

        elif move_count == 9:
        	return "It's a draw!"
        	move_count == 0 


tictactoe_input()
