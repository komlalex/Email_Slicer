# Collect email
# split the email using the @, save the first part as username
# the second part is gonna be saved as domain
# split the second at .

def main(): 
    print("Welcome to the email slicer.")
    print("")

    email_input = input("Input your email address:")

    (username, domain) = email_input.split("@")

    (domain, extension) = domain.split(".")

    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")

while True:
    main()      