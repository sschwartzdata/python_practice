# importing packages
import os
import re


def phone_number_search(search_path):
    for folders, sub_folders, files in os.walk(search_path):

        for file in files:
            file_name = os.path.join(folders, file)
            opened_file = open(file_name, 'r')
            text = opened_file.read()
            # Phone number search by format
            phone = re.search(r'\d{3}-\d{3}-\d{4}|(\d{3})\d{3}-\d{4}', text)
            if phone is None:
                pass
            else:
                print(f'The phone number is located in {file_name}')
                print(f' the phone number is {phone}')
            opened_file.close()


def main():
    print('The phone number formats searched for are '
          '(###)###-### and ###-###-####')
    path = input('What is the directory that you want '
                 'to locate phone numbers in?')
    phone_number_search(path)
    input('Press enter to exit')
    return 0


if __name__ == '__main__':
    main()
