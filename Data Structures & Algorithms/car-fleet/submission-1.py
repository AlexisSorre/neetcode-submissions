#Iteration 2 avec la premiere voiture 
#hors de la boucle 

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        fleet = 1
        prevTime = (target-pairs[0][0])/pairs[0][1]
        for pair, vit in pairs[1:]:
            currTime = (target-pair)/vit
            if currTime >prevTime:
                fleet+=1
                prevTime=currTime
        return fleet



        