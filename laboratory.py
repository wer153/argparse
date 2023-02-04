import argparse

VERSION = '0.0.0'
HELP_MESSAGE = """사용법: git [-v | --version] [-h | --help] <command> [<args>]

다음은 여러가지 상황에서 자주 사용하는 mgit 명령입니다:

보조 명령 / 정보 획득 기능
   version       mgit의 버전 정보를 표시합니다

저수준 명령/ 조작 기능
   hash-object   오브젝트 ID를 계산하고 선택적으로 파일의 블롭을 만듭니다
"""


def version(*_args, **_kwargs):
    print(VERSION)


def help(*_args, **_kwargs):
    print(HELP_MESSAGE)


arg_to_detail = {
    'version': {
        'short': 'v',
        'action': 'store_true',
        'function': version,
    },
    'help': {
        'short': 'h',
        'action': 'store_true',
        'function': help,
    },
}

parser = argparse.ArgumentParser(
    prog='My Git',
    description='Cloning Git',
    epilog='mgit',
    add_help=False,
)


def get_args(arg: str, detail: dict) -> tuple:
    args = []
    try:
        short, action = detail.get('short'), detail['action']
    except KeyError as error:
        raise ValueError(f'arg_to_detail: fill my value for the key({str(error)}) of {arg}')
    if short:
        args.append(f'-{short}')
    args.append(f'--{arg}')
    return tuple(args)


def get_kwargs(arg: str, detail: dict) -> dict:
    kwargs = {}
    try:
        action = detail['action']
    except KeyError as error:
        raise ValueError(f'arg_to_detail: fill my value for the key({str(error)}) of {arg}')
    kwargs |= {'action': action}
    return kwargs


for arg, detail in arg_to_detail.items():
    args: tuple
    kwargs: dict
    args, kwargs = get_args(arg, detail), get_kwargs(arg, detail)
    get_args(arg, detail), get_kwargs(arg, detail)
    parser.add_argument(*args, **kwargs)


# parser.add_argument('-v', '--version', action='store_true')
# parser.add_argument('-h', '--help', action='store_true')

args = parser.parse_args()
for arg, detail in arg_to_detail.items():
    if hasattr(args, arg):
        try:
            function = detail['function']
        except KeyError as error:
            raise ValueError(f'arg_to_detail: fill my value for the key({str(error)}) of {arg}')
        function = detail['function']
        function(getattr(args, arg))
#
# if args.version:
#     print(version)
# if args.help:
#     print(help_message)
