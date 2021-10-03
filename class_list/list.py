class super_list(list):

    def __init__(self):
        self.webelement = []
        super().__init__()

i = super_list()
i.webelement.append('wefwef')
print(i.webelement)






