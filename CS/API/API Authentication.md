# API authentication

**`API authentication`** API 요청을 식별하는 과정이다.

전송되는 데이터의 보안과 무결성을 보장하고 인증되지 않은 접근을 예방할 수 있게 한다.

**`방법`**

1. `API Key` API 요청을 인증하는데 사용되늰 유일한 식별자

​		보통 요청의 헤더로 전달되고, 서버는 요청의 신뢰성을 검증하기 위해 키를 사용한다.

2. `OAuth` Open Authorization. 공적인증표준

   유저가 사이트에 저장되는 private resource를 증명서를 공유하는 일없이 다른 사이트와 공유할 수 있게 한다.

​		API 요청을 인증하기 위해 토큰을 사용한다.

3. `Basic Authentication` API 요청의 HTTP 헤더 username과 password를 보내는 간단한 인증체계이다.

   서버는 증명서를 식별하고 API에 대한 접근을 허용 또는 거부한다.

4. `Digested Access Autehntication` 

   Basic Authentication과 비슷하지만, password가 요청에 보내지기전에 일방향 hash function으로 먼저 암호화된다.

   공격자가 password를 가로채고 사용하는 것을 어렵게 만든다.

전송되는 데이터의 민감성과 요구되는 보안의 레벨에 따라 적절한 인증방법을 결정하는 것이 중요하다.