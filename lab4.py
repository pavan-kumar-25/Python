#Write a Python program to implement the object-oriented concepts of multiple, Multilevel and Hierarchical Inheritances using your domain applications.

#Single inheritance

class Place:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")


class TouristSpot(Place):
    def __init__(self, name, location, highlights):
        super().__init__(name, location)
        self.highlights = highlights

    def display_info(self):
        super().display_info()
        print("Highlights:", ", ".join(self.highlights))


# Create instances of the classes
tourist_spot = TouristSpot("Eiffel Tower", "Paris, France", ["Iconic landmark", "Panoramic view"])


# Display information
print("Tourist Spot Information:")
tourist_spot.display_info()



#multiple inheritance

class Location:  
    country = ""  
    def country(self):  
        print(self.country)  
   
class Highlight:  
    highlight = ""  
    def highlight(self):  
        print(self.highlight)  
  
class TouristSpot(Location, Highlight):  
    def combined_fields(self):  
        print ("The country name is", self.country, "and the highlight of this country is" , self.highlight)  
  
tour = TouristSpot()  
tour.country = "India"  
tour.highlight = "Culture"  
tour.combined_fields()  



#Multilevel inheritance

class Place: #place, name
    def __init__(self,name):
        self.name=name
    
class Touristspot(Place):  #TouristSpot, highlights
    def __init__(self,highlights,name):
        self.highlights=highlights

        Place.__init__(self,name)

class Hotel(Touristspot):  #hotel, facilities
    def __init__(self,facilities,highlights,name):
        self.facilities=facilities

        Touristspot.__init__(self,highlights,name)      
  
class TouristPackage(Hotel):  #TouristPackage, duration
    def __init__(self,facilities,highlights,name):  
        Hotel.__init__(self,facilities,highlights,name)

    def combined_print(self):
        print ( "The best tourist place is ", self.facilities , ", and the package price is ", self.highlights , " with good" , self.name)  

     
tour = TouristPackage("Maldives",50000,"resorts")  
tour.combined_print() 
