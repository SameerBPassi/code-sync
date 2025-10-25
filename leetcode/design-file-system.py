class FileSystem:

    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths or not path or path[0] != '/' or path == '/':
            return False
        
        parent = path[:path.rfind('/')]
        if parent not in self.paths and len(parent) > 1: # / is a valid parent
            return False
        
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)