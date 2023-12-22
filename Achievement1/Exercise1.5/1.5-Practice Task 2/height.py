class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    def __sub__(self, other):
        h1_in_inches = self.feet * 12 + self.inches
        h2_in_inches = other.feet * 12 + other.inches

        output_feet = (h1_in_inches - h2_in_inches) // 12
        output_inches = (h1_in_inches - h2_in_inches) % 12

        return Height(output_feet, output_inches)

    def __str__(self):
        return "%d feet %d inches" % (self.feet, self.inches)
    
    def __gt__(self, other):
        h1_in_inches = self.feet * 12 + self.inches
        h2_in_inches = other.feet * 12 + other.inches

        return h1_in_inches > h2_in_inches
    
    def __ge__(self, other):
        h1_in_inches = self.feet * 12 + self.inches
        h2_in_inches = other.feet * 12 + other.inches

        return h1_in_inches >= h2_in_inches
    
    def __ne__(self, other):
        h1_in_inches = self.feet * 12 + self.inches
        h2_in_inches = other.feet * 12 + other.inches

        return h1_in_inches != h2_in_inches
    
h1 = Height(5, 10)
h2 = Height(3, 11)

height_dif = h1 - h2

print("Height difference is: ", height_dif)

print(Height(4, 6) > Height(4, 8))
print(Height(4, 5) >= Height(4, 5))
print(Height(5, 9) != Height(5, 10))