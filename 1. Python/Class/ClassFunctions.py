class ClassFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        fields = ["Machine Learning", "Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for field in fields:
                print(field)

    def oddOrEven():
            value = int(input("Enter a number: "))
            if(value % 2 == 1):
                print(value, "is odd number")
            else:
                print(value, "is Even number")

    def percentage():
            sub1 = int(input("Subject1= "))
            sub2 = int(input("Subject2= "))
            sub3 = int(input("Subject3= "))
            sub4 = int(input("Subject4= "))
            sub5 = int(input("Subject5= "))
            total = sub1 + sub2 + sub3 + sub4 + sub5
            print("Total: ", total)
            percentage = ((total/500)*100)
            print("Percentage: ", percentage)

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


    def triangle():
            height = int(input("Height: "))
            breadth = int(input("Breadth: "))

            print("Area formula: Breadth*Height*0.5")

            area = breadth * height* 0.5

            print("Area of Triangle is:", area)

            h1 = int(input("Height1= "))
            h2 = int(input("Height2= "))

            breadth1 = int(input("Breadth= "))

            print("perimeter formula: Height1+ Height2 + Breadth")

            perimeter = h1 + h2 + breadth1

            print("Perimeter of Triangle: ", perimeter)