import imaplib
import email
from bs4 import BeautifulSoup
import os
import mimetypes
username = 'testuser.dollar@gmail.com'
password = 'Sanjana1!'

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

mail.select("inbox")

result, data = mail.uid('search', None, "ALL")
inbox_item_list = data[0].split()
global key_
key_ = 0
for item in inbox_item_list:

    result2, email_data = mail.uid("fetch", item, "RFC822")
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    print(dir(email_message))
    to_ = email_message['To']
    from_ = email_message['From']
    subject_ = email_message['Subject']
    date_ = email_message['date']
    counter = 1
    for part in email_message.walk():
        if part.get_content_type() == "multipart":
            continue
        content_type = part.get_content_type()
        filename = part.get_filename()
        if not filename:
            ext = mimetypes.guess_extension(content_type)
            if not ext:
                ext = '.bin'
            filename = 'msg-part-%08d%s' % (counter, ext)
        counter += 1
    save_path = os.path.join(os.getcwd(), "emails", bin(key_))
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    with open(os.path.join(save_path, filename), 'wb') as fp:
        fp.write(part.get_payload(decode=True))
    key_ += 1
