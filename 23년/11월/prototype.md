## 231123
### Javascript 스터디

### `prototype`
- `Javascript` 에서 객체를 상속하는 객체를 가리키는 속성
- `Javascript`는 prototype 기반 언어이며 `prototype chain`이 존재한다.
    * `prototype chain`
        - 하위 객체에서 상위 객체의 메소드와 속성을 물려받는 것
        - 상속되는 메소드나 속성은 `prototype`이라는 속성에 정의되어 전해진다.
        - 객체에서 메소드를 호출했을 때, 그 객체가 메소드를 가지고 있지 않으면 브라우저는 그 객체의 `prototype`을 뒤지며 메소드를 가지는지 찾는다.
        ```js
        function Person(name,age){
            this.name = name;
            this.age = age;
        }
        var personA = new Person("john",20)
        ```
        - `personA`는 `Person()`의 **prototype** 객체이며, `Person()`은 `Object`의 **prototype**객체이다.
        - `prototype chain` : `Object` -> `Person()` -> `personA`
        - 따라서 메소드를 호출하면 `personA`부터 시작해 `Ojbect`까지 메소드의 정의여부를 체크하고, 해당하는 값을 반환한다.
        - 예를 들어, `personA`에서 `name` 메소드를 호출하면 `personA`에 `name`이 정의되어 있기 때문에 정의된 값 `john`을 반환한다.
- 상속되는 멤버 목록은 `생성자.prototype` 코드로 확인할 수 있다.
- `생성자.prototype.메소드=funcion()` 코드로 **생성자**에 메소드를 추가할 수 있으며, 추가한 메소드는 해당 **생성자**로 만들어진 모든 객체에서 사용할 수 있다.
    - 같은 코드로 다시 메소드를 호출해 수정할 수도 있다.