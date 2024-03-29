# ACID Transactions

데이터 트랜잭션이 안전하게 수행된다는 것을 보장하는 성질의 약어

**`Atomicity(원자성)`** 트랜잭션 과정 전체가 온전히 실행된다.

**`Consistendy(일관성)`** 전체 데이터베이스가 트랜잭션의 조건을 충족하는 상태로 유지된다.

**`Isolation(독립성)`** 트랜잭션 중간에 끼어들지 못한다.

**`Durablility(지속성)`** 성공적으로 수행된 트랜잭션은 로그로 반영된다.

## 구현

기본적으로 데이터에 `LOCK` 을 걸고 하는 두 가지 방식이 있다.

**`로깅방식`** DB 데이터를 업데이트하기전에 로그에 모든 변경사항을 기록하는 것

**`섀도우페이징`** 변경이 DB의 복사본에 저장된다.

`LOCK` 의 대안으로 모든 데이터를 별도 복사본으로 유지하는 MVCC 방식도 있다.