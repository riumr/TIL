# NoSQL

표 형식이 아니며, RDB와는 다른 방식으로 데이터를 저장한다.

주요 유형으로는 문서, 키-값, 와이드컬럼, 그래프가 있다.

**부상하게 된 배경** : 다음을 지원했기 때문이다.

1. 2000년대 말에 저장매체 비용 크게 하락했다.
   - 저장소 관리 비용보다 개발자의 생산성을 더 중시했다.
2. 저장 비용이 상승하면서 엄청난 양의 비정형 데이터 처리의 필요성이 커졌다.
3. 요구사항이 지속적으로 변하는 환경
4. 클라우드 컴퓨팅이 발달함에 따라 스케일아웃의 필요성이 커졌다.

**등장하기 전** 소프트웨어 엔지니어들은 변화하는 요구사항에 대처하여 데이터 모델을 설계하는데 어려움을 겪었다.

**유형**

`문서데이터베이스` JSON과 비슷한 문서에 데이터를 저장한다. MongoDB가 대표적이다.

`키-값 데이터베이스`

- 대량의 데이터를 저장해야하지만 검색을 위한 복잡한 쿼리를 수행할 필요가 없는 경우에 적합하다.
- 일반적인 사용자 선호도 저장 또는 캐싱에서 사용된다.
- Redis와 DynanoDB가 대표적이다.

`와이드 컬럼 스토어` 대표적으로 Cassandra와 HBase가 있다.

`그래프 데이터베이스` 

	- 노드와 엣지에 데이터를 저장한다. 
	- 노드에는 사람, 장소, 사물에 대한 정보가 저장되고 엣지에는 노드 간 관계에 대한 정보가 저장된다.
	- 소셜네트워크, 사기탐지 같이 패턴을 검토해야하는 작업에 적합하다.
	- 대표적으로 Neo4j와 JanusGraph가 있다.