# Redis

내장 메모리 데이터 구조 store로, 데이터베이스, 캐시, 메시지 브로커로 사용될 수 있다.

**`지원하는 데이터 타입`**

- String, Hash, List, Set, sorted set, bitmap, hyperloglog, geospatial index

**`다른 DB와 비교시 이점`**

- 데이터를 메모리에 저장하므로, 빠르다.
- 다수의 데이터 타입을 지원하여 복잡한 데이터와 작업하기 쉽다.
- 데이터를 조작하고 쿼리하는 많은 세트의 command가 있다.
- 캐시에 대한 완벽한 지원을 해, 다른 DB에서 보통 캐시로 사용된다.

많은 사람들이 사용하며 크고 활동적인 커뮤니티를 가지고 있다.

BSD 3-Clause 라이센스 open-source 프로젝트이다.