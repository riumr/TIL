# POSIX

**`POSIX`** Portable Operating System Interface

C언어로 작성된 프로그램의 인터페이스 표준 조합

IEEE가 다양한 OS에 사용될 수 있는 API 표준을 제공하기 위해 만들었다.

OS와 상호작용하는 많은 API들을 정의했다.

- 파일과 디렉토리 관리를 위한 함수
- 프로세스 관리
- 프로세스간 통신
- signal handling

Command-line 유틸리티도 정의했다.

- ls, grep, sed

POSIX의 이점은 다양한 운영체제에서 프로그램의 일반적인 인터페이스를 제공한다는 것이다.

따라서 POSIX 표준에 따라 작성된 프로그램은 여러 OS에서 코드의 주요한 변화 없이 컴파일하고 실행할 수 있다.