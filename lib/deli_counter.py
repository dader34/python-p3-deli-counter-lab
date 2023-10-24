# katz_deli = ["arthur","samuel"]

def line(katz_deli):
    if(not katz_deli):
        print("The line is currently empty.")
    else:
        final_str = "The line is currently:"
        for person in katz_deli:
            final_str += f" {katz_deli.index(person) + 1}. {person}"
        print(final_str)
    


def take_a_number(katz_deli,name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        del katz_deli[0]
