# Basic Auth

HTTP 프로토콜에 내장된 간단한 인증 체계이다.

client가 다음과 같은 authentication header를 HTTP 요청과 함께 보내는 방식이다.

```shell
Authentication: Basic [username:password base-64 encoded string]
```

유저정보가 텍스트에 담겨 전송되기 때문에 공격자에게 뺏길 수 있어 많이 안전하지는 않다.

보통 HTTPS와 결합해 최소한의 보안을 제공하는 데만 사용된다.