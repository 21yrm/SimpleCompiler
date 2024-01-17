from llvmlite import ir
from Generator.Constants import Constants

class SymbolTable:
    '''
    符号表类
    '''
    def __init__(self):
        '''
        功能：建立�?�号�?
        参数：无
        返回：无
        '''
        #table：table[i]�?一�?字典，存着key，value�?
        self.Table = [{}]
        self.CurrentLevel = 0  

    def GetItem(self, item):
        '''
        功能：从符号表中获取元素
        参数：待获取的元素的key
        返回：成功：返回元素，失败返回None
        '''
        i = self.CurrentLevel
        while i >= 0:
            TheItemList = self.Table[i]
            if item in TheItemList:
                return TheItemList[item]
            i -= 1
        return None

    def AddItem(self, key, value):
        '''
        功能：向符号表中添加元素
        参数：待添加的key，value
        返回：成功{"result":"success"}，失�?{"result":"fail","reason":具体原因码}
        '''
        if key in self.Table[self.CurrentLevel]:
            return {"result": "fail", "reason": Constants.ERROR_TYPE_REDEFINITION}
        self.Table[self.CurrentLevel][key] = value
        return {"result":"success"}

    def JudgeExist(self, item):
        '''
        功能：判�?元素�?否在符号表里
        参数：待判断的元�?
        返回：�?�果表里有，true，否则false
        '''
        i = self.CurrentLevel
        while i >= 0:
            if item in self.Table[i]:
                return True
            i -= 1
        return False

    def EnterScope(self):
        '''
        功能：进入一�?新的作用域，增加一�?
        参数：无
        返回：无
        '''
        self.CurrentLevel += 1
        self.Table.append({})

    def QuitScope(self):
        '''
        功能：退出一�?作用域，退出一�?
        参数：无
        返回：无
        '''
        if self.CurrentLevel == 0:
            return
        self.Table.pop(-1)
        self.CurrentLevel -= 1
    
    def JudgeWhetherGlobal(self):
        '''
        功能：判�?当前变量�?否全局
        参数：无
        返回：是true，否则false
        '''
        if len(self.Table) == 1:
            return True
        else:
            return False

class Structure:
    '''
    结构体类
    '''
    def __init__(self):
        '''
        描述：初始化
        参数：无
        返回：无
        '''
        self.List = {}
    
    def AddItem(self, Name, MemberList, TypeList):
        '''
        描述：添加一�?元素
        参数：名称，成员列表，类型列�?
        返回：成功{"result":"success"}，失�?{"result":"fail","reason":具体原因码}
        """
        # 处理这个错�??
        if name in self.List:
            return {"result": "fail", "reason": Constants.ERROR_TYPE_REDEFINITION}
        self.List[name] = {"Members": member_list, "Type": ir.LiteralStructType(type_list)}
        return {"result": "success"}

    def GetMemberType(self, Name, Member):
        '''
        描述：获取成员类�?
        参数：结构体名称，结构体成员�?
        返回：类�?,不存在返回None
        '''
        if Name not in self.List:
            return None
        StructItem = self.List[Name]
        TheIndex = StructItem["Members"].index(Member)
        TheType = StructItem["Type"].elements[TheIndex]
        return TheType

    def GetMemberIndex(self, Name, Member):
        '''
        描述：获取成员编�?
        参数：结构体名称，结构体成员�?
        返回：类�?,不存在返回None
        '''
        if Name not in self.List:
            return None
        StructItem = self.List[Name]["Members"]
        TheIndex = StructItem.index(Member)
        return TheIndex



