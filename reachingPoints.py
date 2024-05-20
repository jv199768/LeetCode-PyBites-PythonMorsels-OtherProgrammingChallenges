class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if(tx<sx or ty<sy):
            return False
        if(sx==tx and sy==ty):
            return True
        if(sx==tx):
            if (tx > sx and (tx - sx)) % ty == 0:
                return True
        else:
            return False

        
