# CORS

**`CORS`** Cross Origin Resource Sharing

웹 페이지가 지정된 페이지가 아닌 다른 페이지에 요청을 보내는 것을 막는 웹 브라우저 내장 기능이다.

악의적인 웹페이지가 다른 사이트로부터 민감한 정보를 빼앗는 것을 막기위한 것이다.

어떤 도메인이 웹 서버에 접근할 수 있는지 식별하게 하며, 웹 브라우저는 이런 것을 강제한다.

웹 페이지가 CORS header에 명시되지 않은 다른 도메인에 접근하는 요청을 만드려고하면, 브라우저는 이를 막고 페이지는 어떤 데이터도 받을 수 없다.