## 241102

### IPO 알고리즘

#### (입력-프로세스-출력 알고리즘)

이 알고리즘은 주어진 입력을 바탕으로 어떤 프로세스를 거쳐서 최종 출력을 생성하는지를 명확히 하는 데 도움을 준다.

#### 테스트 케이스

| A   | B   | C   |
| --- | --- | --- |
| A1  | B1  | C1  |
| A1  | B2  | C2  |
| A2  | B1  | C3  |
| A2  | B2  | C1  |
| A3  | B1  | C2  |
| A3  | B2  | C3  |
| A1  | -   | C3  |
| A2  | -   | C2  |
| ()  |     | ()  |

#### 입력 인자 및 값

| A   | B   | C   |
| --- | --- | --- |
| A1  | B1  | C1  |
| A2  | B2  | C2  |
| A3  | -   | C3  |

### 1. 입력 (Input)

주어진 입력 인자와 값은 다음과 같다:

- **입력 인자**: A, B, C
- **값**:
  - A1, B1, C1
  - A2, B2, C2
  - A3, - , C3 (여기서 B는 비어있다)

### 2. 프로세스 (Process)

프로세스 단계에서는 입력 인자에 따라 가능한 조합을 생성하고, 각 조합에 대해 결과를 도출한다. 이 과정에서 비어 있는 값도 고려해야 한다.

#### 가능한 조합 생성

- A와 B의 모든 조합을 고려한다. C는 A와 B의 조합에 따라 결정된다.
- B가 비어 있는 경우, A의 값에 따라 C의 값을 결정할 수 있다.

#### 조합 예시

1. **A1, B1** → C1
2. **A1, B2** → C2
3. **A2, B1** → C3
4. **A2, B2** → C1
5. **A3, B1** → C2
6. **A3, B2** → C3
7. **A1, -** → C3 (B가 비어있을 때)
8. **A2, -** → C2 (B가 비어있을 때)
9. **A3, -** → C3 (B가 비어있을 때)

### 3. 출력 (Output)

출력은 각 조합에 대한 결과이다. 위의 조합을 바탕으로 다음과 같은 테스트 케이스를 도출할 수 있다:

- (A1, B1) - (C1)
- (A1, B2) - (C2)
- (A2, B1) - (C3)
- (A2, B2) - (C1)
- (A3, B1) - (C2)
- (A3, B2) - (C3)
- (A1, -) - (C3)
- (A2, -) - (C2)
- (A3, -) - (C3)

### 결론

이와 같이 IPO 알고리즘을 사용하여 입력 인자와 값에 기반한 테스트 케이스를 도출할 수 있다. 각 단계에서 가능한 조합을 고려하고, 그에 따른 출력을 명확히 함으로써 테스트 케이스를 효과적으로 생성할 수 있다.
