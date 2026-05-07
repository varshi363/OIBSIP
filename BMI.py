def main():
    body_load=float(input("Enter your weight in kilograms : "))
    if body_load<=0:
        print("Weight should be in positive values.")
        return

    body_stature=float(input("Enter the height in meters : "))
    if body_stature == 0:
        print("Height should be in positive values.")
        return

    body_stature = body_stature * body_stature
    bmi = body_load / body_stature

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
      print("Underweight")
    elif bmi < 25:
      print("Normal")
    elif bmi < 30:
      print("Overweight")
    elif bmi < 35:
      print("Obesity Class 1")
    elif bmi < 40:
      print("Obesity Class 2")
    else:
      print("Morbid Obesity")

if __name__ == "__main__":
    main()
