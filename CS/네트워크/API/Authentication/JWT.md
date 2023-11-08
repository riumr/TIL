# JWT

**`JSON Web Tokens`**

당사자 간에 정보를 JSON 개체로 안전하게 전송하기 위한 간결하고 독립적인 방법을 정의하는 개방형 표준(RFC 7519)이다.

- 이 정보는 디지털 방식으로 서명되기때문에 인증되고 신뢰될 수 있다.

- JWT는 secret key나 public/private key(RSA나 ECDSA 사용)에 의해 인증될 수 있다.

보통 유저를 인증하기 위해 사용된다.

- 유저가 로그인하면 다음 요청들은 JWT를 포함하며, 유저가 그 토큰으로 허락된 route. 서비스. 자원에 접근할 수 있게 한다.
- 그러므로 client가 매 요청마다 로그인 정보를 보낼 필요없이 인증할 수 있게 해준다.

세가지 파트로 구성된다.

- **`Header`** JWT가 encoding되는 정보를 방법을 포함한다.
  - Token type : JWT
  - 사용된 sigining 알고리즘 : RSA나 HMAC SHA256
- **`Payload`** claim을 포함한다. claim은 독립객체(보통 user)와 추가 데이터에 관한 설명이다.
- **`Signature`** JWT 전송자가 그것을 작성한 사람이라는 것을 인증하기 위해 사용되며, 메시지가 전송되는 동안 변경되지 않았다는 것을 보장한다.