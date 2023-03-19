from dbhelper import DBHelper
def main():
    db = DBHelper()
    while True:
        print("\n-----welcome-----")
        print()
        print("PRESS 1 to insert new user"
              "\nPRESS 2 to display all user"
              "\nPRESS 3 to delete user"
              "\nPRESS 4 to update user"
              "\nPRESS 5 to exit\n")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                userid = int(input("Enter the userId: "))
                username = str(input("Enter the username: "))
                phone = str(input("Enter the phone number: "))
                db.insert_user(userid, username, phone)
            elif choice == 2:
                db.fetch_all()
                #display user
            elif choice == 3:
                userid = int(input("Enter the userid: "))
                db.delete_user(userid)
            elif choice == 4:
                userid = int(input("Enter the user id: "))
                updated_username = str(input("Enter the updated username: "))
                updated_phonenumber = str(input("Enter the updated phone number: "))
                db.update(userid, updated_username, updated_phonenumber)
                #update user
            elif choice == 5:
                break
            else:
                print("Invalid input try again.")

        except Exception as e:
            print(e)
            print("Invalid Details: Try again")

if __name__ == "__main__":
    main()







