from pyscript import display, document
def generate_message(e):

    Name = document.getElementById("Name").value
    Age = document.getElementById("Age").value
    School = document.getElementById("School").value
    student_profile = f"""
    👨‍🎓 Student Profile
    Name   : \"{name}\"
    Age    :\t{age}
    School : {school}
    {name} is currently {age} years old and is currently studying at {school}.
    """





