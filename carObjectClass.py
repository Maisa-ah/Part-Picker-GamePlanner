class carobject:
    num_of_cars = 0

    def __init__(self):
        carobject.num_of_cars += 1

#info wrapper is the web element that encapsultes the details of the vehicle like color vin etc
    @property
    def InfoWrapper(self, InfoWrapper):
       return self.InfoWrapper
    
    @InfoWrapper.setter
    def InfoWrapper(self, InfoWrapper):
        self.InfoWrapper = InfoWrapper

    @property
    def Color(self, color):
       return self.color
    @Color.setter
    def Color(self, color):
        self.color = color

    @property
    def Vin(self, vin):
        return self.vin
    @Vin.setter
    def Vin(self, vin):
        self.vin = vin

    @property
    def Section(self, section):
        return self.section
    @Section.setter
    def Section(self, section):
        self.section = section

    @property
    def Row(self, row):
        return self.row
    @Row.setter
    def Row(self, row):
        self.row = row

    @property
    def Space(self, space):
        return self.space
    @Space.setter
    def Space(self, space):
        self.space = space

    @property
    def StockNum(self, stocknum):
        return self.stocknum
    @StockNum.setter
    def StockNum(self, stocknum):
        self.stocknum = stocknum

    @property
    def AvalabilityDate(self, avalabilitydate):
        return self.avalabilitydate
    @AvalabilityDate.setter
    def AvalabilityDate(self, avalabilitydate):
        self.avalabilitydate = avalabilitydate


