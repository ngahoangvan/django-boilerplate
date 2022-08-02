# avatar path
AVATAR_UPLOAD_TO = "images/avatars"
COVER_PHOTO_UPLOAD_TO = "images/cover-photos"

# gender options
MALE, FEMALE, OTHER, UNKNOW = range(4)
GENDER_OPTIONS = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
    (UNKNOW, 'UNKNOW')
)

# Roles
NORMAL_USER, ADMIN, GUEST = range(3)
ROLE_CHOICES = (
    (NORMAL_USER, 'NORMAL_USER'),
    (GUEST, 'GUEST'),
    (ADMIN, 'ADMIN'),
)
