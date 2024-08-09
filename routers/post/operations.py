from database.db import get_signature_for_title


def empty_signature(mess_text):
    mess_split = mess_text.split("\n\n")
    sign_text = mess_split[-1]
    sign = get_signature_for_title(sign_text)
    if sign:
        return False
    return True


def delete_signature_in_text(mess_text):
    mess_split = mess_text.split("\n\n")[:-1]
    return "\n\n".join(mess_split)


def get_text_and_signature_title_url(mess_text):
    pre_data = mess_text.split("\n\n")
    text = pre_data[:-1]
    sign_title = pre_data[-1]
    sign_url = get_signature_for_title(sign_title)[0]
    return "\n\n".join(text), sign_title, sign_url
