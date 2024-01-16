class Spot():
    def __init__(self, x, y, piece):
        self.piece = piece
        self.x = x
        self.y = y
    def getPiece(self):
        return self.piece
    def setPiece(self,piece):
        self.piece = piece
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
        self.x = x
    def setY(self,y):
        self.y = y
    
class Piece():
    def __init__(self, white):
        self.white = white
        self.killed = False
    def setWhite(self,white):
        self.white = white
    def isWhite(self):
        return self.white
    def isKilled(self):
        return self.killed
    def setKilled(self,killed):
        self.killed = killed

class King(Piece):
    def __init__(self,white):
        super().__init__(white)
        self.castlingDone = False
    def isCastlingDone(self):
        return self.castlingDone
    def setCastlingDone(self):
        self.castlingDone = True
    def canMove(self,board,start,end):
        pass
    def isValidCastling(self,board,start,end):
        pass
    def isCastlingMove(self,start,end):
        pass

class Queen(Piece):
    def __init__(self,white):
        super().__init__(white)
    def canMove(self,board,start,end):
        pass
    def move(self,board,start,end):
        pass

class Knight(Piece):
    def __init__(self,white):
        super().__init__(white)
    def canMove(self,board,start,end):
        if (end.getPiece().isWhite()==self.isWhite()):
            return False
        else:
            board.get
    def move(self,board,start,end):
        pass

class Bishop(Piece):
    def __init__(self,white):
        super().__init__(white)
    def canMove(self,board,start,end):
        pass
    def move(self,board,start,end):
        pass

class Rook(Piece):
    def __init__(self,white):
        super().__init__(white)
    def canMove(self,board,start,end):
        pass
    def getMoves(self,board,start):
        moves = []
        sx = start.getX()
        sy = start.getY()
        if(self.isWhite()):
            blpx = False
            blnx = False
            blpy = False
            blny = False
            for i in range(1,7):
                if((board.isBoxEmpty(sx,sy+i)) and not blpy):
                    moves.append(board.getBox(sx,sy+i))
                elif(board.isBoxWhite(sx,sy+i) and not blpy):
                    blpy = True
                elif(board.isBoxBlack(sx,sy+i) and not blpy):
                    moves.append(board.getBox(sx,sy+i))
                    blpy = True
                

                if((board.isBoxEmpty(sx,sy-i)) and not blny):
                    moves.append(board.getBox(sx,sy-i))
                elif(board.isBoxWhite(sx,sy-i) and not blny):
                    blny = True
                elif((board.isBoxBlack(sx,sy-i)) and not blny):
                    moves.append(board.getBox(sx,sy-i))
                    blny = True
                

                if((board.isBoxEmpty(sx-i,sy)) and not blnx):
                    moves.append(board.getBox(sx-i,sy))
                elif(board.isBoxWhite(sx-i,sy) and not blnx):
                    blnx = True  
                elif((board.isBoxBlack(sx-i,sy)) and not blnx):
                    moves.append(board.getBox(sx-i,sy))
                    blnx = True

                if((board.isBoxEmpty(sx+i,sy)) and not blpx):
                    moves.append(board.getBox(sx+i,sy))
                elif(board.isBoxWhite(sx+i,sy) and not blpx):
                    blpx = True
                elif((board.isBoxBlack(sx+i,sy)) and not blpx):
                    moves.append(board.getBox(sx+i,sy))
                    blpx = True
            return moves
        if(not self.isWhite()):
            blpx = False
            blnx = False
            blpy = False
            blny = False
            for i in range(1,7):
                if((board.isBoxEmpty(sx,sy+i)) and not blpy):
                    moves.append(board.getBox(sx,sy+i))
                elif(board.isBoxBlack(sx,sy+i) and not blpy):
                    blpy = True
                elif(board.isBoxWhite(sx,sy+i) and not blpy):
                    moves.append(board.getBox(sx,sy+i))
                    blpy = True
                

                if((board.isBoxEmpty(sx,sy-i)) and not blny):
                    moves.append(board.getBox(sx,sy-i))
                elif(board.isBoxBlack(sx,sy-i) and not blny):
                    blny = True
                elif((board.isBoxWhite(sx,sy-i)) and not blny):
                    moves.append(board.getBox(sx,sy-i))
                    blny = True
                

                if((board.isBoxEmpty(sx-i,sy)) and not blnx):
                    moves.append(board.getBox(sx-i,sy))
                elif(board.isBoxBlack(sx-i,sy) and not blnx):
                    blnx = True    
                elif((board.isBoxWhite(sx-i,sy)) and not blnx):
                    moves.append(board.getBox(sx-i,sy))
                    blnx = True
                

                if((board.isBoxEmpty(sx+i,sy)) and not blpx):
                    moves.append(board.getBox(sx+i,sy))
                elif(board.isBoxBlack(sx+i,sy) and not blpx):
                    blpx = True
                elif((board.isBoxWhite(sx+i,sy)) and not blpx):
                    moves.append(board.getBox(sx+i,sy))
                    blpx = True
                
            return moves
