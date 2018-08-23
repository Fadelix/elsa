
# Elsa.py
# 
# mfadly.n@gmail.com
#
# Elsa.py is an IPS/IDS alert system, it work with Mod Security and Owasp CRS
#
# ###########################################################################

import smtplib
import datetime

def main():

# Constant variable
# replace this configuration with your own environment
        f_log = "/var/log/httpd/modsec_audit.log"
        email_from = "emailfrom@email.com"
        email_to = "emailto@ email.com"
        smtp_addr = 'smtp.office365.com'
        smtp_pwd = "password"

        f=open(f_log, "r")
        contents =f.read()
        if contents == '':
                print "konten kosong"
        else:
                #print contents

                from email.MIMEMultipart import MIMEMultipart
                from email.MIMEText import MIMEText
                from email.MIMEBase import MIMEBase
                from email import encoders

                fromaddr = email_from
                toaddr = email_to

                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg['Subject'] = "Electra Security Alarm System (ELSA) v1"

                body = "Hallo sysadmin electra, mas faris & mbak ennitan, saat ini sistem kami menangkap aktivitas yang mencurigakan diserver electra nih, coba dicek lognya dong (This Email Alert was generated automatically with Elsa.py By Electra Techteam-fdlx)"
                msg.attach(MIMEText(body, 'plain'))

                t = datetime.datetime.now()
                fil = t.strftime('%H-%M_%Y-%m-%d')

                filename = fil + "_activity.log"
                attachment = open(f_log, "rb")

                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                msg.attach(part)

                server = smtplib.SMTP(smtp_addr, 587)
                server.starttls()
                server.login(fromaddr, smtp_pwd)
                text = msg.as_string()
                server.sendmail(fromaddr, toaddr, text)
                server.quit()

                k=open(f_log, "w+")
                k.write("")
                k.close()
if __name__== "__main__":
  main()

