import pandas as pd

class working_excel():
    def __init__(self, name,sheetname):
        self._name = name
        self._sheetname = sheetname

    def reading_excel(self):
        dfs = pd.read_excel(self._name,sheetname=self._sheetname)
        return dfs


if __name__ == '__main__':
    name = 'table.xls'
    sheetname= '16tbl02'
    a = working_excel(name,sheetname)
    dfs = a.reading_excel()
    print(type(dfs))

