# Token Authentication

어플리케이션이나 시스템에 요청을 보내고 있는 유저나 `client`를 식별하는 방법이다.

각 요청에 유저명과 비밀번호를 보내는 대신, 유저나 `client`는 다음 보내지는 요청과 보낼 수 있는 고유 `token`을 발행한다.

`token`은 보통 길고 무작위로 만들어진 문자열이며, `client-side`(브라우저 cookie나 모바일 기기)에 저장된다.

보통 `RESTful APIs`에 자주 사용되며, `session-based authentication`의 대체재이다.