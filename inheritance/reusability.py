'''Inheritance (Reusable Code): Here we will use the base class and reuse the initialized variable in child class '''
# "Reusable Code In Inheritance"
import test


class Phone:
    #  Initialising the base class
    def __init__(self, body, thickness, battery, camera, processor):
        self.body = body
        self.thickness = thickness
        self.battery = battery
        self.camera = camera
        self.processor = processor


'''Syntax for reusing the code (from parent to child): 
    {parent-class}.{method-name(variable)} [variables of that method]'''


class SamsungS10(Phone):  # Calling the base class instance variable
    def __init__(self, body, thickness, battery, camera, processor, Extra):
        Phone.__init__(self, body, thickness, battery, camera, processor)
        self.usp = Extra  # Extra variable for this class

    def dispS10(self):
        # Printing the class name
        print(__class__.__name__)
        print(f"Body: {self.body}")
        print(f"Thickness: {self.thickness}")
        print(f"Battery: {self.battery}")
        print(f'Camera: {self.camera}')
        print(f'Processor: {self.processor}')
        print(f'USP: {self.usp}')


class SamsungS11(Phone):
    def __init__(self, body, thickness, battery, camera, processor, Extra):
        Phone.__init__(self, body, thickness, battery, camera, processor)
        self.usp = Extra

    def dispS11(self):
        print(__class__.__name__)
        print(f"Body: {self.body}")
        print(f"Thickness: {self.thickness}")
        print(f"Battery: {self.battery}")
        print(f'Camera: {self.camera}')
        print(f'Processor: {self.processor}')
        print(f'USP: {self.usp}')


s10 = SamsungS10('Light', '1.3mm', "4000Mah", '12MP',
                 "Exynos1234", 'SHINY GLASS BACK')
s10.dispS10()
print('********************************************************************************')
s11 = SamsungS11('Not So Heavy', '3.4mm', '5000Mah',
                 '30MP', "Exynos5678", "ULTRA ZOOM MODE")
s11.dispS11()
