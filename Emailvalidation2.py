def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password too short! Must be at least 8 characters.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    if not any(char in "@#$%&!" for char in password):
        raise ValueError("Password must contain at least one special character (@, #, $, %, &, !).")
    print("✅ Password is valid.")

def validate_url(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError("URL must start with 'http://' or 'https://'.")
    if '.' not in url:
        raise ValueError("URL must contain a dot ('.') like '.com'")
    print("✅ URL is valid.")

try:
    pwd = input("Enter password: ")
    validate_password(pwd)

    link = input("Enter URL: ")
    validate_url(link)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Something went wrong:", e)
