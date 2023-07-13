class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}

        for start, end in edges:
            if start in self.graphDict:
                self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]

        print('Graph Dict:', self.graphDict)

    def getFullPath(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graphDict:
            return []
        
        fullPath = []

        for node in self.graphDict[start]:
            if node not in path:
                newPath = self.getFullPath(node, end, path)

                for path in newPath:
                    fullPath.append(path)

        return fullPath
    
    def getShortestPath(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graphDict:
            return None
        
        shortestPath = None

        for node in self.graphDict[start]:
            if node not in path:
                newPath = self.getShortestPath(node, end, path)

                if newPath:
                    if shortestPath is None or len(shortestPath) > len(newPath):
                        shortestPath = newPath

        return shortestPath
    
if __name__ == '__main__':
    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]


    routeGraph = Graph(routes)
    start = 'Mumbai'
    end = 'New York'

    print(f'All paths between: {start} and {end}: ', routeGraph.getFullPath(start, end))
    print(f'Shortest path between {start} and {end}: ', routeGraph.getShortestPath(start, end))