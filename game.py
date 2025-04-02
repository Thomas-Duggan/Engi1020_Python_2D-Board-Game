def create_board(n):
    """Create a new, empty game board.

    Parameters
    ----------
    n : int
      The width of the game board

    Returns
    -------
    A representation of the game board that can be passed back into other
    functions in this module. This representation should be iterable and
    support the len() function.
    """
    board = []
    for i in range (n):
        board += [" "]
    
    return board
    

def place_piece(board, p):
    """Place a piece on the board.

    Parameters
    ----------
    board
      A board as returned from create_board().

    p : str
      The piece to place.
      If it is a triangle, place at the far left of the board.
      If it is a square, place at the far right of the board.
      If it is neither, return False.

    Returns
    -------
    True if the piece could be placed, False if it could be not
    (e.g., if the relevant starting square is already occupied or if the
     piece is not a valid piece).
    """
    success = False
    
    if p == "triangle" or p == "▲":
        if board[0] == " ":
            board[0] = "▲"
            success = True
    elif p == "square" or p == "■":
        if board[-1] == " ":
            board[-1] = "■"
            success = True
            
    return success
        

def check_move(board, starting_square, ending_square):
    """Is it legal to move the piece at one square to another?

    Parameters
    ----------
    board
      A board as returned from create_board().

    starting_square : int [0, len(board))
      The index of a piece

    ending_square : int [0, len(board))
      The index where the piece would like to move

    Returns
    -------
    True if the proposed move is legal,
    False if it is not.
    """
    if starting_square == ending_square or ending_square <= -1 or ending_square >= len(board):
        return False

    if board[starting_square] == "■":
        if ending_square == starting_square-1:
            if board[ending_square] == "▲" and board[starting_square-1] == "▲":
                return False
            success = True
        elif ending_square == starting_square-2 and board[starting_square-1] == "▲" and board[starting_square-2] == " ":
            success = True
        else:
            success = False
            
    elif board[starting_square] == "▲":
        if ending_square == starting_square+1:
            if board[ending_square] == "■" and board[starting_square+1] == "■":
                return False
            success = True
        elif ending_square == starting_square+2 and board[starting_square+1] == "■" and board[starting_square+2] == " ":
            success = True
        else:
            success = False
    
    else:
        success = False
            
            
    return success
    

def move_piece(board, starting_square, ending_square):
    """Move a piece from one square to another.

    Parameters
    ----------
    board
      A board as returned from create_board().

    starting_square : int [0, len(board))
      The index of a piece

    ending_square : int [0, len(board))
      The index where the piece would like to move

    Pre-condition
    --------------
    The proposed move is legal

    Post-condition
    --------------
    The piece has been moved in the board
    """
    success = False
    if check_move(board,starting_square,ending_square) == True:
        if board[starting_square] == "■":
            if board[ending_square] == " " and board[starting_square-1] != "▲":
                board[starting_square] = " "
                board[ending_square] = "■"
                
            elif board[ending_square] == "▲":
                board[starting_square] = " "
                board[ending_square] = "■"
                
            elif ending_square == starting_square-2 and board[starting_square-1] == "▲":
                board[starting_square] = " "
                board[starting_square-1] = " "
                board[ending_square] = "■"
 
 
        elif board[starting_square] == "▲":
            if board[ending_square] == " " and board[starting_square+1] != "■":
                board[starting_square] = " "
                board[ending_square] = "▲"
                
            elif board[ending_square] == "■":
                board[starting_square] = " "
                board[ending_square] = "▲"
                
            elif ending_square == starting_square+2 and board[starting_square+1] == "■":
                board[starting_square] = " "
                board[starting_square+1] = " "
                board[ending_square] = "▲"


def moves(board, player):
    """Find all of the valid moves available to a player.

    Parameters
    ----------
    board
      A board as returned from create_board().

    player : str (▲ or ■)
      The player whose turn it is to move.

    Returns
    -------
    A set of possible legal moves, where each move is represented by a
    tuple of (starting_square, ending_square). Placing a piece on the board is
    represented by the tuple (None, starting_square).

    If no legal moves are possible for a player, the empty set is returned.
    """
    
    move_list = []
    
    if player == "■":
        for x in range(board.count("■")):
            for i in range(len(board)):
                if board[i] == "■":
                    if board[i-1] == ' ':
                        move_list.append(tuple([i,i-1]))
                    if board[i-1] == '▲' and board[i-2] == ' ':
                        move_list.append(tuple([i,i-2]))
        if board[len(board)-1] == " ":
            move_list.append(tuple([None,len(board)-1]))
        
            
    elif player == "▲":
        for x in range(board.count("▲")):
            for i in range(len(board)):
                if board[i] == "▲":
                    if board[i+1] == ' ':
                        move_list.append(tuple([i,i+1]))
                    if board[i+1] == '■' and board[i+2] == " ":
                        move_list.append(tuple([i,i+2]))
        if board[0] == " ":
            move_list.append(tuple([None,0]))
        
        
    else:
        return None

    
    return set(move_list)
        

def choose_move(board, player):
    """Choose a move for a player.

    Parameters
    ----------
    board
      A board as returned from create_board().

    player : str (▲ or ■)
      The player whose turn it is to move.

    Returns
    -------
    A tuple of (starting_square, ending_square) representing a legal move
    for that player, or None if there is no legal move.
    """
    best_move = None
    move_set = list(moves(board, player))
    for i in range(len(move_set)):
        if move_set[i][0] == None:
            return move_set[i]
        else:
            if player == "▲":
                if move_set[i][1] <= move_set[i-1][1]:
                    best_move = move_set[i]
            if player == "■":
                if move_set[i][1] >= move_set[i-1][1]:
                    best_move = move_set[i]        
    return best_move
        
        
        