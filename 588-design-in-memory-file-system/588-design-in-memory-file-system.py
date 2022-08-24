class Node:
    def __init__(self,name,nodeType):
        self.name=name
        self.type=nodeType
        self.children=None
        self.content=None
        if self.type=='dir':
            self.children={}
        else:
            self.content=''
    
    def updateFileTypeToDir(self):
        self.type='dir'
        self.children={}
        self.content=None
    
    def updateFileTypeToFile(self):
        self.type='file'
        self.children=None
        self.content=''
    
    @staticmethod
    def traverseNode(root,path):
        path=path.split('/')
        if path[0]=='':
            path.pop(0)
        resultList=[]
        for p in path:
            root=root.children[p]
        if root.type=='dir':
            for child in root.children:
                resultList.append(child)
        else:
            resultList.append(root.name)
        resultList.sort()
        return resultList
    
    @staticmethod
    def makedir(root,path):
        path=path.split('/')
        for p in path:
            if p in root.children:
                root=root.children[p]
            else:
                child=Node(p,'dir')
                root.children[p]=child
                root=root.children[p]
        return root
    
    @staticmethod
    def addContentToFile(root,path,content):
        file=Node.makedir(root,path)
        if file.type=='dir':
            file.updateFileTypeToFile()
        file.content+=content
    
    @staticmethod
    def readContentFromFile(root,path):
        file=Node.makedir(root,path)
        return file.content

    
class FileSystem:
    def __init__(self):
        self.root=Node('','dir')

    def ls(self, path: str) -> List[str]:
        return Node.traverseNode(self.root,path[1:])
        
    def mkdir(self, path: str) -> None:
        Node.makedir(self.root,path[1:])
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        Node.addContentToFile(self.root,filePath[1:],content)

    def readContentFromFile(self, filePath: str) -> str:
        return Node.readContentFromFile(self.root,filePath[1:])
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)