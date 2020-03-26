import gspread

class Nandi():
    def get_Name_and_Id(self, sheet):
        names = []
        d = {}
        values_list = sheet.col_values(1)
        values_list.remove(values_list[0])
        n = 0
        key = ''
        val = ''
        for value in values_list:
            if n % 6 == 0:
                #print(value)
                #names.append(value)
                key = value
                val = values_list[n+1]
                d[key] = val
            n = n+1
        return d
    def __init__(self, sheet):
        for key, value in self.get_Name_and_Id(sheet).items():
            print(key, ':', value)
