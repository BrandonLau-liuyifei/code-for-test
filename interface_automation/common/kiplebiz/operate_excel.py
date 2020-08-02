import xlrd

class readExcel(object):
    def __init__(self,path):
        self.path = path

    @property
    def getSheet(self):
        #获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        return sheet

    @property
    def getRows(self):
        #获取行数
        row = self.getSheet.nrows
        return row

    @property
    def getCols(self):
        #获取列数
        col = self.getSheet.ncols
        return col

    #以下是分别获取每一列的数值
    @property
    def getId(self):
        TestId = []
        for i in range(1,self.getRows):
            TestId.append(self.getSheet.cell_value(i,0))
        return TestId

    @property
    def getName(self):
        TestName = []
        for i in range(1, self.getRows):
            TestName.append(self.getSheet.cell_value(i, 1))
        return TestName

    @property
    def getScenario (self):
        TestName = []
        for i in range(1, self.getRows):
            TestName.append(self.getSheet.cell_value(i, 2))
        return TestName

    @property
    def getUrl(self):
        TestUrl = []
        for i in range(1, self.getRows):
            TestUrl.append(self.getSheet.cell_value(i, 3))
        return TestUrl

    @property
    def getMethod(self):
        TestMethod = []
        for i in range(1, self.getRows):
            TestMethod.append(self.getSheet.cell_value(i, 4))
        return TestMethod

    @property
    def getHeaders(self):
        TestHeaders = []
        for i in range(1, self.getRows):
            TestHeaders.append(self.getSheet.cell_value(i, 5))
        return TestHeaders

    @property
    def getContent_type(self):
        TestContent_type = []
        for i in range(1, self.getRows):
            TestContent_type.append(self.getSheet.cell_value(i, 6))
        return TestContent_type

    @property
    def getParams(self):
        TestParams = []
        for i in range(1, self.getRows):
            TestParams.append(self.getSheet.cell_value(i, 7))
        return TestParams

    @property
    def getExpect(self):
        TestExpect = []
        for i in range(1, self.getRows):
            TestExpect.append(self.getSheet.cell_value(i, 8))
        return TestExpect

    @property
    def getCode(self):
        TestCode = []
        for i in range(1, self.getRows):
            TestCode.append(self.getSheet.cell_value(i, 9))
        return TestCode

