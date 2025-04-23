class laptop:
    def __init__(self,Brand,Colour,Ram,Rom,Speed):
        print("instance created")
        self.brand=Brand
        self.colour=Colour
        self.ram=Ram
        self.rom=Rom
        self.speed=Speed
    def about(self):
        return f"this is a {self.brand} laptop colour of {self.colour} with {self.ram} ram & rom  of {self.rom},{self.speed}speed"
laptop1=laptop("Dell","silver","8GB - 64GB","256GB-2TB SSD","Up to 5GHz (Intel Core i9)")
print(laptop1.about())
laptop2=laptop("HP","gold","8GB - 32GB"," 256GB - 1TB SSD"," Up to 4.7GHz (Intel Core i9)")
print(laptop2.about())
laptop3=laptop("lenova","black","8GB - 64GB","256GB - 2TB SSD","Up to 5GHz (Intel Core i9)")
print(laptop3.about())
laptop4=laptop("apple","red"," 8GB - 64GB","256GB - 8TB SSD","Up to 5.2GHz (Intel Core i9)")
print(laptop4.about())
laptop5=laptop("asus","GREEN","8GB - 64GB","1TB SSD","15.6-inch FHD (1920x1080)")
print(laptop5.about())
laptop6=laptop("microsoft","BLUE","8GB - 64GB","256GB - 2TB SSD","Up to 5GHz (Intel Core i9)")
print(laptop6.about())
laptop7=laptop("razer","pink","8GB - 64GB","256GB - 2TB SSD","Up to 5GHz (Intel Core i9)")
print(laptop7.about())
laptop8=laptop("google","yellow","8GB - 64GB","256GB - 2TB SSD","Up to 5GHz (Intel Core i9)")
print(laptop8.about())
laptop9=laptop("acer","maroon","8GB - 64GB","256GB - 2TB SSD","Up to 5GHz (Intel Core i9)")
print(laptop9.about())
laptop10=laptop("MSI","white","8GB - 64GB","256GB - 2TB SSD","Up to 5GHz (Intel Core i9)")
print(laptop10.about())