def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
        except KeyError:
            return "Enter the user name correctly!"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] # перевірка чи існує значення, яка видасть keyerror якщо ні, бо інакше строка нижче просто створює контакт без виклику помилки...
    # хоча і якщо чесно дивно викликати тут помилку "введи ім'я коректно", коли такого контакту зовсім немає. За прикладом на платформі для мене, поки що,
    # обробка помилок через декоратори виглядає вкрай негнучкою :(
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

def list_contacts(contacts):
    if not contacts:
        return "The contactbook is empty."
    return "Contacts:" + "".join(f"\n{name}: {phone}" for name,phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Please enter your command: ")
        command, *args = parse_input(user_input)

        match command: # Помітив, що у прикладі робиться через if-else, але вже почав через match..
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(list_contacts(contacts))
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