class Pawn(Piece):
    def __init__(self,white):
        super().__init__(white)
        self.firstmove = True
    def canMove(self,board,start,end):
        pass
    def getMoves(self,board,start):
        moves = []
        sx = start.getX()
        sy = start.getY()
        if(self.isWhite()):
            if(board.isBoxEmpty(sx,sy+1)):
                moves.append(board.getBox(sx,sy+1))
                if(self.firstmove and board.isBoxEmpty(sx,sy+2)):
                    moves.append(board.getBox(sx,sy+2))
            if(board.isBoxBlack(sx+1,sy+1)):
                moves.append(board.getBox(sx+1,sy+1))
            if(board.isBoxBlack(sx-1,sy+1)):
                moves.append(board.getBox(sx-1,sy+1))

        if(not self.isWhite()):
            if(board.isBoxEmpty(sx,sy-1)):
                moves.append(board.getBox(sx,sy-1))
                if(self.firstmove and board.isBoxEmpty(sx,sy-2)):
                    moves.append(board.getBox(sx,sy-2))
            if(board.isBoxWhite(sx+1,sy-1)):
                moves.append(board.getBox(sx+1,sy-1))
            if(board.isBoxWhite(sx-1,sy-1)):
                moves.append(board.getBox(sx-1,sy-1))
        return moves
    def move(self,board,start,end):
        pass
    def promote(self):
        pass

class Board:
    def __init__(self):
        self.boxes = [ [0]*8 for i in range(8)]
        self.boxes[0][0] = Spot(0,0,Rook(True))
        self.boxes[1][0] = Spot(1,0,Knight(True))
        self.boxes[2][0] = Spot(2,0,Bishop(True))
        self.boxes[3][0] = Spot(3,0,Queen(True))
        self.boxes[4][0] = Spot(4,0,King(True))
        self.boxes[5][0] = Spot(5,0,Bishop(True))
        self.boxes[6][0] = Spot(6,0,Knight(True))
        self.boxes[7][0] = Spot(7,0,Rook(True))

        self.boxes[0][1] = Spot(0,1,Pawn(True))
        self.boxes[1][1] = Spot(1,1,Pawn(True))
        self.boxes[2][1] = Spot(2,1,Pawn(True))
        self.boxes[3][1] = Spot(3,1,Pawn(True))
        self.boxes[4][1] = Spot(4,1,Pawn(True))
        self.boxes[5][1] = Spot(5,1,Pawn(True))
        self.boxes[6][1] = Spot(6,1,Pawn(True))
        self.boxes[7][1] = Spot(7,1,Pawn(True))

        self.boxes[0][7] = Spot(0,7,Rook(False))
        self.boxes[1][7] = Spot(1,7,Knight(False))
        self.boxes[2][7] = Spot(2,7,Bishop(False))
        self.boxes[3][7] = Spot(3,7,Queen(False))
        self.boxes[4][7] = Spot(4,7,King(False))
        self.boxes[5][7] = Spot(5,7,Bishop(False))
        self.boxes[6][7] = Spot(6,7,Knight(False))
        self.boxes[7][7] = Spot(7,7,Rook(False))

        self.boxes[0][6] = Spot(0,6,Pawn(False))
        self.boxes[1][6] = Spot(1,6,Pawn(False))
        self.boxes[2][6] = Spot(2,6,Pawn(False))
        self.boxes[3][6] = Spot(3,6,Pawn(False))
        self.boxes[4][6] = Spot(4,6,Pawn(False))
        self.boxes[5][6] = Spot(5,6,Pawn(False))
        self.boxes[6][6] = Spot(6,6,Pawn(False))
        self.boxes[7][6] = Spot(7,6,Pawn(False))

        for i in range(4):
            for j in range(8):
                self.boxes[j][i+2] = Spot(j,i+2,None)

    def getBox(self, x, y):
        if(x>7 or x<0 or y > 7 or y < 0):
            return None
        return self.boxes[x][y]
    def isBoxEmpty(self, x, y):
        box = self.getBox(x,y)
        if(box == None):
            return False
        elif(box.getPiece()==None):
            return True
        else:
            return False
    def isBoxWhite(self,x,y):
        box = self.getBox(x,y)
        if(box == None):
            return False
        elif(box.getPiece()==None):
            return False
        elif(box.getPiece().isWhite()):
            return True
    def isBoxBlack(self,x,y):
        box = self.getBox(x,y)
        if(box == None):
            return False
        elif(box.getPiece()==None):
            return False
        elif(not box.getPiece().isWhite()):
            return True
def main():
    board = Board()
    spot = board.getBox(0,0)
    piece = spot.getPiece()
    start = board.getBox(4,4)
    moves = piece.getMoves(board,start)
    print(len(moves))
    while(moves):
        m = moves.pop()
        print(m.getX(),m.getY())
    
main()