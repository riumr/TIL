## Figma 앱 생성 메뉴얼 예제

### Figma

- Figma 컴포넌트 생성

  - 컴포넌트 라이브러리 사용 시

    - 사용할 라이브러리 선택 `simple design system`
    - 해당 라이브러리에서 사용할 컴포넌트 선택 `Checkbox Field`

      ![Checkbox Field](Checkbox%20Field.png)

  - 컴포넌트 이름 정의 `체크박스 필드`
  - event 설정 `click`
  - 공통 컴포넌트로 사용할 컴포넌트인지 구별 `공통 컴포넌트로 사용`

- 디자인 시스템 정의

  - 폰트 수준(단계)별 설정

    ![디자인 시스템](image.png)

  - 색상 팔레트
    - 색상 수 설정
    - 색상 단계 설정
  - 테두리
    - 모양
    - 굵기
    - 색
  - 바로 사용할 수 있는 수준까지 상세하게 정의하는 게 좋다.

- 기능정의

  - event별 state 변화/이동 결정

- 애니메이션 정의
  - 발동 조건 event 설정
  - 효과 설정
  - 시간 설정

### VSCODE(code editor)

- React 컴포넌트 파일 생성
- React 컴포넌트와 Figma 컴포넌트 매칭 : Figma 컴포넌트별로 React 컴포넌트 생성
- Figma 컴포넌트 단계에 맞춰 React 컴포넌트 내부 계층 생성
- 각 css property Figma 컴포넌트별로 적용된 디자인 시스템 설정

### 테스트 구현

- React 컴포넌트 별 테스트 진행 : cypress로 React 컴포넌트별 단위테스트를 할 수 있다.
- 단위, 통합, 시스템 테스트까지 진행
- 직접 작동해서 실행시키는 것보다 코드를 통해 테스트하면 정상적으로 작동하는지 확인하는 시간을 단축할 수 있다.
