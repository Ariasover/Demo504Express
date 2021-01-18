from django.core.validators  import RegexValidator

phone_regex = RegexValidator(
    regex=r'\+?1?\d{9,15}$',
    message='Phone number must be entered in the correct +99999999'
)