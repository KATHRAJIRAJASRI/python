class laptop:
    def __init__(self,Brand,Model,Processor,Ram,Storage,Display):
        print("instance created")
        self.brand=Brand
        self.model=Model
        self.processor=Processor
        self.ram=Ram
        self.storage=Storage
        self.display=Display
        
    def about(self):
        return f"this is a {self.brand} laptop model of {self.model} with {self.processor} processor of {self.ram} ram with storage of {self.storage} with display size {self.display} "
laptop1=laptop("Dell XPS 13","Intel Core i7-1260P","16GB DDR5","512GB SSD","13.4-inch FHD+ (1920x1200)","Intel Iris Xe")
laptop2=laptop("HP","Envy x360","AMD Ryzen 7 5800U","16GB DDR4","1TB SSD","15.6-inch FHD (1920x1080)")
print(laptop1.about())
print(laptop2.about())
