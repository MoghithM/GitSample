import re
email_pattern=r"[a-zA-Z0-9._%+-]"
text="Please contact us at example@example.com"
match=re.search(email_pattern,text)
if match:
    print("Email found:",match.group())