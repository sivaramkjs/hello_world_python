help_commands = ["start - to start the car", "stop - to stop the car", "quit - to exit"]
is_started = False
is_stopped= False

while True:
    user_command = input("> ")
    user_command = user_command.lower()
    if user_command == "help":
        for help_command in help_commands:
            print(help_command)
    elif user_command == "start":
        print("Car already started!") if is_started else print("Car started...Ready to go!")
        is_started = True
        is_stopped = False
    elif user_command == "stop":
        print("Car already stopped!") if is_stopped else print("Car stopped")
        is_started = False
        is_stopped = True
    elif user_command == "quit":
        break
    else:
        print("I don't understand that...")