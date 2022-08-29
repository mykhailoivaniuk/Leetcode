class UndergroundSystem:

    def __init__(self):
        self._stations = {}
        self._passengers = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if self._passengers.get(id) is not None:
            raise ValueError("Passenger can'be checked in in 2 places")
        if self._stations.get(stationName) is None:
            self._stations[stationName] = {}
        self._passengers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_name, start_time = self._passengers[id]
        del self._passengers[id]
        self.add_trip_info(start_name, stationName, t - start_time);

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip_info = self._stations[startStation][endStation]
        return trip_info[0] / trip_info[1]
        
    def add_trip_info(self, startName: str, endName: str, duration: int) -> None:
        if self._stations[startName].get(endName) is None:
            self._stations[startName][endName] = [0, 0]
        trip_info = self._stations[startName][endName]
        trip_info[0] += duration
        trip_info[1] += 1

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)