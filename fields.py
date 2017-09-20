from django.db.models import CharField


class MaxCharField(CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        help_text = 'Не более 255 символов'
        if 'help_text' in kwargs:
            kwargs['help_text'] += '<br/>' + help_text
        else:
            kwargs['help_text'] = help_text
        super(MaxCharField, self).__init__(*args, **kwargs)
