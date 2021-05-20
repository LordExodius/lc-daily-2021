# Oscar Yu
# May 17th, 2021

class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        # 1 = top left -> bottom right
        # -1 = top right -> bottom left
        
        numBalls = len(grid[0])
        endingLocations = []
        
        for ball in range(numBalls):
            currentX = ball
            currentY = 0
            blocked = False
            
            while currentY < len(grid):
                direction = grid[currentY][currentX]
                print("Ball", ball, "@", currentX, ",", currentY)
                
                #if going right
                if direction == 1:
                    print("Going Right")
                    #check to see if right side is blocked by wall or other thing
                    if currentX == len(grid[0]) - 1 or grid[currentY][currentX + 1] == -1:
                        print("Blocked")
                        endingLocations.append(-1)
                        break
                    else:
                        currentX += 1
                        currentY += 1
                        print("Went Right")
                
                #if going left
                else:
                    print("Going Left")
                    #check to see if left side is blocked by wall or other thing
                    if currentX == 0 or grid[currentY][currentX - 1] == 1:
                        print("Blocked")
                        endingLocations.append(-1)
                        break
                    else:
                        currentX -= 1
                        currentY += 1
                        print("Went Left")
            else:
                print("Ball", ball, "Exited")
                endingLocations.append(currentX)
                """
                if direction == 1:
                    endingLocations.append(currentX + 1)
                else:
                    endingLocations.append(currentX - 1)
                """
            
        return endingLocations
