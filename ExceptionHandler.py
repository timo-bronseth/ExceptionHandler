# -------------------------------------------------------------------------------------
# Timo Brønseth, January 2020.
# -------------------------------------------------------------------------------------


class ExceptionHandler:
    """
    Handles errors arising from queries to the user.
    """

    @classmethod
    def query_options(cls, query: str, error_message: str, options: list, ignore_case: bool = False) -> str:
        """
        Queries the user for input, and recursively calls itself
        until user has entered in one of the values defined in options.
        """

        user_input = input(query)

        if ignore_case:
            user_input = user_input.lower()
            for i, option in enumerate(options):
                options[i] = option.lower()

        try:
            # Check if user_input points to either of the options, and recursively
            # call the function until user_input matches one of them.
            if user_input not in options:
                raise ValueError

        except ValueError:
            # Prompt the user again for a valid entry.
            print(error_message)
            user_input = cls.query_options(query, error_message, options)

        return user_input

    @classmethod
    def query_int(cls, query: str, error_message: str) -> str:
        """
        Queries the user for an integer, and recursively calls
        itself until user has successfully entered an integer.
        """
        user_input = input(query)

        try:
            # Raises a ValueError if user_input cannot be recast as integer.
            if not user_input.isdigit():
                raise ValueError

        except ValueError:
            # Prompt the user again for a valid entry.
            print(error_message)
            user_input = cls.query_int(query, error_message)

        return user_input

    @classmethod
    def query_str(cls, query: str, error_message: str) -> str:
        """
        Queries the user for a non-integer value, and recursively
        calls itself until user has successfully entered such.
        """

        user_input = input(query)

        try:
            # Raises a ValueError if user_input CAN be recast as integer.
            if user_input.isdigit():
                raise ValueError

        except ValueError:
            # Prompt the user again for a valid entry.
            print(error_message)
            user_input = cls.query_str(query, error_message)

        return user_input
