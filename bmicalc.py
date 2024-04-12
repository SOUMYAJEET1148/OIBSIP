height = float(input("Enter Height In Inches: "))
weight = float(input("Enter Weight In Kg: "))
def BMI (height, weight):
    bmi = weight/(height**2) * 703
    if (bmi < 6):
        return 'severly underweight', bmi

    elif (bmi >=6 and bmi < 7.5):

        return 'underweight', bmi

    elif (bmi >= 7.5 and bmi < 12.5):

        return 'wow! You Are Healthy', bmi

    elif (bmi>=12.5 and bmi < 25.0):

        return 'overweight', bmi

    elif (bmi >= 25.0):

        return 'obese', bmi

quote, bmi = BMI(height,weight)
print('your bmi is: {} and you are: {}' .format(bmi, quote))