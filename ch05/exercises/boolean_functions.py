def percentage_to_letter(score=0):
    grade = "A"
    if 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    elif score < 60:
        grade = "F"
    return grade
    
def is_passing(letter=None):
    if letter in "ABC":
        return True
    else:
        return False

def main():
    num = int(input("enter your score:"))
    let = percentage_to_letter(num)
    percentage_to_letter(num)
    print(num, let, is_passing(let))
    
main()