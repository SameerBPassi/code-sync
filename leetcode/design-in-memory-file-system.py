class FileSystem:

    def __init__(self):
        self.root = {}

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)
        if isinstance(node, str):
            return [path.split('/')[-1]]
        return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path, create=True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = [p for p in filePath.split('/') if p]
        node = self.root
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        file_ = parts[-1]
        node[file_] = node.get(file_, "") + content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._traverse(filePath)
        return node
        
    def _traverse(self, path: str, create=False):
        node = self.root
        if path == '/': return node
        parts = [p for p in path.split('/') if p]
        for p in parts:
            if create:
                node = node.setdefault(p, {})
            else:
                node = node[p]
        return node    

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)