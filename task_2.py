def personal_info(**kwargs):
    return ' '.join(kwargs.values())
print(personal_info(name=input("enter name: "), surname=input("enter suname: ")))




