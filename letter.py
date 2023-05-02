template = """
Dear {name},

I hope this letter finds you well. I am writing to {reason}.

{additional_info}

Thank you for your attention to this matter.

Sincerely,
{sender_name}
"""

# get user input
name = input("Recipient's name: ")
reason = input("Reason for writing: ")
additional_info = input("Additional information: ")
sender_name = input("Your name: ")

# generate letter
letter = template.format(name=name, reason=reason, additional_info=additional_info, sender_name=sender_name)

# print letter
print(letter)
