# List of popular email providers in South Africa
email_providers = ["Gmail", "Yahoo", "Outlook"]

# Function to generate email address
def generate_email():
    # Get user's name
    name = input("Enter your name: ")

    # Ask for surname (optional)
    surname = input("Enter your surname (optional): ")

    # Display email provider options
    print("Choose an email provider:")
    for i, provider in enumerate(email_providers, start=1):
        print(f"{i}. {provider}")

    # Get user's choice
    provider_choice = int(input("Enter the number of your chosen email provider: "))

    # Validate user's choice
    if 1 <= provider_choice <= len(email_providers):
        chosen_provider = email_providers[provider_choice - 1]

        # Generate email address
        if surname:
            email_address = f"{name.lower()}.{surname.lower()}@{chosen_provider.lower()}.com"
        else:
            email_address = f"{name.lower()}@{chosen_provider.lower()}.com"

        # Display the generated email address
        print("Your generated email address is:", email_address)

    else:
        print("Invalid choice. Please enter a valid number.")

# Call the function to generate an email address
generate_email()
