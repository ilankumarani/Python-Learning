# str.format() =     optional method that gives users
#                   more control when displaying output

def string_format():
    animal = "cow"
    item = "moon"

    # print("The "+animal+" jumped over the "+item)
    # print("The {} jumped over the {}".format(animal,item))
    # print("The {1} jumped over the {1}".format(animal, item))  #positional argument
    # print("The {animal} jumped over the {animal}".format(animal="cow", item="moon"))  #keyword ...

    text = "The {} jumped over the {}"
    print(text.format(animal, item))


def string_format_texting():
    name = "Bro"

    print("Hello, my name is {}".format(name))
    print("Hello, my name is {name:10}. Nice to meet you".format(name))
    print("Hello, my name is {:<10}. Nice to meet you".format(name))
    print("Hello, my name is {:>10}. Nice to meet you".format(name))
    print("Hello, my name is {:^10}. Nice to meet you".format(name))

def string_format_number():
    number = 1000

    print("The number pi is {:.3f}".format(number))
    print("The number is {:,}".format(number))
    print("The number is {:b}".format(number))
    print("The number is {:o}".format(number))
    print("The number is {:X}".format(number))
    print("The number is {:E}".format(number))

def main()->None:
    string_format()
    string_format_number()
    string_format_texting()

if __name__ == "__main__":
    main()

