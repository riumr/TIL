# AWS Elastic Beanstalk + Github Actions

<aside>
🔔 이 가이드는
S3 와 RDS 설정 후 진행할 수 있습니다.

</aside>

<aside>
🔔 이 가이드는
IAM / AWS Beanstalk / Django / Github Actions
로 구분됩니다.

AWS는 잘못된 사용을 할 경우 많은 과금이 발생할 수도 있습니다.
**두 개 이상의 Beanstalk 애플리케이션을 생성하면 과금이 발생할 수 있습니다.**
**가이드를 잘 보고 따라해주세요.**

</aside>

<aside>
🇰🇷 지역 설정 - 서울
**경고 : 다른 지역에서 생성한 Beanstalk 애플리케이션은 모두 삭제해아합니다.**

</aside>

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled.png)

# IAM

<aside>
📌 ***기존 IAM 사용자***에 `AdministratorAccess-AWSElasticBeanstalk` 권한 추가

</aside>

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%201.png)

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%202.png)

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%203.png)

# ****Elastic Beanstalk****

### 애플리케이션 ****생성****

<aside>
📌 검색창 ****`Elastic Beanstalk`** 검색 - 페이지 이동
애플리케이션 생성

</aside>

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%204.png)

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%205.png)

<aside>
📌 애플리케이션 및 환경 생성이 끝날 때까지 기다립니다.
환경 상태가 `OK` 가 되면 생성이 끝난 상태입니다.

</aside>

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%206.png)

### Elastic Bean 환경 변수 설정

<aside>
📌 환경 - 구성 - 소프트웨어 - 편집

</aside>

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%207.png)

<aside>
📌 배포 환경에 필요한 환경 변수를 등록합니다.

필수 환경 변수
AWS_ACCESS_KEY_ID : AWS IAM 액세스 키
AWS_SECRET_ACCESS_KEY : AWS IAM 시크릿 키
AWS_STORAGE_BUCKET_NAME : AWS S3 버킷 이름
DATABASE_HOST : AWS RDS 데이터베이스 엔드포인트
DATABASE_NAME : AWS RDS 접속 데이터베이스 이름
DATABASE_PASSWORD : AWS RDS 접속 데이터베이스 패스워드
DEBUG : False

기본 환경 변수
PYTHONPATH : 기본으로 작성

</aside>

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%208.png)

# 장고

### ALLOWED_HOSTS

<aside>
📌 settings.py `ALLOWED_HOSTS` 수정

</aside>

```python
ALLOWED_HOSTS = [
		# "Elastic Beanstalk URL",
    # 예시 "sharestreet-env.eba-xqbmviyc.ap-northeast-2.elasticbeanstalk.com",
    "127.0.0.1",
    "localhost",
]
```

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%209.png)

### .ebextensions

<aside>
📌 1️⃣ manage.py가 위치한 폴더에 `.ebextensions` 폴더 생성
2️⃣ .ebextensions 안에 `django.config` 파일 생성
3️⃣ django.config 파일 내용 작성

</aside>

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%2010.png)

```json
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: [프로젝트명].wsgi:application
  
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /[STATIC_URL]: [STATIC_ROOT]

container_commands:
  01_migrate:
    command: "source /var/app/venv/*/bin/activate && python3 manage.py migrate"
    leader_only: true
  02_collectstatic:
    command: "source /var/app/venv/*/bin/activate && python3 manage.py collectstatic --noinput"
```

예시

```python
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
```

```
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: config.wsgi:application
  
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: staticfiles

container_commands:
  01_migrate:
    command: "source /var/app/venv/*/bin/activate && python3 manage.py migrate"
    leader_only: true
  02_collectstatic:
    command: "source /var/app/venv/*/bin/activate && python3 manage.py collectstatic --noinput"
```

# Github Actions

<aside>
❓ Github Actions는 Github에서 제공하는 
***CI(Continuous Integration, 지속 통합)/ CD(Continuous Deployment, 지속 배포)***
서비스입니다.
특정 이벤트(Push, Pull Request)에 반응하여 ***자동으로*** 특정 작업을 실행시킬 수 있는 서비스입니다.
이 가이드에서는 이벤트에 반응하여 Elastic Beanstalk 배포 작업을 실행하게 할 것입니다.

</aside>

### Gthub Actions workflow 작성

<aside>
📌 1️⃣ manage.py가 위치한 폴더에 `.github` 폴더 생성
2️⃣ .github 폴더 안에 `workflows` 폴더 생성
3️⃣ workflows 폴더 안에 `deploy.yml` 파일 생성
4️⃣ deploy.yml 파일 내용 작성(주석은 삭제할 것 총 8줄)

</aside>

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%2011.png)

```yaml
name: EB_Deploy

on:
  push:
    branches: ***[팀 내 default 브랜치이름]**
		# 예시
		#* branches: [main]
  pull_request:
    branches: ***[팀 내 default 브랜치이름]**
		# 예시
		#* branches: [main]

jobs: 
  deploy: 
      runs-on: ubuntu-latest

      steps:
      - name: Checkout source code
        uses: actions/checkout@v2

      - name: Generate deployment package
        run: zip -r deploy.zip . -x '*.git*'
      
      - name: Get timestamp
        uses: gerred/actions/current-time@master
        id: current-time

      - name: Run string replace
        uses: frabert/replace-string-action@master
        id: format-time
        with:
          pattern: '[:\.]+'
          string: "${{ steps.current-time.outputs.time }}"
          replace-with: '-'
          flags: 'g'
      - name: Deploy to EB
        uses: einaregilsson/beanstalk-deploy@v20
        with:
          aws_access_key: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws_secret_key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          application_name: ***[Beanstalk 애플리케이션 이름]**
					# 예시
					# application_name*: "kdt-django-bean"
          environment_name: ***[Beanstalk 환경 이름]**
					# 예시
****					# environment_name*: "Kdtdjangobean-env"
          version_label: "python-${{ steps.format-time.outputs.replaced }}"
          region: "ap-northeast-2"
          deployment_package: deploy.zip
```

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%2012.png)

<aside>
📌 GitHub Repo - 아래 두 가지 secrets 생성
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY

</aside>

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%2013.png)

![Untitled](AWS%20Elastic%20Beanstalk%20+%20Github%20Actions%20c105ef4b786245369cbdbc4d2be270dd/Untitled%2014.png)

### Github Action 작동 확인

<aside>
📌 Push 후 Action이 정상적으로 작동하는지 확인 
이후에는 이벤트(Push or Pull Request)가 실행될 때 자동으로 배포가 진행 됩니다.

</aside>

<aside>
⚠️ 개발 중 환경 변수가 추가되면 Elastic Beanstalk 환경 구성에 환경 변수를 추가해야 합니다.

</aside>

### 에러 상황

<aside>
⚠️ Elastic Beanstalk / Github 환경 변수 미설정 또는 오타

</aside>

<aside>
⚠️ Github Actions workflow 파일 작성 오타

</aside>