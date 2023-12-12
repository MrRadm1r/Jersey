import openpyxl

class EmptyCellError(ValueError):
    pass

class OptionError(AttributeError):
    pass

class Plot:
    def __init__(self, path):
        self.workbook = openpyxl.load_workbook(path)
        self.sheet = self.workbook.active
        self.column = "A"
        self.row = 1
        self.dialog = True
        self.cell = None
        self.progressing()

    def progressing(self):
        while self.dialog:
            self.cell_update()
            if self.cell[0] == "/":
                if self.cell[1] == ">":
                    variants = {}
                    for i in self.cell[2:].split():
                        self.is_empty_cell(i)
                        variants[self.sheet[i].value[1:]] = i
                        print("Выбор:", self.sheet[i].value)
                    print(variants)
                    choise = input()
                    if variants.get(choise, False):
                        self.separate(variants[choise])
                    else:
                        raise OptionError(f"Не найдено опции выбора \"{choise}\" среди {list(variants.keys())}")
                    # self.cell_update()
                elif self.cell[1] == "~":
                    self.separate(self.cell[2:])
                elif self.cell[1] == "!":
                    self.dialog = False
                else:
                    print("You:", self.cell)
                    self.row += 1

            else:
                print("Speaker:", self.cell)
                self.row += 1
        else:
            self.close()

    def separate(self, link):
        i = 0
        while link[i].isalpha():
            i += 1
        self.column = link[:i]
        self.row = int(link[i:])

    def call(self, link):
        self.is_empty_cell(link)
        cell_value = self.sheet[link].value
        return cell_value

    def cell_update(self):
        link = self.column + str(self.row)
        
        self.cell = self.sheet[link].value
        self.is_empty_cell(link)

    def is_empty_cell(self, link):
        if not self.sheet[link].value:
            raise EmptyCellError(f"Ячейка {link} пуста")


    def close(self):
        self.workbook.close()



if __name__ == "__main__":
    plot = Plot("plot.xlsx")
    plot.close()
    # print(plot.call("A1"))
