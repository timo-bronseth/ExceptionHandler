from ExceptionHandler import ExceptionHandler


def feed_the_AI():
    """
    Ask for user input via the ErrorHandling method.
    """

    # AI requests tea, but has a sense of proper taste.
    user_input = ExceptionHandler.query_options(
        query="\nPlease feed me 'green tea' or 'herbal tea': ",
        error_message="\nYuck! That's not what I wanted!",
        options=["green tea", "herbal tea"],
        ignore_case=True)

    print("\n-AI enjoys a cup of {}-".format(user_input),
          "\nThanks, human!")

    # AI requests integer, any integer.
    ExceptionHandler.query_int(
        query="\nPlease feed me any integer: ",
        error_message="\nYuck! That's not what I wanted!")

    print("\n-AI plays with the integer happily-",
          "\nThanks, human!")


if __name__ == "__main__":
    feed_the_AI()