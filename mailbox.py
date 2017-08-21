import smtplib
from email.mime.text import MIMEText


msg = MIMEText('mail conet here ,sogoodnow sent')
msg['Subject'] = 'email alert'
msg['From'] = 'sogoodnow@sina.com'
msg['To'] = 'qiugc@inf-technology.com'


s = smtplib.SMTP('smtp.sina.com')
s.login('sogoodnow@sina.com', 'qiuguochang2016')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
