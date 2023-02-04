import argparse  # https://docs.python.org/ko/3/library/argparse.html

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


def help_(*_args, **_kwargs):
    print(HELP_MESSAGE)


parser = argparse.ArgumentParser(
    prog='My Git',
    description='Cloning Git project',
    epilog='mgit',
    add_help=False,
)

parser.add_argument('-v', '--version', action='store_true')
parser.add_argument('-h', '--help', action='store_true')

args = parser.parse_args()
if args.version:
    version()
if args.help:
    help_()
