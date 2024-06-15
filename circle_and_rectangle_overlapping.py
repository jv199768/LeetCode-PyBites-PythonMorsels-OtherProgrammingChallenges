class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        Xn = max(x1, min(xCenter, x2))
        Yn = max(y1, min(yCenter, y2))
        Dx = Xn-xCenter
        Dy = Yn-yCenter
        return (Dx**2 + Dy**2) <= radius**2
        
