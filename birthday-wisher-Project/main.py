import datetime as dt
import random
import os
import shutil
import smtplib
import pandas

today_tuple = (dt.datetime.now().month,dt.datetime.now().day)

data = pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]',birthday_person['name'])

    my_email = 'sam.sahyouni@gmail.com'
    password = 'vmqi akxk zmik hnyo'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f'{birthday_person["email"]}',
            msg=f'Subject:Happy Birthday {birthday_person["name"]}\n\n{contents}'
        )


# with open('birthdays.csv') as bday_file:
#     bday_content = bday_file.readlines()
#     bday_names = [line.split(',', 1)[0] for line in bday_content if month in line and day in line]
#     if not bday_names:
#         print('No birthdays today!')
#     # print(bday_names)


# pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# for name in bday_names:
#     random_letter = random.choice(os.listdir('letter_templates'))
#     shutil.copyfile(f'letter_templates/{random_letter}', f'coded bday letters/bday_letter.txt')
#     old = '[NAME]'
#     new = name
#     with open('coded bday letters/bday_letter.txt') as bday_letter:
#         letter_contents = bday_letter.read()
#         new_letter = letter_contents.replace(old, new)
#         with open('coded bday letters/bday_letter.txt', 'w') as completed_letter:
#             completed_letter.write(new_letter)
#     with open('coded bday letters/bday_letter.txt') as new_bday_letter:
#         birthday_letter = new_bday_letter.read()
#     # email birthday message to birthday ppl
#         my_email = 'sam.sahyouni@gmail.com'
#         password = 'vmqi akxk zmik hnyo'
#         with smtplib.SMTP('smtp.gmail.com') as connection:
#             connection.starttls()
#             connection.login(user=my_email,password=password)
#             connection.sendmail(
#                 from_addr=my_email,
#                 to_addrs='sam@vineyardaugusta.org',
#                 msg=f'Subject: Happy Birthday {name}\n\n{birthday_letter}'
#             )
#
#     print(f'email to {name} sent')



# 4. Send the letter generated in step 3 to that person's email address.




