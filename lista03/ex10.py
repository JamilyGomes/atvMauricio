class Temp:
    def celsius_pFahrenheit(self,temp_C):
        self.temp_C=temp_C

        far=self.temp_C*(9/5)+32
        return far
    
x=Temp()

c= float(input("dgt a temperatura em Celsius: "))
far= x.celsius_pFahrenheit(c)
print("temperatura em fahrenheit: " + str(far))
