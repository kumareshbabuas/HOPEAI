class ElegibilityForMarriage():    
    def Elegible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        if(gender == "Male" and age >= 21):
            eligible = "Your ELIGIBLE"
        elif(gender == "Female" and age >=18):
            eligible = "Your ELIGIBLE"
        else:
            eligible = "NOT ELIGIBLE"
        return eligible
        
        