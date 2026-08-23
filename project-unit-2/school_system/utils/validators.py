def validate_name(name):
    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    return name


def validate_age(age_text):
    try:
        age = int(age_text)
    except (TypeError, ValueError) as error:
        raise ValueError("Age must be a whole number.") from error
    else:
        if age <= 0:
            raise ValueError("Age must be greater than zero.")
        return age


def validate_text(value, field_name):
    value = value.strip()
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")
    return value
