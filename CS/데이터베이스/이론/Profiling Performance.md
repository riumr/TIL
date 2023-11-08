# Profling Performance

**`Profling Performance`**

CPU time, memeory, 네트워크 대역폭과 같은 리소스 사용 측면에서 컴퓨터시스템, 기기, 프로그램의 performance를

측정하고 분석하는 것이다.

**`목적`** 낮은 performance를 유발하는 요인을 식별하고 분석해 효율성과 반응성을 개선하는 쪽으로 시스템이 최적화되고

개선될 수 있도록 하는 것이다.

**`접근법`**

1. **`sampling`**

​		performance 핫스팟과 병목지점을 식별하기 위해 주기적으로 시스템 performance에 관한 데이터를 수집하고 

​		그것을 분석하는 것이다.

2. **`Instrumentation`** 

​		performance 데이터를 측정하고 기록하는 추가적인 코드를 포함하도록 시스템이나 프로그램을 수정하는 것이다.

3. **`Tracing`**

​		다양한 요소가 어떻게 상호작용하고 performance가 어떻게 영향받는지 볼 수 있도록

​		시스템이나 프로그램의 실행동안 일어난 이벤트들의 결과를 기록하는 것이다.

`Performance Profiling` 도구는 컴퓨터, 모바일 기기, embedded system과 같은 광범위한 시스템에서 가능하다.

이러한 도구는 CPU 활용, 메모리 사용, 네트워크 활동, disk 입출력과 같은 시스템 performance의 다양한

측면을 프로파일하기 위해 사용될 수 있다.

어떤 도구는 다양한 함수나 코드블록의 소요시간을 알려줄 수 있고, 그건 낮은 performance를 내고있는

시스템이나 프로그램의 구역을 식별할 수 있게 해준다.

**`Performance Profiler`** 를 효과적으로 사용하기 위해서는 프로파일되는 시스템과 프로그램의 작동목적과 특징들에 대한

명확한 이해를 가지고, 또한 잠재적 performace 병목과 trade-off에 대해서도 아는 것이 중요하다.

최우선인 performance issue를 식별하고 우선순위로 분류해 효과적인 최적화 전략을 개발하기 위해, performace data를 

분석하고 해석하는 시스템적 접근을 가지는 것도 중요하다. 