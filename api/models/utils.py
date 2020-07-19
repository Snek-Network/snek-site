class ModelReprMixin:
    """Mixin providing a `__repr__` method."""

    def __repr__(self):
        attributes = ' '.join(
            f'{attribute}={value!r}'
            for attribute, value in sorted(
                self.__dict__.items(),
                key=lambda tup: tup[0]
            )
            if not attribute.startswith('_')
        )
        return f'<{self.__class__.__name__}({attributes})>'
