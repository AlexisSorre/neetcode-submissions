class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        pairs = sorted(zip(position, speed), reverse=True)


        fleet=0

        temps_flotte_devant = 0

        for pos, vit in pairs:
            temps = (target - pos) / vit
            if temps > temps_flotte_devant:
                fleet += 1
                temps_flotte_devant = temps

        return fleet