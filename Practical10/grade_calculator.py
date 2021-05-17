#function
def grade_calculator(name,code,poster,exam):
    grade=code*0.4+poster*0.3+exam*0.3
    return print(name+","+str(grade))

#example
test=grade_calculator("Joy",85,86,74)

