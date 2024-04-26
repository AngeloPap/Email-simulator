# --- OOP Email Simulator --- #
import time
'''
This program is an email simulator that allows you to check your inbox,
check your spam, move emails between them, mark mails as read and delete
any emails from either your main inbox or your spam inbox.
'''

# --- Email Class --- #


class Email:
    def __init__(self, Email_address, subject_line, email_content):
        self.email_address = Email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
inbox = []
spam = []


# --- Functions --- #
def populate_inbox(Email_address, subject_line, email_content):
    Email_address = Email(Email_address, subject_line, email_content)
    inbox.append(Email_address)


def list_emails():
    count = -1
    print("\nInbox:")
    print("---------------------")
    for email in inbox:
        count += 1
        print(count, email.subject_line)


def read_email(index):
    email = inbox[index]
    print(f"From: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print("---------")
    print(f"{email.email_content}")
    email.has_been_read = True


def list_emails_in_spam():
    count = -1
    print("\nSpam:")
    print("---------------------")
    for email in spam:
        count += 1
        print(count, email.subject_line)


def read_spam_email(index):
    email = spam[index]
    print(f"From: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print("---------")
    print(f"{email.email_content}")
    email.has_been_read = True


# --- Email Program --- #
'''
Populates the inbox with 3 examples.
'''
populate_inbox("clarkkent@gmail.com", "Advisor meeting for dissertation",
               "Hi there,\nCould we set up a meeting.\nThanks,\nKent")
populate_inbox("anakin@gmail.com", "Returning library book",
               "Hi there,\nYou have a book overdue. Please could you return it"
               "at your earliest convenience.\n Kind regards,\nAnakin")
populate_inbox("ruby@gmail.com", "Order return",
               "Hi there,\nI'd like to return my recent order."
               "\nThanks,\nRuby")

menu = True

while menu is True:

    user_choice = int(input('''\nWould you like to:
---------------------
1. Read an email
2. View unread emails
3. Quit application

Enter selection: '''))

    if user_choice == 1:
        '''
        Section to choose either normal inbox or spam inbox.
        '''
        normal_or_spam = True
        while normal_or_spam is True:
            which_one = int(input('''\nWould you like to:
---------------------
1. Check your inbox
2. Check your Spam

Enter selection: '''))
            if which_one == 1:
                list_emails()
                choice = int(input('''\nWhich email would you like to read?
Type the number it is in the list or if there are no emails type -1 to return
to the main menu: '''))
                print("---------")
                if choice == -1:
                    normal_or_spam = False
                    continue
                read_email(choice)
                chosen_email = inbox[choice]

                menu_for_inbox = True
                while menu_for_inbox is True:
                    choice_for_inbox = int(input('''\nWould you like to:
---------------------
1. Mark as read
2. Move email to spam
3. Delete email

Enter selection: '''))

                    if choice_for_inbox == 1:
                        print(f"\nEmail from {chosen_email.email_address}"
                              f" was marked as read.")
                        time.sleep(1)
                        print("\nLoading main menu...")
                        time.sleep(1)
                        print("\n")
                        menu_for_inbox = False
                        normal_or_spam = False
                    elif choice_for_inbox == 2:
                        inbox.pop(choice)
                        spam.append(chosen_email)
                        time.sleep(1)
                        print(f"\nEmail from {chosen_email.email_address} was"
                            f" moved to spam.\nThis email will still be marked" 
                            f" as read.")
                        time.sleep(1)
                        print("\n")
                        un_read_email = True
                        while un_read_email is True:
                            un_read = int(input('''
Would you like to un mark this from read?
Please choose:
---------------------
1.Yes
2.No\n'''))
                            if un_read == 1:
                                chosen_email.has_been_read = False
                                time.sleep(1)
                                print(f"Email from"
                                      f" {chosen_email.email_address}"
                                      f" is no longer marked as read.")
                                time.sleep(1)
                                print("\n")
                                un_read_email = False
                            elif un_read == 2:
                                time.sleep(1)
                                print(f"Email from"
                                      f" {chosen_email.email_address}"
                                      f" has been left as read.")
                                time.sleep(1)
                                print("\n")
                                un_read_email = False
                            else:
                                print("Sorry please choose a valid option.")
                                print("Either 1 for yes or 2 for no.")
                        time.sleep(1)
                        print("\nLoading main menu...")
                        time.sleep(1)
                        print("\n")
                        menu_for_inbox = False
                        normal_or_spam = False
                    else:
                        inbox.pop(choice)
                        print(f"\nEmail from "
                            f"{chosen_email.email_address} was deleted.")
                        time.sleep(1)
                        print("\nLoading main menu...")
                        time.sleep(1)
                        print("\n")
                        menu_for_inbox = False
                        normal_or_spam = False
            elif which_one == 2:
                list_emails_in_spam()
                choice = int(input('''\nWhich email would you like to read?
Type the number it is in the list or if there are no emails type -1 to return
to the main menu: '''))
                print("---------")
                if choice == -1:
                    normal_or_spam = False
                    continue
                read_spam_email(choice)
                chosen_email = spam[choice]

                menu_for_spam = True
                while menu_for_spam is True:
                    choice_for_spam = int(input('''\nWould you like to:
---------------------
1. Mark as read
2. Move to main inbox
3. Delete email

Enter selection: '''))

                    if choice_for_spam == 1:
                        print(f"\nEmail from {chosen_email.email_address}"
                            f" was marked as read.")
                        time.sleep(1)
                        print("\nLoading main menu...")
                        time.sleep(1)
                        print("\n")
                        menu_for_spam = False
                    elif choice_for_spam == 2:
                        spam.pop(choice)
                        inbox.append(chosen_email)
                        time.sleep(1)
                        print(f"\nEmail from {chosen_email.email_address}"
                            f" was moved to the main inbox. This email will"
                            f" still be marked as read.")
                        time.sleep(1)
                        print("\n")
                        un_read_email = True
                        while un_read_email is True:
                            un_read = int(input('''
Would you like to un-read this?
Please choose:
---------------------
1.Yes
2.No\n'''))
                            if un_read == 1:
                                chosen_email.has_been_read = False
                                time.sleep(1)
                                print(f"Email from"
                                      f" {chosen_email.email_address}"
                                      f"is no longer marked as read.")
                                un_read_email = False
                            elif un_read == 2:
                                time.sleep(1)
                                print(f"Email from"
                                      f" {chosen_email.email_address}"
                                      f"has been left as read.")
                                un_read_email = False
                            else:
                                print("Sorry please choose a valid option.")
                                print("Either 1 for yes or 2 for no.")
                        time.sleep(1)
                        print("\nLoading main menu...")
                        time.sleep(1)
                        print("\n")
                        menu_for_spam = False
                        normal_or_spam = False
                    else:
                        inbox.pop(choice)
                        print(f"\nEmail from "
                              f"{chosen_email.email_address} was deleted.")
                        time.sleep(1)
                        print("\nLoading main menu...")
                        time.sleep(1)
                        print("\n")
                        menu_for_spam = False

    elif user_choice == 2:
        print(f"\nUnread emails:")
        print("---------------------")
        for email in inbox:
            if email.has_been_read is False:
                print(f"Subject: {email.subject_line}")
        time.sleep(1)
        print("\nLoading main menu...")
        time.sleep(1)

    elif user_choice == 3:
        print("Application closing...")
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        menu = False

    else:
        print("Oops - incorrect input, please try again.")
