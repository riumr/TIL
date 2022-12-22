# bootsrap

## Layout_breakpoint

bootsrap sass 활용

```scss
$grid-breakpoints: (
  xs: 0,
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px,
  xxl: 1400px
);
```

설정 후 사용방식

```scss
@media (min-width: 576px) { ... }
```

## content

### Reboot

**표현 가능한 것들**

`Horizental Rules` `Lists` `Inline Code` `Code blocks` `Variable`

`User input(highlight)` `Sample output` `Tables` **`Forms`** `button`

`address` `Blockquote` `Inline elements` **`Summary`**

### Typography

Typography를 조작할 수 있다. 감각적인 디자인을 원할 때 유용하다.

### Images

이미지의 크기와 위치를 조작할 수 있다. 조작법을 참고할 수 있을 것이다.

### Tables

감각적인 Table을 만들 수 있게 해 준다.

#### Figures

caption 있는 이미지를 삽입한다.

## Forms

다양한 형태의 Form을 제작할 수 있다. 거의 모든 형태의 Form을 제작할 수 있다.

```html
<form action="" method="">
	<label for="ID"></label>
  <input id="ID">
</form>
```

**Range**

```html
<label for="customRange1" class="form-label">Example range</label>
<input type="range" class="form-range" id="customRange1">
```

## Utilities

`background` `borders` `colors` `display` `flex` `float` `interaction(text)`

**`opacity(투명도)`** `overview` `position` `shadow` `sizing` `spacing` **`Text`**

`vertical alignment` `visability`