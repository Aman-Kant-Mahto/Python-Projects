import smtplib
my_mail="aravrider3@gmail.com"
passcode="hibjfgxdybtatmuz"

connection= smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail,password=passcode)

mail_content=" Subject: trip on this weekend: \n\n hey aao kbhi haweli pe"

try:
    connection.sendmail(from_addr=my_mail, to_addrs="amanmahto669@gmail.com", msg=mail_content)

except Exception as e:
    print("something went wrong",e)

connection.close()
