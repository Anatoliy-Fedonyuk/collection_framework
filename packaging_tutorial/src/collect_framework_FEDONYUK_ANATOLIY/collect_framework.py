"""--This file is the entry point application Collection Framework--"""
from functools import lru_cache
import click
from loguru import logger

logger.add('debug.log', colorize=True, format='{time} {level} {message}', level='DEBUG')


@lru_cache(typed=True, maxsize=1024)
def get_number_char(string: str) -> int:
    """The function returns the number of characters in a string that occur only once"""
    try:
        return sum(1 for ch in string if string.count(ch) == 1)
    except Exception as ex:
        logger.error(f"[ERROR] An error occurred in get_number_char: {ex}")
        raise


@click.command()
@click.option('--string', '-s', help='The string to process')
@click.option('--file', '-f', type=click.Path(exists=True), help='The path to the input text file')
def main(string: str, file: str) -> None:
    """This function implements the command line interface for the function get_number_char.
    In this case, the --file command will take precedence!"""
    try:
        if not string and not file:
            return click.secho('Either --string or --file must be provided!', bg='bright_white', fg='black')
        if file:
            with open(file, encoding='utf-8') as f:
                string = f.read()

        result = get_number_char(string=string)
        click.secho(f'THERE ARE {result} UNIQUE CHARACTERS IN THIS TEXT!', bg='bright_white', fg='black')
    except Exception as e:
        logger.error(f"[ERROR] An error occurred in main: {e}")
        raise


def get_collection_number(strings: list[str] | tuple[str]) -> list[int]:
    """function returns the number of characters in st rings that occur only once"""
    try:
        return list(map(get_number_char, strings))
    except Exception as ex:
        logger.error(f"[ERROR] An error occurred in get_collection_number: {ex}")
        raise


def do_collection_checks(collection: list[str] | tuple[str] | str) -> list[int]:
    """function returns the numbers of characters in the collection"""
    try:
        match collection:
            case str(col) if col:
                return [get_number_char(col)]
            case list(col) | tuple(col) if col:
                if all(isinstance(item, str) and item for item in col):
                    return get_collection_number(col)
        logger.error("[ERROR] TypeError - only a string and collections of strings are expected.")
        raise TypeError('--only not empty strings and collections of strings are expected--')
    except Exception as e:
        logger.error(f"[ERROR] An unexpected error occurred in do_collection_checks: {e}")
        raise


if __name__ == '__main__':
    # main()  # Operating mode for the command line.
    logger.info("[INFO] Start working application in mode __main__!")
    assert do_collection_checks("wmmmmmmmwww") == [0]
    assert do_collection_checks("Толя") == [4]
    assert get_collection_number(["abbbccdf", " "]) == [3, 1]
    assert do_collection_checks(["abbbccdf", '#####!##################']) == [3, 1]
    logger.info("[INFO] All Assertion - is True !")

