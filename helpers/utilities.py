class Utilities(object):

    """
    convert a string to a class if the class exists
    """
    @staticmethod
    def str_to_class(context):
        context_is_instance = isinstance(globals()[context], types.ClassTypes)
        if context in globals() and context_is_instance:
            return globals()[context]
        return None
